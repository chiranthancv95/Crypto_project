# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
from Crypto.PublicKey import RSA
from Crypto import Random
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource

class Crypto(Resource):

    def get(self):
        random_generator = Random.new().read
        key = RSA.generate(2048, random_generator)
        pub_key = key.publickey()
        priv_export = key.exportKey('PEM').decode('ascii')
        pub_export = pub_key.exportKey('PEM').decode('ascii')
        key_dict = {"private_key": pub_export, "public_key": priv_export}
        return jsonify(key_dict)

    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': key_dict})

# adding the defined resources along with their corresponding urls
api.add_resource(Crypto, '/')

# driver function
if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80, threaded=True)
