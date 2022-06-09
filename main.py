from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/a')
def hello():
    return 'Where are you'

@app.route('/b')
def hello():
    return 'not here either'

@app.route('/c')
def hello():
    return 'neither'