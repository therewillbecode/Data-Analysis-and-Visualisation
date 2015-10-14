__author__ = 'Tom'
import unittest
import pandas as pd
import random as r
import validation as v



class test_can_handle_strings(unittest.TestCase):
        def test_should_return_true_for_negative_int(self):
            self.assertEqual(v.check_neg_num('-40'), True)

        def test_should_return_false_for_positive_int(self):
            self.assertEqual(v.check_neg_num('835'), False)

        def test_should_return_false_for_non_digit(self):
            self.assertEqual(v.check_neg_num('Britain'), False)

        def test_should_return_false_for_zero(self):
            self.assertEqual(v.check_neg_num('0'), False)

        def test_should_return_true_for_negative_float(self):
            self.assertEqual(v.check_neg_num('-10.82'), True)


class test_can_handle_boolean_input(unittest.TestCase):
        def test_can_handle_boolean_input(self):
            self.assertEqual(v.check_neg_num(True), False)


