__author__ = 'Tom'
import pandas as pd
import numpy as np

def hoursToNanoseconds(h):
    return h*60*60*1000000000   # converts hours to nanoseconds


# takes a dataframe and gives it a new column with time series with intervals converted in no of hours
def convert_time_interval(dataframe, col, hours):     # series should be a string
    interval = hoursToNanoseconds(hours)
    dataframe['hour'] = pd.DatetimeIndex(((dataframe[col].astype(np.int64) // interval + 1) * interval))


def group_time_series(df, TsCol):    # TsCol is the column in df holding t values for time series
    df = df[TsCol].groupby(df[TsCol].sum())
    return df

