from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.link import LinkItemModel
from plaid_client.client import client

class AccountGroup(Resource):
  @jwt_required()
  def get(self, item_id):
    item = LinkItemModel.find_by_item_id(item_id)
    if item is None:
      return {'message': 'Item not found'}, 404
    
    if item.user_id != current_identity.id:
      return {'message': 'You cannot access this item'}, 400
    
    response = client.Accounts.get(item.access_token)
    return jsonify(response)

class AllAccounts(Resource):
  @jwt_required()
  def get(self):
    items = LinkItemModel.find_by_user_id(current_identity.id)
    response = {
      'accounts': [
        client.Accounts.get(i.access_token)
        for i in items
      ]
    }
    return jsonify(response)
