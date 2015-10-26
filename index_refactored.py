__author__ = 'Tom'
__doc__ = """ 
reads raw data, partitions by country and controls which cleaning functions are then applied
""" 

import pandas as pd
from Analysis import Manipulate_Dfs as m
from Data_Cleaning import Time_Series_Cleaning as ts
from Data_Cleaning import Main_Cleaning_Functions as clean
from Data_Cleaning import outliers_cleaning as outlier
from Data_Cleaning import Keywords_Cleaning as keyw

# Reads raw data from CSV and returns a Pandas DataFrame object
def readcsv(csvfile, encoding, index_col='country', parse_dates='created_at'):
    try:
        df = pd.read_csv(csvfile, encoding=encoding, index_col=0, parse_dates=parse_dates)
        return df.dropna()
    except OSError:
        print('file does not exist')
    except UnicodeDecodeError:
        print('encoding is the wrong codec for file')

# Takes the raw pandas data frame and creates a new dictionary of dataframes for each country.
def partition_df(df, col): # return dictionary object of filtered data frame for each unique element in col
    try:
        # dict comprehension creates dict to holds DataFrame for each country
        dict1 = {k: df[df[col] == k] for k in m.get_unique_vals(df, col)}
        return dict1
    except (TypeError):
         print(TypeError('arg1 must be a DataFrame'))
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')

# this is the main cleaning function that calls the bulk of cleaning functions on a given dataframe
def clean_frame(df):

    # remove negative nums
    df = clean.map_remove(df, 'amount_raised', clean.neg_num)
    df = clean.map_remove(df, 'amount_goal', clean.neg_num)
    df = clean.map_remove(df, 'category_id', clean.neg_num)
    df = clean.map_remove(df, 'platform_id', clean.neg_num)
    df = clean.map_remove(df, 'amount_raised', clean.neg_num)
    df = clean.map_remove(df, 'amount_goal', clean.neg_num)

    # remove outliers
    df = outlier.remove_outliers(df, 5, 'amount_goal')
    df = outlier.remove_outliers(df, 5, 'amount_raised')

    # add amount needed column to df
    df['amount_needed'] = df.amount_goal - df.amount_raised
    # add completed column
    df.completed = [df.amount_needed == 0]


    # tokenize keywords using NLTK library
    #df.description = keyw.tokenizeElements(df, 'description')

    return df

# set variables for csv read
encoding = "ISO-8859-1"
file = 'raw_data.csv'
indexCol = 'country'

# call readcsv and assign results to _raw
df_raw = readcsv(file, encoding=encoding, index_col=indexCol)


# dict comprehension creates dict to holds DataFrame for each country
dict_countries = partition_df(df_raw, 'country')

# next step is to call main cleaning function for each dataframe in the dictionary dict_countries
