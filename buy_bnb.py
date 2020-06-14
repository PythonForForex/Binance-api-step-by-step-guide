import os

from binance.client import Client

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)


# functions

def topup_bnb(min_balance: float, topup: float):
	''' Top up BNB balance if it drops below minimum specified balance '''
	bnb_balance = client.get_asset_balance(asset='BNB')
	bnb_balance = float(bnb_balance['free'])
	if bnb_balance < min_balance:
		qty = round(topup - bnb_balance, 5)
		print(qty)
		order = client.order_market_buy(symbol='BNBUSDT', quantity=qty)
		return order
	return False


# example
min_balance = 1.0
topup = 2.5
order = topup_bnb(min_balance, topup)
