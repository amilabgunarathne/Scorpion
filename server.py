# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:36:54 2018

@author: Kanchana Ranasinghe
"""

from flask import Flask, request, Response
from flask_api import status
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

#db_connect = create_engine('sqlite:///scorpion.db')
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    resp = Response({}, status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
     app.run(port=8090)