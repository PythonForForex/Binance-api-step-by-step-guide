===============================================================
Binance Python API – A Step-by-Step Guide - AlgoTrading101 Blog
===============================================================

This is the code used in `Binance Python API – A Step-by-Step Guide <https://algotrading101.com/learn/binance-python-api/>`_ published on the Algotrading101 Blog

** The code and article were updated on June 28, 2021 to work with the latest version of Python-Binance (v0.7.10)
-----------------
Table of Contents
-----------------

* `What is the Binance API?  <https://algotrading101.com/learn/binance-python-api/#what-is-the-binance-api>`_
* `Why should I use the Binance API?  <https://algotrading101.com/learn/binance-python-api/#why-should-i-use-the-binance-api>`_
* `Why shouldn’t I use the Binance API?  <https://algotrading101.com/learn/binance-python-api/#why-should-i-not-use-the-binance-api>`_
* `What are the alternatives to using the Binance API?  <https://algotrading101.com/learn/binance-python-api/#what-are-alternatives-to-binance-api>`_
* `Are there any Python libraries available for the Binance API?  <https://algotrading101.com/learn/binance-python-api/#are-there-python-libraries-binance-api>`_
* `How do I get started with the Binance API?  <https://algotrading101.com/learn/binance-python-api/#how-do-start-with-binance-api>`_
* `Does Binance offer a demo account?  <https://algotrading101.com/learn/binance-python-api/#does-binance-offer-a-demo-account>`_
* `How do I retrieve my account balance using the Binance API?  <https://algotrading101.com/learn/binance-python-api/#how-do-i-retrieve-account-balance>`_
* `How can I retrieve the latest price for Bitcoin?  <https://algotrading101.com/learn/binance-python-api/#how-do-i-get-latest-bitcoin-price>`_
* `How can I get Bitcoin’s historical price data in CSV format?  <https://algotrading101.com/learn/binance-python-api/#how-do-i-get-bitcoin-historical-csv-data>`_
* `Should I trade futures or spot? What is the difference?  <https://algotrading101.com/learn/binance-python-api/#should-i-trade-spot-or-futures>`_
* `How to access technical indicators such as the 20 SMA?  <https://algotrading101.com/learn/binance-python-api/#technical-indicators-binance-api>`_
* `How to fire an order for Ethereum using the Binance API?  <https://algotrading101.com/learn/binance-python-api/#fire-an-ethereum-order-binance-api>`_
* `How to implement a stop loss or take profit using the Binance API?  <https://algotrading101.com/learn/binance-python-api/#implement-stop-loss-binance-api>`_
* `How to use Binance Coin (BNB) for discounted trading commissions?  <https://algotrading101.com/learn/binance-python-api/#use-bnb-for-discount-trading-fees>`_
* `How to execute a trade on ETH when BTC hits a certain price?  <https://algotrading101.com/learn/binance-python-api/#execute-eth-trade-on-bitcoin-price>`_
* `How to execute an ETH trade when BTC moves 5% in the last 5 minutes?  <https://algotrading101.com/learn/binance-python-api/#execute-eth-trade-on-btc-price-movement>`_
* `Final Thoughts  <https://algotrading101.com/learn/binance-python-api/#final-thoughts>`_

------------
Requirements
------------

* `python <https://www.python.org>`_ >= 3.4+
* `python_binance <https://github.com/sammchardy/python-binance>`_ (tested to work with >= 0.7.10 )
* `bta_lib <https://github.com/mementum/bta-lib>`_ (tested to work with >= 1.0.0 )
* `pandas <https://github.com/pandas-dev/pandas>`_ (tested to work with >= 1.0.3 )

-----------
Author Info
-----------

:author: Jignesh Davda 
:author page: https://algotrading101.com/learn/author/jdavda/
:published: 2020-06-30
