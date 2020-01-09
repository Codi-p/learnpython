# !python
#

from flask import Flask
from flask import current_app
from flask import g
from flask import request
from flask import session

app = Flask(__name__)

@app.route('/')
def index():    
    return '<h1>Hello world! Your browser is {} </h1>'.format(request.headers)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {}!</h1>'.format(name)

