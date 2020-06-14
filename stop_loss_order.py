import os

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)

## main

try:
	order = client.create_oco_order(
		symbol='ETHUSDT',
		side='SELL',
		quantity=100,
		price=250,
		stopPrice=150,
		stopLimitPrice=150,
		stopLimitTimeInForce='GTC')

except BinanceAPIException as e:
	# error handling goes here
	print(e)
except BinanceOrderException as e:
	# error handling goes here
	print(e)


# use exchange info to confirm order types
info = client.get_symbol_info('ETHUSDT')
print(info['orderTypes'])
