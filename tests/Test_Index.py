__author__ = 'Tom'
import unittest
import index_refactored as v

class Test_read_csv(unittest.TestCase):

    # check that functions limit arg types
    def test_CheckRaiseTypeError(self):
        with self.assertRaises(OSError):
           v.readcsv('ff.csv', "ISO-8859-1")


class Testreadcsv(unittest.TestCase):
    # check that element count for each label in parsed data frame > 1
    def test_readcsv(self):
        self.assertEqual(all(elements > 1 for elements in main.readCsv('raw_data.csv', encoding="ISO-8859-1").count()), True)



