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
    def calculate(ohlc_data, short_period=12, long_period=26, signal_period=9, fill_null = False):
        indicator_macd = trend.MACD(ohlc_data['Close'], long_period, short_period, signal_period, fill_null)
        indicator_ema_short = trend.ema_indicator(ohlc_data['Close'], short_period,fill_null)
        indicator_ema_long = trend.ema_indicator(ohlc_data['Close'], long_period, fill_null)
        ohlc_data['macd'] = indicator_macd.macd()
        ohlc_data['macd_sig'] = indicator_macd.macd_signal()
        ohlc_data['macd_diff'] = indicator_macd.macd_diff()
        ohlc_data['ema_short'] = indicator_ema_short
        ohlc_data['ema_long'] = indicator_ema_long