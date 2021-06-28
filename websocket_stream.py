from time import sleep

from binance import ThreadedWebsocketManager


btc_price = {'error':False}

def btc_trade_history(msg):
	''' define how to process incoming WebSocket messages '''
	if msg['e'] != 'error':
		print(msg['c'])
		
		btc_price['last'] = msg['c']
		btc_price['bid'] = msg['b']
		btc_price['last'] = msg['a']
		btc_price['error'] = False
	else:
		btc_price['error'] = True


# init and start the WebSocket
bsm = ThreadedWebsocketManager()
bsm.start()

# subscribe to a stream
bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol='BTCUSDT')

# put script to sleep to allow WebSocket to run for a while
# this is just for example purposes
sleep(2)

# add a second stream
bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol='ETHUSDT')

# put script to sleep to allow WebSocket to run for a while
# this is just for example purposes
sleep(2)

# stop websocket
bsm.stop()

sleep(2)
# display more info about the various websocket streams
help(ThreadedWebsocketManager)
