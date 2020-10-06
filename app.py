from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, current_identity, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.link_item import CreateLinkToken, CreateLinkItem, LinkItem, LinkItemList
from resources.link_account import AccountGroup, AllAccounts
from resources.link_institution import Institution, LinkedInstitutions

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
api.add_resource(CreateLinkItem, '/create_link_item')

api.add_resource(LinkItem, '/link_item/<string:item_id>', endpoint='link_item_resource')
api.add_resource(LinkItemList, '/link_items')
api.add_resource(AccountGroup, '/link_item/<string:item_id>/accounts', endpoint='link_item_accounts_resource')
api.add_resource(AllAccounts, '/all_accounts')
api.add_resource(Institution, '/institution/<string:institution_id>')
api.add_resource(LinkedInstitutions, '/linked_institutions')

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(port=5000, debug=True)