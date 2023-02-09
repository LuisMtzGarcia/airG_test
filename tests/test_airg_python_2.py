import csv
import os
import unittest

from airg_python_2 import generate_csv

class TestRandomData(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file"
        self.total_rows = 100_000
        self.chunk_size = 5_000

    def tearDown(self):
        filename = self.filename + ".csv"
        if os.path.isfile(filename):
            os.remove(filename)
    
    def test_file_created_correct_name(self):
        """Tests if the file was created and named correctly."""

        generate_csv(self.filename, self.total_rows, self.chunk_size)

        expected_filename = self.filename + '.csv'
        
        self.assertTrue(os.path.isfile(expected_filename))

    def test_number_of_rows(self):
        """Tests if the correct number of rows have been generated."""

        generate_csv(self.filename, self.total_rows, self.chunk_size)

        with open(self.filename + ".csv", "r") as file:
            reader = csv.reader(file)
            num_rows = 0
            for row in reader:
                num_rows += 1

        self.assertEqual(num_rows, self.total_rows)

    def test_rows_have_correct_data(self):
        """Tests if the rows in the file contain the correct data."""

        generate_csv(self.filename, self.total_rows, self.chunk_size)

        with open(self.filename + ".csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.assertIsInstance(int(row[0]), int)
                self.assertIsInstance(row[1], str)

