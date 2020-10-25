import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import mplfinance as mpf
import pandas as pd
import datetime


class TimeSeriesPlot:
    def __init__(self):
        self.__plots_dict = {}

    def add_series(self, dataframe, time_col, y_col, label, color, kind):
        if label in self.__plots_dict:
            print(f'Error: label {label} already exists!')
            return
        self.__plots_dict[label] = (dataframe,time_col,y_col,kind,color,label)

    def draw(self, y_label, title):
        axes_set = False
        keys = list(self.__plots_dict.keys())
        if len(keys) < 1:
            print('Error: no plots found')
            return
        first_key = keys[0]
        first_plot = self.__plots_dict[first_key]
        ax = first_plot[0].plot(x=first_plot[1],
                                y=first_plot[2],
                                kind=first_plot[3],
                                color=first_plot[4],
                                title=title,
                                label=first_plot[5])
        if len(keys) > 1:
            for key in keys[1:]:
                plot = self.__plots_dict[key]
                plot[0].plot(ax=ax,
                             x=plot[1],
                             y=plot[2],
                             kind=plot[3],
                             color=plot[4],
                             label=plot[5])

        plt.xticks(rotation=45)
        plt.ylabel(y_label)
        plt.show()


class CandleStick:
    def __init__(self):
        self.__plots_dict = {}

    @staticmethod
    def draw(ohlc_data):
        mpf.plot(ohlc_data, type='candle')







