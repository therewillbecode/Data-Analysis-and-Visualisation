__author__ = 'Tom'
#import index
import pandas as pd
import random as r

# takes pandas series and cleans


def random_choice(testargs):
    return r.choice(testargs)

TestArgs = [r.randrange(-1000000, 1000000), r.randrange(0,100000), (r.random()*-100),
            'B', 'b', 'dobhnio dobgjudo', 'glrgnkrglknd\gd/rlk332fkbhj', 'UK', '$500', '-$500', 'joe\'s fast run usa']

rand_list = []
[rand_list.append(random_choice(TestArgs)) for x in range(0, 90)]

print(rand_list)
pseries = pd.Series(rand_list)
print(pseries)

# use apply function on df/series to execute the below!!!!
def conv_neg_int_bool(x):   # only works on intergers not float/decimal
    bool = False
    if type(x) == "float":
        x = round(int(x))
    if str.isdigit(str(x)):
        bool = int(x) > 0
    return bool

h = pseries.apply(conv_neg_int_bool)
print(h)



#checkout apply map, filter and map for pandas