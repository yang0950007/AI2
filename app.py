from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('input_data.html')

@app.route('/submit_form', methods=['POST'])
def handle_form():
    id_number = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    email = request.form.get('email')

    # Validate ID number (assuming it's numeric)
    if not re.match(r'^\d+$', id_number):
        return "Invalid ID number: must contain only digits", 400

    # Check ID number length
    if len(id_number) != 10:
        return "Invalid ID number: length must be 10", 400

    # Check if the first character is an English alphabet and convert it to corresponding number
    first_char = id_number[0]
    if not first_char.isalpha():
        return "Invalid ID number: first character must be an English alphabet", 400
    else:
        # Convert the first character to corresponding number
        first_char_num = ord(first_char.upper()) - 64 + 9  # A is 10, B is 11, ..., Z is 33

    # Multiply the first digit by 1 and the second digit by 9
    first_digit = first_char_num // 10
    second_digit = first_char_num % 10
    result = first_digit * 1 + second_digit * 9

    # Multiply the third to ninth digits by 8, 7, 6, 5, 4, 3, 2, 1
    for i in range(2, 10):
        result += int(id_number[i]) * (10 - i)

    # Add the last digit
    result += int(id_number[-1])

    # Check if the result is divisible by 10
    if result % 10 != 0:
        return "Invalid ID number: check digit does not match", 400

    # Validate name (assuming it's alphabetic)
    if not re.match(r'^[A-Za-z\s]+$', name):
        return "Invalid name: must contain only alphabetic characters and spaces", 400

    # Validate gender
    if gender not in ['Male', 'Female']:
        return "Invalid gender: must be 'Male' or 'Female'", 400

    # Validate email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Invalid email", 400

    return "All entries are valid", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces and port 80
