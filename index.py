__author__ = 'Tom'
import numpy as np
import pandas as pd
from Analysis import Manipulate_Dfs
from Data_Cleaning import Time_Series_Cleaning as ts


#1 create functions for everything here
#2 create class for each country/category - must have name and all important indexes

#3 learn about queues
# 3.1 learn about locking
#4 index should create objects consisting of cleaned data on different threads concurrently - use queue and locking

# delete and change to another file
# reads csv and excludes records that contain NaN
def readcsv(csvfile, encoding, index_col=0, parse_dates='created_at'):
    df = pd.read_csv(csvfile, index_col=index_col, encoding=encoding, parse_dates=parse_dates)
    return df.dropna()

# map project ids
entrepreneurship = '27'
construction = '28'

# call read csv function and get raw df

# add amount needed column to df
df['amount_needed'] = df.amount_goal - df.amount_raised
df['completed'] = [x == 0 for x in df.amount_needed]


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

# convert frequency using nanosecond conversion from 1 min to 3 H
df.created_at = pd.to_datetime(pd.Series(df.created_at))

# third argument sets interval span in hours for time series conversion
ts.convert_time_interval(df, 'created_at', 3)

# create series of our DFs
SplitDataFrames = pd.Series([df[df.country == 'Nepal'], df[df.country == 'Indonesia'],
                  df[df.country == 'Philippines'],
                  df[df.category_id == entrepreneurship],
                  df[df.category_id == construction]],
                  index=['Nepal_All', 'Indonesia_All', 'Philippines_All',
                         'All_Entrepreneurship', 'All_Construction'])

# then group each df in series by threehour time frequency
h3tsDataFrames = []
[h3tsDataFrames.append(index.groupby(index.hour).sum()) for index in SplitDataFrames]

# add cumulative sum column to number each time series data point
[h3tsDataFrames.append(index.groupby(index.hour).sum()) for index in SplitDataFrames]


#h3TsDataFrames = [print(index.groupby(index.threehour).sum()) for index in h3TsDataFrames]

#print(h3TsDataFrames)
#print(h3tsDataFrames[1])
print(SplitDataFrames[0])
print(df.amountNeeded)

