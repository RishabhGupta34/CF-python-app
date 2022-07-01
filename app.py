from flask import Flask
import os
import sys

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Python on Cloud Foundry APP ' + sys.argv[1] + '!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[2]))
