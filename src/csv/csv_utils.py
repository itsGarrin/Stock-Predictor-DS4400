import time

import pandas as pd

import api_calls


# Create a function to calculate the 100-day return for stocks in the list
def get_returns(symbols):
    # Create an empty DataFrame with symbol and return columns
    df = pd.DataFrame(columns=['symbol', 'stock_return_100', 'market_return_100'])

    # Find the 100-day return for the market
    market_return_100 = get_return('VTI')

    for i, symbol in enumerate(symbols):
        print(symbol)
        # Calculate the 100-day return
        stock_return_100 = get_return(symbol)

        # Add the symbol, stock return, and market return to the DataFrame using pd.concat
        df = pd.concat([df, pd.DataFrame(
            {'symbol': symbol, 'stock_return_100': stock_return_100, 'market_return_100': market_return_100},
            index=[0])], axis=0)

        # If the index is at 1200, pause for 60 seconds to avoid the API limit
        if i % 1150 == 0:
            time.sleep(60)

    return df


# Create a function to calculate the return for a stock over the last 100 days
def get_return(symbol):
    # Call the alpha vantage api to get the data
    stock_data = api_calls.call_daily(symbol)

    # Return None if there is no data or less than 100 days of data
    try:
        if len(stock_data['Time Series (Daily)']) < 100:
            return None
    except:
        return None

    # Get the adjusted closing prices
    stock_data_df = pd.DataFrame(stock_data['Time Series (Daily)']).T

    # Calculate the return from the first day to the last day
    return_100 = (float(stock_data_df['5. adjusted close'][0]) - float(stock_data_df['5. adjusted close'][-1])) / float(
        stock_data_df['5. adjusted close'][-1])

    return return_100


# Create a function to calculate the news sentiment for stocks in the list
def get_sentiment(symbols):
    # Create an empty DataFrame with symbol and sentiment columns
    df = pd.DataFrame(columns=['symbol', 'sentiment'])

    for i, symbol in enumerate(symbols):
        print(symbol)
        # Call the alpha vantage api to get the news data
        news = api_calls.call_news(symbol)

        # If there is no news data, return None
        try:
            if news['items'] == '0':
                df = pd.concat([df, pd.DataFrame({'symbol': symbol, 'sentiment': None}, index=[0])], axis=0)
                continue
        except:
            df = pd.concat([df, pd.DataFrame({'symbol': symbol, 'sentiment': None}, index=[0])], axis=0)
            continue

        # Create a Pandas DataFrame
        stock_news = pd.DataFrame(news['feed'])

        # Calculate the average sentiment
        sentiment = stock_news['overall_sentiment_score'].mean()

        # Add the symbol and sentiment to the DataFrame using pd.concat
        df = pd.concat([df, pd.DataFrame({'symbol': symbol, 'sentiment': sentiment}, index=[0])], axis=0)

        # If the index is at 1200, pause for 60 seconds to avoid the API limit
        if i % 1150 == 0:
            time.sleep(60)

    return df


# Create a function to calculate the company overview data for stocks in the list
def get_overview(symbols):
    # Create an empty DataFrame with symbol and return columns
    df = pd.DataFrame(
        columns=['symbol', 'market_cap', 'ebitda', 'pe_ratio', 'peg_ratio', 'book_value', 'dividend_per_share',
                 'dividend_yield', 'eps', 'revenue_per_share', 'profit_margin', 'operating_margin', 'return_on_assets',
                 'return_on_equity', 'revenue', 'gross_profit', 'diluted_eps', 'quarterly_earnings_growth',
                 'quarterly_revenue_growth', 'trailing_pe', 'forward_pe', 'price_to_sales_ratio', 'price_to_book_ratio',
                 'ev_to_revenue', 'ev_to_ebitda', 'beta'])

    for i, symbol in enumerate(symbols):
        print(symbol)

        # Call the alpha vantage api to get the company overview data
        overview = api_calls.call_company_overview(symbol)

        # If there is no overview data, return None
        try:
            if overview['Symbol'] == '0':
                df = pd.concat([df, pd.DataFrame(
                    {'symbol': symbol, 'market_cap': None, 'ebitda': None, 'pe_ratio': None, 'peg_ratio': None,
                     'book_value': None, 'dividend_per_share': None, 'dividend_yield': None, 'eps': None,
                     'revenue_per_share': None, 'profit_margin': None, 'operating_margin': None,
                     'return_on_assets': None, 'return_on_equity': None, 'revenue': None, 'gross_profit': None,
                     'diluted_eps': None, 'quarterly_earnings_growth': None, 'quarterly_revenue_growth': None,
                     'trailing_pe': None, 'forward_pe': None, 'price_to_sales_ratio': None, 'price_to_book_ratio': None,
                     'ev_to_revenue': None, 'ev_to_ebitda': None, 'beta': None}, index=[0])], axis=0)
                continue
        except:
            df = pd.concat([df, pd.DataFrame(
                {'symbol': symbol, 'market_cap': None, 'ebitda': None, 'pe_ratio': None, 'peg_ratio': None,
                 'book_value': None, 'dividend_per_share': None, 'dividend_yield': None, 'eps': None,
                 'revenue_per_share': None, 'profit_margin': None, 'operating_margin': None, 'return_on_assets': None,
                 'return_on_equity': None, 'revenue': None, 'gross_profit': None, 'diluted_eps': None,
                 'quarterly_earnings_growth': None, 'quarterly_revenue_growth': None, 'trailing_pe': None,
                 'forward_pe': None, 'price_to_sales_ratio': None, 'price_to_book_ratio': None, 'ev_to_revenue': None,
                 'ev_to_ebitda': None, 'beta': None}, index=[0])], axis=0)
            continue

        # Add the symbol and overview data to the DataFrame using pd.concat
        df = pd.concat([df, pd.DataFrame(
            {'symbol': symbol, 'market_cap': overview['MarketCapitalization'], 'ebitda': overview['EBITDA'],
             'pe_ratio': overview['PERatio'], 'peg_ratio': overview['PEGRatio'], 'book_value': overview['BookValue'],
             'dividend_per_share': overview['DividendPerShare'], 'dividend_yield': overview['DividendYield'],
             'eps': overview['EPS'], 'revenue_per_share': overview['RevenuePerShareTTM'],
             'profit_margin': overview['ProfitMargin'], 'operating_margin': overview['OperatingMarginTTM'],
             'return_on_assets': overview['ReturnOnAssetsTTM'], 'return_on_equity': overview['ReturnOnEquityTTM'],
             'revenue': overview['RevenueTTM'], 'gross_profit': overview['GrossProfitTTM'],
             'diluted_eps': overview['DilutedEPSTTM'],
             'quarterly_earnings_growth': overview['QuarterlyEarningsGrowthYOY'],
             'quarterly_revenue_growth': overview['QuarterlyRevenueGrowthYOY'], 'trailing_pe': overview['TrailingPE'],
             'forward_pe': overview['ForwardPE'], 'price_to_sales_ratio': overview['PriceToSalesRatioTTM'],
             'price_to_book_ratio': overview['PriceToBookRatio'], 'ev_to_revenue': overview['EVToRevenue'],
             'ev_to_ebitda': overview['EVToEBITDA'], 'beta': overview['Beta']}, index=[0])], axis=0)

        # If the index is at 1200, pause for 60 seconds to avoid the API limit
        if i % 1150 == 0:
            time.sleep(60)

    return df
