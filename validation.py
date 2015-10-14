__author__ = 'Tom'
# import index
import pandas as pd
import random as r


# takes pandas series and cleans


def random_choice(testargs):
    return r.choice(testargs)


TestArgs = [r.randrange(-1000000, 1000000), r.randrange(0, 100000), (r.random() * -100),
            'B', 'b', 'dobhnio dobgjudo', 'glrgnkrglknd\gd/rlk332fkbhj', 'UK', '$500', '-$500', 'joe\'s fast run usa']

rand_list = []
[rand_list.append(random_choice(TestArgs)) for x in range(0, 90)]

print(rand_list)
pseries = pd.Series(rand_list)
print(pseries)


# for list checks if when x is stripped of minus symbol == a digit, returns True is x is stripped and true
def check_neg_num(x):
    if x == True:   # prevents bug whereby function evaluates Truthy argument as negative number
        return False
    x = str(x)
    minus = False
    stripped = x.strip('-')
    if type(stripped) == "float":
        stripped = round(int(stripped))
    if str.isdigit(str(stripped)) == True:
        minus = '-' in x
    return minus


# h = pseries.apply(conv_neg_int_bool)


x = ['4', '-3', 'phillipines', 'gf', '891555', '43.3', '0']

print([check_neg_num(i) for i in x])
# checkout apply map, filter and map for pandas
