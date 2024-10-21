import sys
import os
import unittest
import shutil
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from file_reader_task import txt_file_reader

class TestTxtFileReader(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = 'test_files'
        os.makedirs(self.test_dir, exist_ok=True)
        # Redirect stdout to capture the output
        self.capturedOutput = StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        # Remove the temporary directory after testing
        shutil.rmtree(self.test_dir)
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_txt_file_reader_with_matching_pattern(self):
        # Create a test .txt file with a matching pattern
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as file:
            file.write('This is a test line with the pattern.\n')

        # Call the txt_file_reader function with a matching regex pattern
        txt_file_reader(self.test_dir, r'pattern')

        # Check if the expected output is printed
        self.assertEqual(
            'test_file.txt:1\n',
            self.capturedOutput.getvalue(),
            'Expected output does not match'
        )

    def test_txt_file_reader_with_non_matching_pattern(self):
        # Create a test .txt file with a non-matching pattern
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as file:
            file.write('This is a test line without the pattern.\n')

        # Call the txt_file_reader function with a non-matching regex pattern
        txt_file_reader(self.test_dir, r'non_matching_pattern')

        # Check if no output is printed
        self.assertEqual(
            '',
            self.capturedOutput.getvalue(),
            'Unexpected output was printed'
        )

    def test_txt_file_reader_with_multiple_matching_lines(self):
        # Create a test .txt file with multiple matching lines
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as file:
            file.write('This is a test line with the pattern.\n')
            file.write('This is another test line with the pattern.\n')

        # Call the txt_file_reader function with a matching regex pattern
        txt_file_reader(self.test_dir, r'pattern')

        # Check if the expected output is printed
        self.assertEqual(
            'test_file.txt:1\n',
            self.capturedOutput.getvalue(),
            'Expected output does not match'
        )

    def test_txt_file_reader_with_no_txt_files(self):
        # Call the txt_file_reader function with a directory containing no .txt files
        txt_file_reader(self.test_dir, r'pattern')

        # Check if no output is printed
        self.assertEqual(
            '',
            self.capturedOutput.getvalue(),
            'Unexpected output was printed'
        )

if __name__ == '__main__':
    unittest.main()
