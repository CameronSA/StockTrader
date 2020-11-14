import ta
from ta import momentum

# MOMENTUM INDICATORS:
# Awesome Oscillator
# Kaufman’s Adaptive Moving Average (KAMA)
# Percentage Price Oscillator (PPO)
# Percentage Volume Oscillator (PVO)
# Rate Of Change (ROC)
# Relative Strength Index (RSI)
# Stochastic Relative Strength Index (SRSI)
# Stochastic Oscillator
# True Strength Index (TSI)
# Ultimate Oscillator
# William's %R

class RelativeStrengthIndex:
    @staticmethod
    def calculate(ohlc_data, period=14, fill_null = False):
        indicator_rsi = ta.momentum.rsi(ohlc_data['Close'], period, fill_null)
        ohlc_data['RSI'] = indicator_rsi