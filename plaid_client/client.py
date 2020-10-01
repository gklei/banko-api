import plaid
from config import plaid_config

config = plaid_config['default']
client = plaid.Client(**config)