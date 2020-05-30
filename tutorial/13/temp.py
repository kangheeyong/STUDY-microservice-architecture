from pykrx import stock


tickers = stock.get_market_ticker_list()
print(tickers)

df = stock.get_market_ohlcv_by_date("20180810", "20181212", "005930")
print(df.head(3))

