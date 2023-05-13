"""Test the file generator module."""
import json
import os
import unittest
from unittest.mock import patch

from src.file_generator import create_file, write_in_file


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
        # Test that a new file can be created successfully
        self.assertTrue(create_file(self.filename))
        self.assertTrue(os.path.exists(self.filename))

        # Test that an existing file cannot be created again
        self.assertFalse(create_file(self.filename))

    def test_write_in_file(self):
        """Test of the write_in_file function."""
        # Test that writing to an existing file succeeds
        json_list = [
            {
                "status": "success",
                "class": ["person", "wine glass"],
                "confidence": [0.96, 0.49],
                "filename": "test_image.jpg",
            },
            {
                "status": "success",
                "class": ["cat"],
                "confidence": [0.96],
                "filename": "test_image2.jpg",
            },
        ]
        with open(self.filename, "w", encoding="UTF-8") as file:
            json.dump(json_list, file, indent=4, ensure_ascii=False)
        self.assertTrue(write_in_file(self.filename, json_list))
        with open(self.filename, "r", encoding="UTF-8") as file:
            contents = file.read()
        self.assertEqual(json.loads(contents), json_list)

        # Test that writing to a nonexistent file fails
        self.assertFalse(write_in_file("nonexistent.json", json_list))

        # Test that writing to a read-only file fails
        with patch("os.access", return_value=False):
            self.assertFalse(write_in_file(self.filename, json_list))

        # Test that writing to a file with insufficient permissions fails
        with patch("os.access", return_value=False):
            self.assertFalse(write_in_file(self.filename, json_list))


if __name__ == "__main__":
    unittest.main()
