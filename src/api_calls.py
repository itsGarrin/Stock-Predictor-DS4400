import requests
import config

api_key = config.alphavantage_api_key
api_url = 'https://www.alphavantage.co/query'


def call_alpha_vantage_daily(symbol: str):
    # ... code to call alphavantage api
    url = api_url + '?function=TIME_SERIES_DAILY_ADJUSTED' + \
          '&symbol=' + symbol + \
          '&apikey=' + api_key + \
          '&outputsize=compact'
    r = requests.get(url)
    data = r.json()

    return data


def call_alpha_vantage_news(symbol: str):
    # ... code to call alphavantage api
    url = api_url + '?function=NEWS_SENTIMENT' + \
          '&tickers=' + symbol + \
          '&apikey=' + api_key + \
          '&limit=200'
    r = requests.get(url)
    data = r.json()

    return data
