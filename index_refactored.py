__author__ = 'Tom'
__author__ = 'Tom'
import numpy as np
import pandas as pd
from Analysis import Manipulate_Dfs
from Data_Cleaning import Time_Series_Cleaning as ts


def readcsv(csvfile, encoding, index_col=0, parse_dates='created_at'):
    try:
        df = pd.read_csv(csvfile, index_col=index_col, encoding=encoding, parse_dates=parse_dates)
        return df
    except OSError:
        print('file does not exist')
    except UnicodeDecodeError:
        print('encoding is the wrong codec for file')

# set variable for csv read
encoding = "ISO-8859-1"
file = 'raw_data.csv'

# call readcsv and assign results to _raw
df_raw = readcsv(file, encoding=encoding)
