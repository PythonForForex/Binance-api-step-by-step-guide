import os
from time import sleep

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)
price = {'BTCUSDT': None, 'error':False}


def btc_pairs_trade(msg):
	''' define how to process incoming WebSocket messages '''
	if msg['e'] != 'error':
		price['BTCUSDT'] = float(msg['c'])
	else:
		price['error']:True


# init and start the WebSocket
bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_pairs_trade)
bsm.start()

## main

while not price['BTCUSDT']:
	# wait for WebSocket to start streaming data
	sleep(0.1)

while True:
	# error check to make sure WebSocket is working
	if price['error']:
		# stop and restart socket
		bsm.stop_socket(conn_key)
		bsm.start()
		price['error'] = False
	else:
		if price['BTCUSDT'] > 10000:
			try:
				order = client.order_market_buy(symbol='ETHUSDT', quantity=100)
				break
			except BinanceAPIException as e:
				# error handling goes here
				print(e)
			except BinanceOrderException as e:
				# error handling goes here
				print(e)
	sleep(0.1)


bsm.stop_socket(conn_key)
reactor.stop()
