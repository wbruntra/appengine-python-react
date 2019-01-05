from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Status(Resource):
    def get(self):
        return {'status': 'Connected'}

api.add_resource(Status, '/api')
