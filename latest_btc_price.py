import os

from binance.client import Client

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)

## main

# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol='BTCUSDT')
# print full output (dictionary)
print(btc_price)
# print just the price
print(btc_price['price'])
