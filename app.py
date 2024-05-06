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

    # Check if the first character is an English alphabet
    if not id_number[0].isalpha():
        return "Invalid ID number: first character must be an English alphabet", 400

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
