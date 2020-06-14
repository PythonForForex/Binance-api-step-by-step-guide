import os

from binance.client import Client

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)

## main

# get balances for all assets & some account information
print(client.get_account())

# get balance for a specific asset only (BTC)
print(client.get_asset_balance(asset='BTC'))

# get balances for futures account
print(client.futures_account_balance())

# get balances for margin account
# will raise an exception if margin account is not activated
#print(client.get_margin_account())
