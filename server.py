from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
from flask import Response

app = Flask(__name__)
api = Api(app)


class API(Resource):
    def get(self):
        resp = Response("")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

api.add_resource(API, '/api') # Route_1

if __name__ == '__main__':
     app.run(port=8090)