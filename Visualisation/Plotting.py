import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import mplfinance as mpf
import pandas as pd
import datetime


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

        #plt.xticks(rotation=45)

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
                 lower_col, upper_indicator_col, lower_indicator_col, width_col, title, include_width = False):
        df = pd.DataFrame()
        df['Close'] = dataframe[close_col]
        df['Moving Average'] = dataframe[mavg_col]
        df['Upper Band'] = dataframe[upper_col]
        df['Lower Band'] = dataframe[lower_col]
        df['Upper Indicator'] = dataframe[upper_indicator_col]
        df['Lower Indicator'] = dataframe[lower_indicator_col]
        df['Band Width'] = dataframe[width_col]
        df['Date'] = dataframe.index

        ax = df.plot(x='Date', y='Close', label='Close Price', color='blue', title=title, zorder=1)
        df.plot(ax=ax, x='Date', y='Moving Average', label='Moving Average', color='green', zorder=5)
        df.plot(ax=ax, x='Date', y='Upper Band', label='Upper Band', color='orange', zorder=10)
        df.plot(ax=ax, x='Date', y='Lower Band', label='Lower Band', color='orange', zorder=15)

        if include_width:
            df.plot(ax=ax, x='Date', y='Band Width', label='Band Width', color='purple', zorder=20)

        if 1 in set(df['Upper Indicator']):
            df.groupby('Upper Indicator').get_group(1).plot(
                ax=ax, x='Date', y='Upper Band', label='Sell Signal', color='red', kind='scatter',
                marker='v', s=50, zorder=25)
        if 1 in set(df['Lower Indicator']):
            df.groupby('Lower Indicator').get_group(1).plot(
                ax=ax, x='Date', y='Lower Band', label='Buy Signal', color='green', kind='scatter',
                marker='^', s=50, zorder=30)

        ax.fill_between(df['Date'], df['Lower Band'], df['Upper Band'], alpha=0.2, color='orange')

        plt.ylabel('Price ($)')
        plt.show()


class RSIPlot:
    def __init__(self, dataframe, close_col, rsi_col, title):
        df = pd.DataFrame()
        df['Close'] = dataframe[close_col]
        df['RSI'] = dataframe[rsi_col]
        df['Date'] = dataframe.index

        fig = plt.figure()
        left, width = 0.1, 0.8
        rect1 = [left, 0.4, width, 0.5] # left, bottom, width, height
        rect2 = [left, 0.1, width, 0.3]

        ax1 = fig.add_axes(rect1)
        ax2 = fig.add_axes(rect2, sharex=ax1)

        ax1.plot(df.Date, df.Close, color='blue')
        ax1.set_title(title)

        fillcolor='red'
        linecolor = 'orange'
        ax2.plot(df.Date, df.RSI, color=linecolor)
        ax2.axhline(70, color=fillcolor, linestyle='--')
        ax2.axhline(30, color=fillcolor, linestyle='--')
        #ax2.fill_between(df.Date, 100, 70, facecolor=fillcolor, edgecolor=fillcolor, alpha=0.2)
        #ax2.fill_between(df.Date, 0, 30, facecolor=fillcolor, edgecolor=fillcolor, alpha=0.2)
        ax2.fill_between(df.Date, df.RSI, 70, where=(df.RSI >= 70), facecolor=fillcolor, edgecolor=fillcolor, alpha=0.2)
        ax2.fill_between(df.Date, df.RSI, 30, where=(df.RSI <= 30), facecolor=fillcolor, edgecolor=fillcolor, alpha=0.2)
        ax2.set_ylim(0, 100)
        ax2.set_yticks([30, 70])
        ax2.text(0.025, 0.95, 'RSI (14)', va='top', transform=ax2.transAxes, fontsize=9)

        #ax1 = df.plot(x='Date', y='Close', label='Close Price', color='blue', title=title, zorder=1)
        #df.plot(ax=ax, x='Date', y='RSI', label='RSI', color='green', zorder=5)

        plt.show()






