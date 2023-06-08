from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    container_id = os.uname()[1]
    return f"<h1>Container ID: {container_id}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
