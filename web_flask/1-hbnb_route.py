#!/usr/bin/python3
from flask import Flask
" script that starts a Flask web application "
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    "prints Hello HBNB on the main route"
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "display “HBNB”"
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
