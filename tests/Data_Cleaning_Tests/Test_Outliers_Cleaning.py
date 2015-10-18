__author__ = 'Tom'
import unittest
import pandas as pd
import numpy as np
from Data_Cleaning import outliers_cleaning as v


df=pd.DataFrame({'Data':np.random.normal(size=200)})  #example dataset of normally distributed data.


class test_num_handles_unexpected_input(unittest.TestCase):

        def test_num_raises_valueerror(self):
            self.assertRaises(TypeError, v.num('qwerty'))


class test_remove_outliers_handles_unexpected_input(unittest.TestCase):

        def test_should_raise_attributeerror_for_non_dataframe(self):
            self.assertRaises(AttributeError, v.remove_outliers('g', 3,'Data'))

        def test_should_accept_digit_string_for_arg2(self):
            self.assertEqual(v.remove_outliers(df, '4','Data').__class__.__name__, 'DataFrame')

        def test_should_accept_int_for_arg2(self):
            self.assertEqual(v.remove_outliers(df, 4,'Data').__class__.__name__, 'DataFrame')


class test_remove_outliers_handles_boolean_input(unittest.TestCase):
        def test_delete_row_containing_300(self):
            df2 = pd.DataFrame({'Data': [1, 2, 3, 4, 9, 300]})   # example dataset with one outlier
            print('hh')
            print(v.remove_outliers(df2, 3, 'Data'))
            self.assertEqual(v.remove_outliers(df2, 2, 'Data').Data.count(), 5)

