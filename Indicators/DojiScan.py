import pandas as pd

class DojiScan:
    def __new__(cls, ohlc_data):
        __doji_data = pd.DataFrame()
        __doji_data['Doji'] = ohlc_data['Close'] - ohlc_data['Open']
        __doji_data['Date'] = __doji_data.index
        return __doji_data