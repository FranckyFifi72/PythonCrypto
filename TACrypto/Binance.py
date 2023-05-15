from datetime import datetime
from typing import *
import time
import TACrypto.constants as constants
import TACrypto.utilities as ut

class BinanceClient:
    def __init__(self, futures=False):
        self.exchange = constants.binance_exchange_info
        self.futures = futures

        if self.futures:
            self._base_url = constants.binance_futures_api_url
        else:
            self._base_url = constants.binance_api_url

        self.symbols = self.get_symbols()

    def _make_request(self, endpoint: str, query_parameters: Dict):
        try:
            response = requests.get(self._base_url + endpoint, params=query_parameters)

        except Exception as e:
            print("Connection error while making request to %s: %s", endpoint, e)
            return None

        if response.status_code == 200:
            return response.json()
        else:
            print("Error while making request to %s: %s (status code = %s)",
                  endpoint, response.json(), response.status_code)
            return None

    def get_symbols(self) -> List[str]:

        params = dict()

        endpoint = constants.binance_futures_exchange_info if self.futures else constants.binance_exchange_info
        data = self._make_request(endpoint, params)

        symbols = [x["symbol"] for x in data["symbols"]]

        return symbols

    def get_historical_data(self, symbol: str, interval: Optional[str] = "1m", start_time: Optional[int] = None,
                            end_time: Optional[int] = None, limit: Optional[int] = 1500):

        params = dict()

        params["symbol"] = symbol
        params["interval"] = interval
        params["limit"] = limit

        if start_time is not None:
            params["startTime"] = start_time
        if end_time is not None:
            params["endTime"] = end_time

        endpoint = constants.binance_futures_klines if self.futures else constants.binance_klines
        raw_candles = self._make_request(endpoint, params)

        candles = []

        if raw_candles is not None:
            for c in raw_candles:
                candles.append((float(c[0]), float(c[1]), float(c[2]), float(c[3]), float(c[4]), float(c[5]),))
            return candles
        else:
            return None
