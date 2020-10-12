from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.link import LinkItemModel
from plaid_client.client import client

class ItemAccounts(Resource):
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
    item_objects = [
      client.Item.get(i.access_token)['item']
      for i in items
    ]

    accounts = []
    for index, item in enumerate(item_objects):
      ins_response = client.Institutions.get_by_id(
        institution_id=item['institution_id'],
        _options={
          'include_optional_metadata': True
        }
      )['institution']

      account_response = client.Accounts.get(items[index].access_token)
      account_response['institution_info'] = {
        'name': ins_response['name'],
        'logo': ins_response['logo']
      } 
      accounts.append(account_response)

    return jsonify({'accounts': accounts})
