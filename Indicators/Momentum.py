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
    def __calculate_signals(indicator_rsi, upper_lim, lower_lim):
        # 1, 0, -1 for buy, hold and sell respectively
        signals = []
        for item in indicator_rsi:
            if item > upper_lim:
                signals.append(-1)
            elif item < lower_lim:
                signals.append(1)
            else:
                signals.append(0)
        return signals

    @staticmethod
    def calculate(ohlc_data, period=14, fill_null = False,
                  upper_lim=70, lower_lim=30, strong_upper_lim=80, strong_lower_lim=20):
        indicator_rsi = ta.momentum.rsi(ohlc_data['Close'], period, fill_null)
        ohlc_data['rsi'] = indicator_rsi
        ohlc_data['rsi_signal'] = RelativeStrengthIndex.__calculate_signals(
            indicator_rsi, upper_lim, lower_lim)
        ohlc_data['strong_rsi_signal'] = RelativeStrengthIndex.__calculate_signals(
            indicator_rsi, strong_upper_lim, strong_lower_lim)
