from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    uri = os.environ["DATABASE_URI"]
    return f'Hello, World! {uri}'
