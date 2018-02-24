# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:36:54 2018

@author: Kanchana Ranasinghe
"""

from flask import Flask, request, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps, loads
from flask_jsonpify import jsonify

from server03 import check_password, random_password

db_connect = create_engine('sqlite:///scorpion.db')
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    resp = Response({}, status=200, mimetype='application/json')
    return resp

@app.route('/api/users', methods = ['POST'])
def user():
    if request.method == 'POST':
        data = loads(request.data, strict=False)
        conn = db_connect.connect()
        if 'email' in data.keys():

            email = data['email']

            if 'password' not in data.keys():
                password = check_password(random_password())
                autogen = True
            else:
                password = check_password(data['password'])
                autogen = False


            #checking password errors
            if password == 'error':
                    resp = Response(dumps({"status": 400, "message": "Password complexity requirement not met",
                                           "developerMessage": "User creation failed because password complexity requirement not met"}), status=400)
                    return resp

            #check if username already present
            query = conn.execute("select count(*) from userdata where email='"+email+"'").fetchall()
            if query[0][0] > 0:
                resp = Response(dumps({ "status": 409,
                         "message": "A user with email: " + email + " already exists.",
                         "developerMessage": "User creation failed because the email: " + email + " already exists.",
                        }), status=409)
                return resp

            #username not already present
            else:
                query = conn.execute("insert into userdata('email','password') values('" + email + "', '" + password + "')")
                user_id= conn.execute("select userid from userdata where email='" + email + "'").first()[0]
                out_dict = {"self": "http://192.168.53.223:8090/api/users/" + str(user_id),
                          "email": email,}

                #for optional mobile number
                if 'mobile' in data.keys():
                    mobile = data["mobile"]
                    conn.execute("update userdata set mobile='"+mobile+"' where userid="+str(user_id))
                    out_dict["mobile"] = mobile

                #send text message to user with password

                else:
                    #send email to user
                    pass

                #decide user role type
                if 'role' in data.keys():
                    role = data["role"]
                    if role not in ["user", "moderator", "admin"]:
                        resp = Response(dumps({}),status=400)
                        return resp
                else:
                    role = "user"
                conn.execute("update userdata set role='"+role+"' where userid="+str(user_id))
                out_dict["role"] = role

                resp = Response(dumps(out_dict), status=201)
                return resp

        #email not sent by cllient in POST data
        elif 'email' not in data.keys():
            resp = Response(dumps({}), status=400)
            return resp
        return ""
    return ""


@app.route('/api/faculties', methods = ['POST'])
def faculties():
    if request.method == 'POST':
        data = loads(request.data, strict=False)
        conn = db_connect.connect()
        if 'name' in data.keys():

            name = data['name']

            #check if faculty name already present
            query = conn.execute("select count(*) from faculties where name='"+name+"'").fetchall()
            if query[0][0] > 0:
                resp = Response(dumps({ "status": 409,
                         "message": "A faculty with name: " + name + " already exists.",
                         "developerMessage": "Faculty creation failed because the faculty name: " + name + " already exists.",
                        }), status=409)
                return resp

            #username not already present
            else:
                query = conn.execute("insert into faculties('name') values('" + name + "')")
                user_id= conn.execute("select fac_id from faculties where name='" + name + "'").first()[0]
                out_dict = {"self": "http://192.168.53.223:8090/api/faculties/" + str(user_id),
                          "name": name,}
                resp = Response(dumps(out_dict), status=201)
                return resp
        return ""
    return ""





if __name__ == '__main__':
    app.debug = True
    app.run(port=8090, host="0.0.0.0")
