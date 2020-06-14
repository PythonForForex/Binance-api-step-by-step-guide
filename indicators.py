import btalib
import pandas as pd

# load DataFrame
btc_df = pd.read_csv('btc_bars3.csv', index_col=0)
# btc_df.set_index('date', inplace=True)
btc_df.index = pd.to_datetime(btc_df.index, unit='ms')

# calculate 20 moving average using Pandas
btc_df['20sma'] = btc_df.close.rolling(20).mean()
print(btc_df.tail(5))

# calculate just the last value for the 20 moving average
mean = btc_df.close.tail(20).mean()

# get the highest closing price in 2020
max_val = btc_df.close['2020'].max()

print(mean)
print(max_val)

# technical indicators using bta-lib

# sma
sma = btalib.sma(btc_df.close)
print(sma.df)

# create sma and attach as column to original df
btc_df['sma'] = btalib.sma(btc_df.close, period=20).df
print(btc_df.tail())

# calculate rsi and macd
rsi = btalib.rsi(btc_df, period=14)
macd = btalib.macd(btc_df, pfast=20, pslow=50, psignal=13)

print(rsi.df)
print(macd.df)

# access last rsi value
print(rsi.df.rsi[-1])

# join the rsi and macd calculations as columns in original df
btc_df = btc_df.join([rsi.df, macd.df])
print(btc_df.tail())
