import requests
import config

api_key = config.alphavantage_api_key
api_url = 'https://www.alphavantage.co/query'


def call_daily(symbol: str, outputsize: str = 'compact'):
    # ... code to call alphavantage api
    url = api_url + '?function=TIME_SERIES_DAILY_ADJUSTED' + \
          '&symbol=' + symbol + \
          '&apikey=' + api_key + \
          '&outputsize=' + outputsize
    r = requests.get(url)
    data = r.json()

    return data


def call_news(symbol: str, limit: int = 200):
    # ... code to call alphavantage api
    url = api_url + '?function=NEWS_SENTIMENT' + \
          '&tickers=' + symbol + \
          '&apikey=' + api_key + \
          '&limit=' + limit
    r = requests.get(url)
    data = r.json()

    return data


def call_company_overview(symbol: str):
    # ... code to call alphavantage api
    url = api_url + '?function=OVERVIEW' + \
          '&symbol=' + symbol + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_income_statement(symbol: str):
    # ... code to call alphavantage api
    url = api_url + '?function=INCOME_STATEMENT' + \
          '&symbol=' + symbol + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_balance_sheet(symbol: str):
    # ... code to call alphavantage api
    url = api_url + '?function=BALANCE_SHEET' + \
          '&symbol=' + symbol + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_cash_flow(symbol: str):
    # ... code to call alphavantage api
    url = api_url + '?function=CASH_FLOW' + \
          '&symbol=' + symbol + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_earnings(symbol: str):
    # ... code to call alphavantage api
    url = api_url + '?function=EARNINGS' + \
          '&symbol=' + symbol + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data
