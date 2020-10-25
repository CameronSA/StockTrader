import pandas as pd


def to_ohlc(dataframe, open_col, high_col, low_col, close_col, timestamp_col):
    __reformatted_data = dict()
    __reformatted_data['Date'] = dataframe[timestamp_col]
    __reformatted_data['Open'] = dataframe[open_col]
    __reformatted_data['High'] = dataframe[high_col]
    __reformatted_data['Low'] = dataframe[low_col]
    __reformatted_data['Close'] = dataframe[close_col]
    __df = pd.DataFrame.from_dict(__reformatted_data)
    __df.set_index('Date', inplace=True)
    return __df
