__author__ = 'Tom'
import unittest
import index as main

class TestUnique(unittest.TestCase):

    # check that functions limit arg types
    def test_CheckRaiseTypeError(self):
        with self.assertRaises(TypeError):
            main.getUniqueLabelVals(7, 'country')


class Testreadcsv(unittest.TestCase):
    # check that element count for each label in parsed data frame > 1
    def test_readcsv(self):
        self.assertEqual(all(elements > 1 for elements in main.readCsv('raw_data.csv', encoding="ISO-8859-1").count()), True)



