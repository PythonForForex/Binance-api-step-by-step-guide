import os
from time import sleep

import pandas as pd
from binance import ThreadedWebsocketManager
from binance.client import Client

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
		price['error'] = True


# init and start the WebSocket
bsm = ThreadedWebsocketManager()
bsm.start_symbol_ticker_socket(symbol='BTCUSDT', callback=btc_pairs_trade)
bsm.start()


## main
while not price['BTCUSDT']:
	# wait for WebSocket to start streaming data
	sleep(0.1)

while True:
	# error check to make sure WebSocket is working
	if price['error']:
		# stop and restart socket
		bsm.stop()
		sleep(2)
		bsm.start()
		price['error'] = False
	else:
		if price['BTCUSDT'] > 10000:
			try:
				order = client.order_market_buy(symbol='ETHUSDT', quantity=100)
				break
			except Exception as e:
				print(e)

	sleep(0.1)


bsm.stop()
