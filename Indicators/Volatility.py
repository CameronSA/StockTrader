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
    def __calculate_signal(lband_indicator, hband_indicator):
        # 1, 0, -1 for buy, hold and sell respectively
        signal = []
        for lband, hband in zip(lband_indicator, hband_indicator):
            if lband > 0:
                signal.append(1)
            elif hband > 0:
                signal.append(-1)
            else:
                signal.append(0)
        return signal

    @staticmethod
    def calculate(ohlc_data, std_devs, period):
        indicator_bb = ta.volatility.BollingerBands(close=ohlc_data["Close"], n=period, ndev=std_devs)
        ohlc_data['bb_lower'] = indicator_bb.bollinger_lband()
        ohlc_data['bb_upper'] = indicator_bb.bollinger_hband()
        ohlc_data['bb_mavg'] = indicator_bb.bollinger_mavg()
        ohlc_data['bb_width'] = indicator_bb.bollinger_wband()
        ohlc_data['bb_signal'] = BollingerBands.__calculate_signal(
            indicator_bb.bollinger_lband_indicator(),
            indicator_bb.bollinger_hband_indicator())

