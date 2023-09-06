"""Test the file generator module."""
import os
import unittest

from src.file_generator import create_file


class TestFileGenerator(unittest.TestCase):
    """Test the file generator module."""

    def setUp(self):
        self.filename = "test_file.json"

    def tearDown(self):
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass

    def test_create_file(self):
        """Test of the create_file function."""
        self.assertTrue(create_file(self.filename))
        self.assertTrue(os.path.exists(self.filename))

        self.assertFalse(create_file(self.filename))


if __name__ == "__main__":
    unittest.main()
