from alpaca.data import StockBarsRequest
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.timeframe import TimeFrame
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
