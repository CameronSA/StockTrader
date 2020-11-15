import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd


class TimeSeriesPlot:
    def __init__(self):
        self.__plots_dict = {}

    def add_series(self, dataframe, y_col, label, color):
        if label in self.__plots_dict:
            print(f'Error: label {label} already exists!')
            return
        self.__plots_dict[label] = (dataframe, y_col, label, color)

    def draw(self, y_label, title):
        axes_set = False
        keys = list(self.__plots_dict.keys())
        if len(keys) < 1:
            print('Error: no plots found')
            return
        first_key = keys[0]
        first_plot = self.__plots_dict[first_key]
        ax = first_plot[0][first_plot[1]].plot(label=first_plot[2], color=first_plot[3], title=title)
        if len(keys) > 1:
            for key in keys[1:]:
                plot = self.__plots_dict[key]
                plot[0][plot[1]].plot(ax=ax, label=plot[2], color=plot[3])

        plt.ylabel(y_label)
        plt.legend()
        plt.show()


class CandleStick:
    def __init__(self):
        self.__plots_dict = {}

    @staticmethod
    def draw(ohlc_data):
        mpf.plot(ohlc_data, type='candle')

class BollingerPlot:
    def __init__(self, dataframe, close_col, mavg_col, upper_col,
                 lower_col, signal_col, width_col, title):
        df = pd.DataFrame()
        df['Close'] = dataframe[close_col]
        df['Moving Average'] = dataframe[mavg_col]
        df['Upper Band'] = dataframe[upper_col]
        df['Lower Band'] = dataframe[lower_col]
        df['Signal'] = dataframe[signal_col]
        df['Band Width'] = dataframe[width_col]
        df['Date'] = dataframe.index

        fig = plt.figure()
        left, width = 0.1, 0.8
        rect1 = [left, 0.4, width, 0.5]  # left, bottom, width, height
        rect2 = [left, 0.1, width, 0.3]

        ax1 = fig.add_axes(rect1)
        ax2 = fig.add_axes(rect2, sharex=ax1)

        ax1.plot(df.Date, df.Close, label='Close Price', color='blue', zorder=1)
        df.plot(ax=ax1, x='Date', y='Moving Average', label='Moving Average', color='green', zorder=5)
        df.plot(ax=ax1, x='Date', y='Upper Band', label='Upper Band', color='orange', zorder=10)
        df.plot(ax=ax1, x='Date', y='Lower Band', label='Lower Band', color='orange', zorder=15)
        if 1 in set(df['Signal']):
            df.groupby('Signal').get_group(1).plot(
                ax=ax1, x='Date', y='Lower Band', label='Buy Signal', color='green', kind='scatter',
                marker='^', s=50, zorder=25)

        if -1 in set(df['Signal']):
            df.groupby('Signal').get_group(-1).plot(
                ax=ax1, x='Date', y='Upper Band', label='Sell Signal', color='red', kind='scatter',
                marker='v', s=50, zorder=25)

        ax1.fill_between(df['Date'], df['Lower Band'], df['Upper Band'], alpha=0.2, color='orange')
        ax1.set_ylabel('Price ($)')
        ax1.set_xlabel('')
        ax1.set_xticks([])
        ax1.set_title(title)
        ax1.legend()

        ax2.plot(df.Date, df['Band Width'], label='Band Width', color='purple')
        ax2.fill_between(df['Date'], df['Band Width'], 0, alpha=0.2, color='purple')

        ax2.set_ylabel('Band Width ($)')
        ax2.set_xlabel('')
        plt.grid()
        plt.xticks(rotation=15)
        plt.show()


class RSIPlot:
    def __init__(self, dataframe, close_col, rsi_col, signal_col, strong_signal_col, title):
        df = pd.DataFrame()
        df['Close'] = dataframe[close_col]
        df['RSI'] = dataframe[rsi_col]
        df['Signal'] = dataframe[signal_col]
        df['Strong Signal'] = dataframe[strong_signal_col]
        df['Date'] = dataframe.index

        fig = plt.figure()
        left, width = 0.1, 0.8
        rect1 = [left, 0.4, width, 0.5] # left, bottom, width, height
        rect2 = [left, 0.1, width, 0.3]

        ax1 = fig.add_axes(rect1)
        ax2 = fig.add_axes(rect2, sharex=ax1)

        ax1.plot(df.Date, df.Close, color='blue', label='Close Price')
        ax1.set_title(title)
        ax1.grid()
        ax1.legend()
        ax1.set_ylabel('Price ($)')
        ax1.set_xlabel('')
        ax1.set_xticks([])

        fillcolor = 'salmon'
        secondary_fillcolor = 'red'
        linecolor = 'orange'
        ax2.plot(df.Date, df.RSI, color=linecolor, label='RSI')

        if 1 in set(df['Signal']):
            df.groupby('Signal').get_group(1).plot(
                ax=ax2, x='Date', y='RSI', label='Buy Signal', color='green', kind='scatter',
                marker='^', s=50, zorder=25)

        if -1 in set(df['Signal']):
            df.groupby('Signal').get_group(-1).plot(
                ax=ax2, x='Date', y='RSI', label='Sell Signal', color='red', kind='scatter',
                marker='v', s=50, zorder=25)

        if 1 in set(df['Strong Signal']):
            df.groupby('Strong Signal').get_group(1).plot(
                ax=ax2, x='Date', y='RSI', label='Strong Buy Signal', color='green', kind='scatter',
                marker='^', s=100, zorder=25)

        if -1 in set(df['Strong Signal']):
            df.groupby('Strong Signal').get_group(-1).plot(
                ax=ax2, x='Date', y='RSI', label='Strong Sell Signal', color='red', kind='scatter',
                marker='v', s=100, zorder=25)

        ax2.axhline(70, color=fillcolor, linestyle='--')
        ax2.axhline(30, color=fillcolor, linestyle='--')
        ax2.axhline(80, color=secondary_fillcolor, linestyle='--')
        ax2.axhline(20, color=secondary_fillcolor, linestyle='--')
        ax2.fill_between(df.Date, df.RSI, 70, where=(df.RSI >= 70), facecolor=fillcolor, edgecolor=fillcolor, alpha=0.2)
        ax2.fill_between(df.Date, df.RSI, 30, where=(df.RSI <= 30), facecolor=fillcolor, edgecolor=fillcolor, alpha=0.2)
        ax2.set_ylim(0, 100)
        ax2.set_yticks([20, 30, 70, 80])
        ax2.grid()
        ax2.legend()
        ax2.set_ylabel('RSI')
        ax2.set_xlabel('')

        plt.xticks(rotation=15)
        plt.show()

class MACDPlot:
    def __init__(self, dataframe, close_col, macd_col, macd_ema_col, macd_diff_col, macd_sig_col,
                 ema_short_col, ema_long_col, ema_sig_col, title):
        df = pd.DataFrame()
        df['Close'] = dataframe[close_col]
        df['MACD'] = dataframe[macd_col]
        df['MACD EMA'] = dataframe[macd_ema_col]
        df['MACD Diff'] = dataframe[macd_diff_col]
        df['MACD Signal'] = dataframe[macd_sig_col]
        df['EMA Short'] = dataframe[ema_short_col]
        df['EMA Long'] = dataframe[ema_long_col]
        df['EMA Signal'] = dataframe[ema_sig_col]
        df['Date'] = dataframe.index

        fig = plt.figure()
        left, width = 0.1, 0.8
        rect1 = [left, 0.4, width, 0.5]  # left, bottom, width, height
        rect2 = [left, 0.1, width, 0.3]

        ax1 = fig.add_axes(rect1)
        ax2 = fig.add_axes(rect2, sharex=ax1)

        ax1.plot(df.Date, df.Close, color='blue', label='Close Price')
        ax1.plot(df.Date, df['EMA Short'], color='green', label='Short EMA')
        ax1.plot(df.Date, df['EMA Long'], color='red', label='Long EMA')

        if 1 in set(df['EMA Signal']):
            df.groupby('EMA Signal').get_group(1).plot(
                ax=ax1, x='Date', y='EMA Long', label='Buy Signal', color='green', kind='scatter',
                marker='^', s=50, zorder=25)

        if -1 in set(df['EMA Signal']):
            df.groupby('EMA Signal').get_group(-1).plot(
                ax=ax1, x='Date', y='EMA Long', label='Sell Signal', color='red', kind='scatter',
                marker='v', s=50, zorder=25)

        ax1.set_title(title)
        ax1.legend()
        ax1.grid()
        ax1.set_ylabel('Price ($)')
        ax1.set_xlabel('')
        ax1.set_xticks([])

        ax2.plot(df.Date, df.MACD, color='green', label='MACD')
        ax2.plot(df.Date, df['MACD EMA'], color='red', label='MACD Signal')
        ax2.plot(df.Date, df['MACD Diff'], color='blue', label='MACD Diff')

        if 1 in set(df['MACD Signal']):
            df.groupby('MACD Signal').get_group(1).plot(
                ax=ax2, x='Date', y='MACD Diff', label='Buy Signal', color='green', kind='scatter',
                marker='^', s=50, zorder=25)

        if -1 in set(df['MACD Signal']):
            df.groupby('MACD Signal').get_group(-1).plot(
                ax=ax2, x='Date', y='MACD Diff', label='Sell Signal', color='red', kind='scatter',
                marker='v', s=50, zorder=25)

        ax2.fill_between(df.Date, df['MACD Diff'], 0, facecolor='blue', edgecolor='blue', alpha=0.2)
        ax2.axhline(0, color='black', linestyle='--')
        ax2.legend()
        ax2.grid()
        ax2.set_ylabel('MACD')
        ax2.set_xlabel('')
        plt.xticks(rotation=15)
        plt.show()

class Histogram:
    def __init__(self, list, label):
        plt.hist(list, bins='rice', label=label)
        plt.legend()
        plt.show()







