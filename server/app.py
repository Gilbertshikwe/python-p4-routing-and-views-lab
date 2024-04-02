#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the string in the console
    return f'<h1>{param}</h1>'  # Display the string in the web browser

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(1, param + 1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == 'mod':
        result = num1 % num2
    else:
        return 'Invalid operation'
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
