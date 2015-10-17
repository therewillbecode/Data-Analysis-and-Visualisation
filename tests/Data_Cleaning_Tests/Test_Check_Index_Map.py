__author__ = 'Tom'
__author__ = 'Tom'
import unittest
import pandas as pd
from cleaning import neg_num as neg
from cleaning import remove_rows_where_true_for_index as remove

x = ['4', '-3', 'phillipines', 'gf', '891555', '43.3', '0']
i = x = ['2', '2', '-1', 'gf', '-8555', '43.3', '3']
p = x = ['-1', '2', 'f', '2', '-2', '43.3', 'g']
l = x = ['2', '2', 'f', '2', '-2', '43.3', 'g']

df = pd.DataFrame([x, i, p, l], index=['x', 'i', 'p', 'l'])


class test_(unittest.TestCase):
        def test_should_remove_rows_where_function_true_for_col(self):
            self.assertEquals(len(remove(df, 0, neg)), 3)
            self.assertEquals(len(remove(df, 6, neg)), 4)
            self.assertEquals(len(remove(df, 2, neg)), 3)


class test_works_for_various_index_types(unittest.TestCase):
    print('')


class test_handles_unexpected_input(unittest.TestCase):
        def test_should_handle_empty_dataframe(self):
            print('')

        def test_raise_TypeError_for_non_dataframe(self):
           self.assertRaises(TypeError, (remove('qwerty', 3, neg)))

        def test_raise_IndexError_for_out_of_range(self):
           self.assertRaises(IndexError, (remove(df, 90, neg)))