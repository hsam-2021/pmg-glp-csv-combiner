from unittest import TestCase
import unittest
import numpy as np
import pandas as pd
from csvCombine import (combined_csv,is_valid_file)
import csv
import os

# mock data
test_file = 'test.csv'
data = [
    ['b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6', 'Satchels', 'accessories'],
    ['c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7', 'Purses', 'Purses'],
]
dictionary1 = {
    'email_hash': ['b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6',
                   'c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7',
                   'faaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18',
                   '5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e'],
    'category': ["Satchels", "Purses", "Purses", "Wallets"],
}
df1 = pd.DataFrame(dictionary1)

dictionary2 = {
    'email_hash': ['b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6',
                   'c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7'],
    'category': ["Blouses", "Shirts"],
}
df2 = pd.DataFrame(dictionary2)

dictionary3 = {
    'email_hash': ['b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6'],
    'category': ["Kitchen Cleaner"],
}
df3 = pd.DataFrame(dictionary3)
df1.to_csv('test1.csv', index=False)
df2.to_csv('test2.csv', index=False)
df3.to_csv('test3.csv', index=False)
files = ['test1.csv', 'test2.csv', 'test3.csv']


class TestCsvCombine(TestCase):

    def test_combined_csv_happy_path(self):
        with open(test_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            writer.writerows(data)

    '''
    test for reading the lines correctly from the csv file
    '''

    def test_read_csv_lines_happy_path(self):
        with open(test_file, 'r') as csv_file:
            reader = csv.reader(csv_file, dialect='excel')
            self.assertEqual(next(reader), data[0])
            self.assertEqual(next(reader), data[1])

    '''
    test for counting the unique values in filename column which should be equal to the number of files in the folder
    '''

    def test_unique_filenames(self):
        result_df = combined_csv(files)
        self.assertEqual(result_df['filename'].nunique(), 3, "The number of unique values in filename column is equal "
                                                             "to the number of .csv files")

    # def test_csv_file_not_empty(self):
    #     with self.assertRaises(error):
    #         is_valid_file("data/")
    #
    # def test_csv_file_not_empty(self):
    #     self.assertEqual(is_valid_file("data/"), True)


if __name__ == '__main__':
    unittest.main()
