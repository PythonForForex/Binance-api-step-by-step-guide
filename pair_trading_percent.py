import os
from time import sleep

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
import pandas as pd

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)
price = {'BTCUSDT': pd.DataFrame(columns=['date', 'price']), 'error':False}


def btc_pairs_trade(msg):
	''' define how to process incoming WebSocket messages '''
	if msg['e'] != 'error':
		price['BTCUSDT'].loc[len(price['BTCUSDT'])] = [pd.Timestamp.now(), float(msg['c'])]
	else:
		price['error']:True
	

# init and start the WebSocket
bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_pairs_trade)
bsm.start()

## main
while len(price['BTCUSDT']) == 0:
	# wait for WebSocket to start streaming data
	sleep(0.1)
	
sleep(300)

while True:
	# error check to make sure WebSocket is working
	if price['error']:
		# stop and restart socket
		bsm.stop_socket(conn_key)
		bsm.start()
		price['error'] = False
	else:
		df = price['BTCUSDT']
		start_time = df.date.iloc[-1] - pd.Timedelta(minutes=5)
		df = df.loc[df.date >= start_time]
		max_price = df.price.max()
		min_price = df.price.min()

		if df.price.iloc[-1] < max_price * 0.95:
			try:
				order = client.futures_create_order(symbol='ETHUSDT', side='SELL', type='MARKET', quantity=100)
				break
			except BinanceAPIException as e:
				# error handling goes here
				print(e)
			except BinanceOrderException as e:
				# error handling goes here
				print(e)

		elif df.price.iloc[-1] > min_price * 1.05:
			try:
				order = client.futures_create_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=100)
				break
			except BinanceAPIException as e:
				# error handling goes here
				print(e)
			except BinanceOrderException as e:
				# error handling goes here
				print(e)
	sleep(0.1)


# properly stop and terminate WebSocket
bsm.stop_socket(conn_key)
reactor.stop()
