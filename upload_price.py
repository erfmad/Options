import alpaca_trade_api as tradeapi
import config 
from alpaca_trade_api.rest import TimeFrame

api = tradeapi.REST(config.API_KEY_ID,config.SECRET_KEY,base_url=config.API_URL)

barsets = api.get_bars(['AAPL','MSFT'],TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df
print(barsets)


# loop over the keys in the barsets dictionary

#for symbol in barsets:
#    print(f"Processing Symbol {symbol}")
#
#    # loop through each bar for the current symbol in the dictionary
#
#    for bar in barsets[symbol]:
#        print(bar.t,bar.o,bar.h,bar.l,bar.c,bar.v)










#from alpaca_trade_api.rest import REST, TimeFrame
#api = REST()
#api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df
#

