import plaid
from config import plaid_config

config = plaid_config['default']
client = plaid.Client(
  client_id=config['client_id'],
  secret=config['secret'],
  environment=config['environment'],
  api_version=config['api_version']
)