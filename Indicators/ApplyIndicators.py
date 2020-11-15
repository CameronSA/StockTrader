import Indicators.Volatility as volatility
import Indicators.Momentum as momentum
import Indicators.Trend as trend


def apply_indicators(ohlc_data):
    momentum.RelativeStrengthIndex.calculate(ohlc_data)
    volatility.BollingerBands.calculate(ohlc_data, 2, 20)
    trend.MACD.calculate(ohlc_data)
