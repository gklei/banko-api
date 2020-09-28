import importlib
import json

def import_config(name: str):
  try:
    module = importlib.import_module('config.local_{}_config'.format(name))
  except Exception:
    module = importlib.import_module('config.{}_config'.format(name))
  return getattr(module, '{}_config'.format(name))

def import_json_config(name: str):
  try:
    with open(f'local_{name}.json') as f:
      return json.load(f)
  except FileExistsError:
    with open(f'{name}.json') as f:
      return json.load(f)

plaid_config = import_config('plaid')
income_config = import_config('income')
expense_config = import_config('expense')