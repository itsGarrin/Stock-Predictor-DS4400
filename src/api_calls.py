import csv
import requests

import config

api_key = config.alphavantage_api_key
api_url = 'https://www.alphavantage.co/query'


def call_daily(symbol: str, outputsize: str = 'compact'):
    # ... code to call alphavantage api
    try:
        url = api_url + '?function=TIME_SERIES_DAILY_ADJUSTED' + \
              '&symbol=' + symbol + \
              '&apikey=' + api_key + \
              '&outputsize=' + outputsize
        r = requests.get(url)
        data = r.json()

        return data
    except:
        return None


def call_news(symbol: str, limit: int = 200):
    # ... code to call alphavantage api
    try:
        url = api_url + '?function=NEWS_SENTIMENT' + \
              '&tickers=' + symbol + \
              '&apikey=' + api_key + \
              '&limit=' + str(limit)
        r = requests.get(url)
        data = r.json()

        return data
    except:
        return None


def call_company_overview(symbol: str):
    # ... code to call alphavantage api
    try:
        url = api_url + '?function=OVERVIEW' + \
              '&symbol=' + symbol + \
              '&apikey=' + api_key
        r = requests.get(url)
        data = r.json()

        return data
    except:
        return None


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


def call_listings():
    # ... code to call alphavantage api
    url = api_url + '?function=LISTING_STATUS' + \
          '&apikey=' + api_key
    r = requests.get(url)
    decoded_content = r.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

    return my_list


def call_earnings(symbol: str):
    # ... code to call alphavantage api
    url = api_url + '?function=EARNINGS' + \
          '&symbol=' + symbol + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_simplemovingaverage(symbol: str, interval: str, time_period: int, series_type: str):
    # ... code to call alphavantage api
    url = api_url + '?function=SMA' + \
          '&symbol=' + symbol + \
          '&interval=' + interval + \
          '&time_period=' + str(time_period) + \
          '&series_type=' + series_type + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_vwap(symbol: str, interval: str):
    # ... code to call alphavantage api
    url = api_url + '?function=VWAP' + \
          '&symbol=' + symbol + \
          '&interval=' + interval + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_stoch(symbol: str, interval: str):
    # ... code to call alphavantage api
    url = api_url + '?function=STOCH' + \
          '&symbol=' + symbol + \
          '&interval=' + interval + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_rsi(symbol: str, interval: str, time_period: int, series_type: str):
    # ... code to call alphavantage api
    url = api_url + '?function=RSI' + \
          '&symbol=' + symbol + \
          '&interval=' + interval + \
          '&time_period=' + str(time_period) + \
          '&series_type=' + series_type + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data


def call_adx(symbol: str, interval: str, time_period: int):
    # ... code to call alphavantage api
    url = api_url + '?function=ADX' + \
          '&symbol=' + symbol + \
          '&interval=' + interval + \
          '&time_period=' + str(time_period) + \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()

    return data
