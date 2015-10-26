__author__ = 'Tom'
__doc__ = """ Functions to carry out simple data cleaning tasks on pandas data frames"
""" 
import pandas as pd

# data cleaning functions
x = ['4', '-3', 'phillipines', 'gf', '891555', '43.3', '0']
i = x = ['2', '2', '-1', 'gf', '-8555', '43.3', '3']
p = x = ['-1', '2', 'f', '2', '-2', '43.3', 'g']
l = x = ['2', '2', 'f', '2', '-2', '43.3', 'g']

df = pd.DataFrame([x, i, p, l], index=['x', 'i', 'p', 'l'])

# for list checks if when x is stripped of minus symbol == a digit, returns True is x is stripped and true
def neg_num(x):
    if x == True:   # prevents bug whereby function evaluates Truthy argument as negative number
        return False
    x = str(x)
    minus = False
    try:
        stripped = x.strip('-')
        stripped = round(float(stripped))
        if str.isdigit(str(stripped)) == True:
           minus = '-' in x
        return minus
    except (ValueError, TypeError):
        return False


def map_remove(dataframe, col, function):   # col must be integer
     try:
        print(dataframe)
        dataframe.mapped_series = dataframe[col].apply(function)
        print('/n')
        print(dataframe)
        return dataframe[dataframe.mapped_series == False]
     except (AttributeError, TypeError):
        print('arg1 needs to be a Dataframe')
     except (IndexError, ValueError):
        print('no such col in DataFrame')
     except KeyError as e:
        cause = e.args[0]
        print(' not a valid column in the dataframe')
        print(cause)

print('______________________')
