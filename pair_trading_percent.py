import os
from time import sleep

import pandas as pd
from binance import ThreadedWebsocketManager
from binance.client import Client

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
		price['error'] = True
	

# init and start the WebSocket
bsm = ThreadedWebsocketManager()
bsm.start()
bsm.start_symbol_ticker_socket(symbol='BTCUSDT', callback=btc_pairs_trade)


## main
while len(price['BTCUSDT']) == 0:
	# wait for WebSocket to start streaming data
	sleep(0.1)
	
sleep(300)

while True:
	# error check to make sure WebSocket is working
	if price['error']:
		# stop and restart socket
		bsm.stop()
		sleep(2)
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
			except Exception as e:
				print(e)

		elif df.price.iloc[-1] > min_price * 1.05:
			try:
				order = client.futures_create_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=100)
				break
			except Exception as e:
				print(e)

	sleep(0.1)


# properly stop and terminate WebSocket
bsm.stop()
