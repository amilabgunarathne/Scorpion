# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:36:54 2018

@author: Kanchana Ranasinghe
"""

from flask import Flask, request, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify


db_connect = create_engine('sqlite:///scorpion.db')
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    resp = Response({}, status=200, mimetype='application/json')
    return resp

@app.route('/api/users', methods = ['POST'])
def user(user_id):
    if request.method == 'POST':
        data = request.json  # a multidict containing POST data

        if data['email'] is None:
            resp = Response({}, status=400, mimetype='application/json')
            return resp
        else:
            conn = db_connect.connect()
            email = data['email']
            query = conn.execute("select count(*) from userdata where email='"+email+"'").fetchall()

            if query[0][0] > 0:
                resp = Response({
                         "status": 409,
                         "message": "A user with email: {email} already exists.",
                         "developerMessage": "User creation failed because the email:" + email + "already exists.",
                        }, status=409, mimetype='application/json')
                return resp
            else:
                conn = db_connect.connect()
                email = data['email']
                password = data['password']
                query = conn.execute("insert into userdata values('" + email + "', '" + password + "')")
                resp = Response({
                         "self": "http://localhost:8090/api/users/" + email,
                          "email": email,
                        }, status=201, mimetype='application/json')
                return resp

if __name__ == '__main__':
     app.run(port=8090, host="0.0.0.0")
