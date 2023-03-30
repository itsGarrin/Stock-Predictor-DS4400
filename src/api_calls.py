import requests
from alpaca.data import StockBarsRequest
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.timeframe import TimeFrame
from newsapi import NewsApiClient
import config


def call_alpaca(symbols: [], timeframe: TimeFrame, start: str, end: str):
    # ... code to call alpaca api
    api_key = config.alpaca_api_key
    secret_key = config.alpaca_secret_key

    api = StockHistoricalDataClient(api_key, secret_key)
    request_params = StockBarsRequest(
        symbol_or_symbols=symbols,
        timeframe=timeframe,
        start=start,
        end=end
    )
    call = StockHistoricalDataClient.get_stock_bars(api, request_params)
    return call


def call_alpha_vantage_news(symbol: str):
    # ... code to call alphavantage api
    api_key = config.alphavantage_api_key
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT' + \
          '&tickers=' + symbol + \
          '&apikey=' + api_key + \
          '&limit=200'
    r = requests.get(url)
    data = r.json()

    return data


def call_newsapi(symbol: str, start: str, end: str):
    # ... code to call newsapi api
    api_key = config.newsapi_api_key
    api = NewsApiClient(api_key=api_key)
    call = api.get_everything(q=symbol, from_param=start, to=end, language='en', sort_by='relevancy')
    return call
