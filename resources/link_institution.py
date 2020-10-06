from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.link import LinkItemModel
from plaid_client.client import client

class Institution(Resource):
  @jwt_required()
  def get(self, institution_id):
    response = client.Institutions.get_by_id(
      institution_id,
      _options={
        'include_optional_metadata': True
      })
    return jsonify(response)

class LinkedInstitutions(Resource):
  @jwt_required()
  def get(self):
    items = LinkItemModel.find_by_user_id(current_identity.id)
    item_objects = [
      client.Item.get(i.access_token)['item']
      for i in items
    ]
    response = []
    for item in item_objects:
      ins_response = client.Institutions.get_by_id(
      item['institution_id'],
      _options={
        'include_optional_metadata': True
      })['institution']
      response.append({
        'item_id': item['item_id'],
        'institution_id': item['institution_id'],
        'name': ins_response['name'],
        'logo': ins_response['logo'] if 'logo' in ins_response else None,
        'primary_color': ins_response['primary_color']
      })
    return jsonify({
      'institutions': response
    })