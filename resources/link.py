from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.link import LinkItemModel
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

class CreateLinkItem(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('public_token',
      type=str,
      required=True,
      help="This field cannot be left blank."
  )
  @jwt_required()
  def post(self):
    data = CreateLinkItem.parser.parse_args()
    public_token = data['public_token']
    exchange_response = client.Item.public_token.exchange(public_token)

    model = LinkItemModel(
      item_id=exchange_response['item_id'],
      access_token=exchange_response['access_token'],
      user_id=current_identity.id
    )
    model.save_to_db()
    response = {
      'item_id': exchange_response['item_id']
    }
    return jsonify(response)