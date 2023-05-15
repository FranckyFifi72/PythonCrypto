from typing import List, Any

import pandas as pd
import numpy as np
import  CryptoAnalysis.TACrypto.constants as constants
import CryptoAnalysis.TACrypto.Binance as Binance
import datetime as dt
import CryptoAnalysis.TACrypto.utilities as ut
import time

class HistoricalData():
    symbols: list[str] = []
    symbolsUSDT: list[str] = []

    def __init__(self, symbol : str = 'BTCUSDT'):
        self.start_time : dt.datetime = None
        self.end_time : dt.datetime = None
        self.client = Binance.BinanceClient(futures=False)
        self.df : pd.DataFrame
        self.symbol = symbol
        self.interval = '1d'
        if len(HistoricalData.symbols) == 0:
            HistoricalData.symbols = self.client.get_symbols()
            HistoricalData.symbolsUSDT = filter(lambda usdt: usdt.endswith("USDT"), HistoricalData.symbols)

    def get_historical_data(self, start_time : dt.datetime, end_time : dt.datetime, limit : int=1500, interval : str = '1d'):
        collection = []

        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

        while start_time < end_time:
            data = self.client.get_historical_data(self.symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
            if not data: break
            #print(client.exchange + " " + symbol + " : Collected " + str(len(data)) + " initial data from " + str(
            #   ut.ms_to_dt_local(data[0][0])) + " to " + str(ut.ms_to_dt_local(data[-1][0])))
            start_time = int(data[-1][0] + 1000)
            collection += data
            time.sleep(1.1)

        return collection


