__author__ = 'Tom'
__author__ = 'Tom'
import unittest

import pandas as pd

from Data_Cleaning import Main_Cleaning_Functions as m

x = ['4', '-3', 'phillipines', 'gf', '891555', '43.3', '0']
i = x = ['2', '2', '-1', 'gf', '-8555', '43.3', '3']
p = x = ['-1', '2', 'f', '2', '-2', '43.3', 'g']
l = x = ['2', '2', 'f', '2', '-2', '43.3', 'g']

df = pd.DataFrame([x, i, p, l], index=['x', 'i', 'p', 'l'])


# mock data frame for tests
df2 = pd.DataFrame({
                   'country': ['UK', 'FRA', 'UK', 'DE', 'BRA', 'KE'],
                   'pop': [0, 1, 0, 1, 1, 1],
                   'goal': [2, 4, 6, 2, 5, 7],
                   'raised': [0, 2, 1, 4, 5, 7],
                  })


class test_(unittest.TestCase):
        def test_should_remove_rows_where_function_true_for_col(self):
            self.assertEquals(len(m.map_remove(df, 0, m.neg_num)), 3)
            self.assertEquals(len(m.map_remove(df, 6, m.neg_num)), 4)
            self.assertEquals(len(m.map_remove(df, 2, m.neg_num)), 3)

class test_handles_unexpected_input(unittest.TestCase):
        def test_raise_TypeError_for_non_dataframe_arg1(self):
            self.assertRaises(TypeError, (m.map_remove('qwerty', 3, m.neg_num)))

        def test_raise_TypeError_for_non__arg2(self):
            self.assertRaises(TypeError, (m.map_remove(df, [2, 2], m.neg_num)))

        def test_raise_IndexError_for_out_of_range(self):
            self.assertRaises(IndexError, (m.map_remove(df, 90, m.neg_num)))


class test_str_for_col_arg(unittest.TestCase):
        def test_returns_dataframe_arg1(self):
            t = (m.map_remove(df2, 'goal', m.neg_num))
            self.assertEquals(t.__class__.__name__, 'DataFrame')
