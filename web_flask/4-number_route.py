#!/usr/bin/python3
" script that starts a Flask web application "

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    "prints Hello HBNB on the main route"
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "display “HBNB”"
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def parse_C(text):
    "display “C ” followed by the value of the text variable"
    new_str = text.replace('_', ' ')
    return "C " + new_str


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def parse_python(text="is_cool"):
    "display “Python ”, followed by the value of the text"
    new_str = text.replace('_', ' ')
    return "Python " + new_str


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    "display “n is a number” only if n is an integer"
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
