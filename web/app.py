import os

DEBUG = os.environ.get("DEBUG", "false") == "true"

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flaska Dockerized'


@app.route("one")
def one():
	return "One"


@app.route("two")
def two():
    return "two = 2"


@app.route("three")
def three():
    return "3"


if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0", debug=DEBUG)