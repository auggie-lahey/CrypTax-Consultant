import ccxt
import time

exchange = ccxt.binance()
exchange_time = exchange.public_get_time()['serverTime']
your_time = exchange.milliseconds()

print('Exchange UTC time:', exchange_time, exchange.iso8601(exchange_time))
print('Your UTC time:', your_time, exchange.iso8601(your_time))
### this line is for syncing up linux boxes with UTC ###
!sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"

binance = ccxt.binance({'api_key': 'xxx','secret': 'xxx'})
binance.fetchBalance()

bittrex = ccxt.bittrex()
bittrex.apiKey = 'xxx'
bittrex.secret = 'xxx'
bittrex.fetch_balance()
