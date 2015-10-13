__author__ = 'Tom'
import numpy as np
import pandas as pd

# reads csv and excludes records that contain NaN
def readcsv(csvfile, encoding, index_col=0, parse_dates='created_at'):
    df = pd.read_csv(csvfile, index_col=index_col, encoding=encoding, parse_dates=parse_dates)
    return df.dropna()

# set project ids
entrepreneurship = '27'
construction = '28'

# df is our raw data frame taken from the csv
df = readcsv('raw_data.csv', encoding="ISO-8859-1")

# add amount needed column to df
df['amount_needed'] = df.amount_goal - df.amount_raised
df['completed'] = [x == 0 for x in df.amount_needed]

# convert to timestamp
# use cython to speed this operation up
# df.created_at = pd.to_datetime(df.created_at)


# GET AMOUNT RAISED BY PLATFORM ID

AllCat_Nepal = df[df.country == 'Nepal']
AllCat_Indonesia = df[df.country == 'Indonesia']
AllCat_Philippines = df[df.country == 'Philippines']

Total_Raised = AllCat_Nepal.amount_raised.sum() + AllCat_Indonesia.amount_raised.sum() + AllCat_Philippines.amount_raised.sum()
Total_Needed = AllCat_Nepal.amount_needed.sum() + AllCat_Indonesia.amount_needed.sum() + AllCat_Philippines.amount_needed.sum()

# entrepreneurship and construction category_ids
EntCatNeeded = df[df.category_id == entrepreneurship].amount_needed.sum()
ConstCatNeeded = df[df.category_id == construction].amount_needed.sum()
EntCatRaised = df[df.category_id == entrepreneurship].amount_raised.sum()
ConstCatRaised = df[df.category_id == construction].amount_raised.sum()

OtherCatNeeded = Total_Needed - (EntCatNeeded + ConstCatNeeded)
OtherCatRaised = Total_Raised - (EntCatRaised + ConstCatRaised)

# create series for raised
df.amountRaised = pd.Series([AllCat_Nepal.amount_raised.sum(),
                                 AllCat_Indonesia.amount_raised.sum(),
                                 AllCat_Philippines.amount_raised.sum(),
                                 Total_Raised,
                                 EntCatRaised,
                                 ConstCatRaised,
                                 OtherCatRaised],
                                 index=['Nepal_All', 'Indonesia_All', 'Philippines_All', 'Total', 'All_Entrepreneurship',
                                        'All_Construction', 'All_OtherCategories'])
# create series for needed
df.amountNeeded = pd.Series([AllCat_Nepal.amount_needed.sum(),
                                 AllCat_Indonesia.amount_needed.sum(),
                                 AllCat_Philippines.amount_needed.sum(),
                                 Total_Needed,
                                 EntCatNeeded,
                                 ConstCatNeeded,
                                 OtherCatNeeded],
                                 index=['Nepal_All', 'Indonesia_All', 'Philippines_All', 'Total', 'All_Entrepreneurship',
                                        'All_Construction', 'All_OtherCategories'])
df.created_at = pd.to_datetime(pd.Series(df.created_at))

def hoursToNanoseconds(hours):
    return hours*60*60*1000000000   # converts hours to nanoseconds

def

nano = hoursToNanoseconds(3)
df['threehour'] = pd.DatetimeIndex(((df.created_at.astype(np.int64) // nano + 1) * nano))

# create series of our DFs
SplitDataFrames = pd.Series([df[df.country == 'Nepal'], df[df.country == 'Indonesia'],
                  df[df.country == 'Philippines'],
                  df[df.category_id == entrepreneurship],
                  df[df.category_id == construction]],
                  index=['Nepal_All', 'Indonesia_All', 'Philippines_All',
                         'All_Entrepreneurship', 'All_Construction'])

# then group each df in series by threehour time frequency
h3tsDataFrames = []
[h3tsDataFrames.append(index.groupby(index.threehour).sum()) for index in SplitDataFrames]

# add cumulative sum column to number each time series data point
[h3tsDataFrames.append(index.groupby(index.threehour).sum()) for index in SplitDataFrames]


#h3TsDataFrames = [print(index.groupby(index.threehour).sum()) for index in h3TsDataFrames]

#print(h3TsDataFrames)
print(df.description)

#df.to_csv('df.csv')
#not enough data for nepal
#h3tsDataFrames[0].to_csv('h3tsNepal.csv')
#h3tsDataFrames[1].to_csv('h3tIndonesia.csv')


# time series for everything bpogus
#print(df.groupby(df.created_at).sum())
#threehourTS = (df.groupby(df.threehour).sum())
#print(threehourTS)
#print(df.columns.unique())

# CHEATSHEET
#
# df[df.c == value]
# h[(h.year < value) & (h.year>= value)]   find alll films that is true for BOTH values
# h[(h.year < 1980) | (h.year>= 1990)]   find alll films before and after dates
# t[t.title == 'Macbeth'].sort('year')    sort all films called macbeth by
# df.sort(['column1', 'column2'])
# df.groupby(df.created_at).sum())      aggregates data according to time


# 1. tokenize descriptions
# 2. create datavalidation functions that remove negative numbers and test
#2- create function for each column and test for each data validation point eg - integer - negative
