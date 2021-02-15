from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    del response.headers['Cache-Control']
    return 'Hello, World!'
