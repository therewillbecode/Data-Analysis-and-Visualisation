__author__ = 'Tom'
__author__ = 'Tom'
import numpy as np
import pandas as pd
from Analysis import Manipulate_Dfs
from Data_Cleaning import Time_Series_Cleaning as ts


def readcsv(csvfile, encoding, index_col='country', parse_dates='created_at'):
    try:
        df = pd.read_csv(csvfile, index_col=index_col, encoding=encoding, parse_dates=parse_dates)
        return df.dropna()
    except OSError:
        print('file does not exist')
    except UnicodeDecodeError:
        print('encoding is the wrong codec for file')


# set variables for csv read
encoding = "ISO-8859-1"
file = 'raw_data.csv'
indexCol = 'country'

# call readcsv and assign results to _raw
df_raw = readcsv(file, encoding=encoding, index_col=indexCol)
print(df_raw.columns)