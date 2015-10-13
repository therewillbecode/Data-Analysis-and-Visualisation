__author__ = 'Tom'
#import index
import pandas as pd
import random as r

# takes pandas series and cleans


def random_choice(testargs):
    return r.choice(testargs)

TestArgs = [r.randrange(-10000000, 10000000), r.random()*100, (r.random()*-100),
            'B', 'b', 'dobhnio dobgjudo', 'glrgnkrglknd\gd/rlk332fkbhj', 'UK', '$500', '-$500', 'joe\'s fast run usa']

rand_list = []
[rand_list.append(random_choice(TestArgs)) for x in range(0, 90)]

print(rand_list)
pseries = pd.Series(rand_list)
print(pseries)

# use apply function on df/series to execute the below!!!!
def remove_neg_int(series)
   # use pd.dataframe.mask to return only elements of a given type
  f=  [i* for i in series]
  print(f)


remove_neg_int(pseries)


#checkout apply map, filter and map for pandas