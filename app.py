from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.after_request
def remove_header(response):
    del response.headers['cache-control']
    return response
