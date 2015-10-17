__author__ = 'Tom'
import unittest

from cleaning import neg_num as v


class test_can_handle_strings(unittest.TestCase):
        def test_should_return_true_for_negative_int(self):
            self.assertEqual(v('-40'), True)

        def test_should_return_false_for_positive_int(self):
            self.assertEqual(v('835'), False)

        def test_should_return_false_for_non_digit(self):
            self.assertEqual(v('Britain'), False)

        def test_should_return_false_for_zero(self):
            self.assertEqual(v('0'), False)

        def test_should_return_true_for_negative_float(self):
            self.assertEqual(v('-10.82'), True)

        def test_should_return_false_for_dash_char(self):
            self.assertEqual(v('30-70.82'), False)
            self.assertEqual(v('3070.82-'), False)

        def test_should_return_false_for_misxed(self):
            self.assertEqual(v('7882Kg'), False)

class test_can_handle_numbers(unittest.TestCase):
        def test_should_return_true_for_negative_int(self):
            self.assertEqual(v(-52), True)

        def test_should_return_false_for_positive_int(self):
            self.assertEqual(v(284), False)

        def test_should_return_true_for_negative_float(self):
            self.assertEqual(v(-959.3), True)

        def test_should_return_false_for_positive_float(self):
            self.assertEqual(v(9.3), False)


class test_can_handle_boolean_input(unittest.TestCase):
        def test_can_handle_boolean_input(self):
            self.assertEqual(v(True), False)
            self.assertEqual(v(False), False)


class test_can_handle_edge_cases(unittest.TestCase):
        def test_should_handle_large_strings(self):
            self.assertEqual(v('58684676455356441442810'), False)
            self.assertEqual(v('-6868467044848428441442810'), True)
            self.assertEqual(v('8452195869558878840.6885258'), False)
            self.assertEqual(v('-541200067058280644.84887541810'), True)

        def test_should_handle_large_nums(self):
            self.assertEqual(v(58684676455356441442810), False)
            self.assertEqual(v(-6868467044848428441442810), True)
            self.assertEqual(v(8452195869558878840.6885258), False)
            self.assertEqual(v(-541200067058280644.84887541810), True)

        def test_should_handle_inputs_close_to_zero(self):
            self.assertEqual(v(0.00001), False)
            self.assertEqual(v(-0.000523), True)


class test_value_error_raised_not_passed_str_or_num(unittest.TestCase):
        def test_exception_raised(self):
            self.assertRaises(Exception, v([3, 2]))             # list
            self.assertRaises(Exception, v({'frog', 32}))       # set
            self.assertRaises(Exception, v(lambda x: x + 1))    # lambda function


