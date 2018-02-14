# this is a test commit from Brady
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Bill I am committing this and testing the server.'
