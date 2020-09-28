from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, current_identity, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.link import CreateLinkToken

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'banko'
api = Api(app)

@app.before_first_request
def create_tables():
  db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(CreateLinkToken, '/create_link_token')

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(port=5000, debug=True)