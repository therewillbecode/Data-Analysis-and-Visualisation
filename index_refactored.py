__author__ = 'Tom'
import pandas as pd
from Analysis import Manipulate_Dfs as m
from Data_Cleaning import Time_Series_Cleaning as ts
from Data_Cleaning import Main_Cleaning_Functions as clean
from Data_Cleaning import outliers_cleaning as outlier
from Data_Cleaning import Keywords_Cleaning as keyw


def readcsv(csvfile, encoding, index_col='country', parse_dates='created_at'):
    try:
        df = pd.read_csv(csvfile, encoding=encoding, index_col=0, parse_dates=parse_dates)
        return df.dropna()
    except OSError:
        print('file does not exist')
    except UnicodeDecodeError:
        print('encoding is the wrong codec for file')

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
    df.completed = [df_clean.amount_needed == 0]


    # tokenize keywords using NLTK library
    #df.description = keyw.tokenizeElements(df, 'description')

    return df


# set variables for csv read
encoding = "ISO-8859-1"
file = 'raw_data.csv'
indexCol = 'country'

# call readcsv and assign results to _raw
df_raw = readcsv(file, encoding=encoding, index_col=indexCol)

# add amount_needed column
#df_raw = m.add_amount_needed(df_raw, 'amount_goal', 'amount_raised')
#print(df_raw.columns)

# for performance single DataFrame assigned to each country from raw_df and cleaned concurrently
unique_countries = m.get_unique_vals(df_raw, 'country')


#print((df_raw.__class__na))
print('lets go')
print(df_raw.columns)
df_clean =  clean_frame(df_raw)