import ta
from ta import trend

# TREND INDICATORS:
# Average Directional Movement Index (ADX)
# Aroon Indicator
# Commodity Channel Index (CCI)
# Detrended Price Oscillator (DPO)
# Exponentially Moving Average (EMA)
# Ichimoku Kinkō Hyō (Ichimoku)
# Know Sure Thing (KST) Oscillator
# Moving Average Convergence Divergence (MACD)
# Mass Index (MI)
# Parabolic Stop and Reverse (Parabolic SAR)
# Simple Moving Average (SMA)
# Schaff Trend Cycle (STC)
# Triple exponential average (TRIX)
# Vortex Indicator (VI)
# Weighted Moving Average (WMA)

# Note - The absolute MACD value depends on the security price, so do not use it to compare stocks. For this, use PPO
class MACD:
    @staticmethod
    def __calculate_ema_signals(ema_short, ema_long):
        ema_diff = []
        signal = []
        for short, long in zip(ema_short, ema_long):
            diff = short - long
            ema_diff.append(diff)

        for i in range(len(ema_diff)):
            # diff is short ema minus long ema.
            # A transition from positive to negative is a sell signal.
            # A transition from negative to positive is a buy signal.
            if i > 0:
                current_diff = ema_diff[i]
                prev_diff = ema_diff[i-1]
                # Sell signal
                if prev_diff > 0 > current_diff:
                    signal.append(-1)
                # Buy signal
                elif prev_diff < 0 < current_diff:
                    signal.append(1)
                else:
                    signal.append(0)
            else:
                signal.append(0)

        return signal

    @staticmethod
    def __calculate_macd_signals(macd_diff):
        signal = []
        # A transition from negative to positive is a buy signal.
        # A transition from positive to negative is a sell signal
        for i in range(len(macd_diff)):
            if i > 0:
                prev_diff = macd_diff[i-1]
                current_diff = macd_diff[i]
                # Buy signal
                if prev_diff < 0 < current_diff:
                    signal.append(1)
                elif prev_diff > 0 > current_diff:
                    signal.append(-1)
                else:
                    signal.append(0)
            else:
                signal.append(0)
        return signal

    @staticmethod
    def calculate(ohlc_data, short_period=12, long_period=26, signal_period=9, fill_null = False):
        indicator_macd = trend.MACD(ohlc_data['Close'], long_period, short_period, signal_period, fill_null)
        indicator_ema_short = trend.ema_indicator(ohlc_data['Close'], short_period,fill_null)
        indicator_ema_long = trend.ema_indicator(ohlc_data['Close'], long_period, fill_null)
        ohlc_data['macd'] = indicator_macd.macd()
        ohlc_data['macd_ema'] = indicator_macd.macd_signal()
        ohlc_data['macd_diff'] = indicator_macd.macd_diff()
        ohlc_data['ema_short'] = indicator_ema_short
        ohlc_data['ema_long'] = indicator_ema_long
        ohlc_data['macd_signal'] = MACD.__calculate_macd_signals(indicator_macd.macd_diff())
        ohlc_data['ema_signal'] = MACD.__calculate_ema_signals(indicator_ema_short, indicator_ema_long)
