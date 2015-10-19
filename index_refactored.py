__author__ = 'Tom'
__author__ = 'Tom'
import pandas as pd
from Analysis import Manipulate_Dfs as m
from Data_Cleaning import Time_Series_Cleaning as ts


def readcsv(csvfile, encoding, index_col='country', parse_dates='created_at'):
    try:
        df = pd.read_csv(csvfile, encoding=encoding, index_col=0, parse_dates=parse_dates)
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

# add amount_needed column
df_raw = m.add_amount_needed(df_raw, 'amount_goal', 'amount_raised')
print(df_raw.columns)

# for performance dataframe is made for each country from raw_df and cleaned on different threads concurrently
unq = m.get_unique_vals(df_raw, 'country')
print(unq)