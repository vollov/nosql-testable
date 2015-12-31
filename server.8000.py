#!/usr/bin/python

from flask import Flask, jsonify, make_response, abort, request, json

app = Flask(__name__)


############################################################
#  Restful api registration strat
############################################################

def register_blueprints(application):

    from api import account
    application.register_blueprint(account)
    
    
@app.route('/')
def index():
    return "Hello, World!"

register_blueprints(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)