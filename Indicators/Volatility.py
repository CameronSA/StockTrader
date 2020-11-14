import ta
from ta import volatility

# VOLATILITY INDICATORS:
# Bollinger Bands
# Average True Range
# Donchian Channel
# Keltner Channel
# Ulcer Index


class BollingerBands:
    @staticmethod
    def calculate(ohlc_data, std_devs, period):
        indicator_bb = ta.volatility.BollingerBands(close=ohlc_data["Close"], n=period, ndev=std_devs)
        ohlc_data['bb_lower'] = indicator_bb.bollinger_lband()
        ohlc_data['bb_upper'] = indicator_bb.bollinger_hband()
        ohlc_data['bb_lower_ind'] = indicator_bb.bollinger_lband_indicator()
        ohlc_data['bb_upper_ind'] = indicator_bb.bollinger_hband_indicator()
        ohlc_data['bb_mavg'] = indicator_bb.bollinger_mavg()
        ohlc_data['bb_width'] = indicator_bb.bollinger_wband()
