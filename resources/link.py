from flask import jsonify
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity
from plaid_client.client import client

class CreateLinkToken(Resource):
  @jwt_required()
  def get(self):
    response = client.LinkToken.create({
      'user': {
        'client_user_id': str(current_identity.id),
      },
      'products': ["transactions"],
      'client_name': "Banko",
      'country_codes': ['US'],
      'language': 'en',
    })
    return jsonify(response)