""" Unit tests for preprocessing.py """
import unittest
import argparse
import os
import tempfile
from pathlib import Path
from unittest.mock import patch
from src.preprocessing import (
    args_parser,
    traverse_directories,
    folder_contains_media_files
)

class TestArgsParser(unittest.TestCase):
    """ Class Test for args_parser function"""
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        path=['Data/Test'],
        model='Models/yolov8l-seg.pt',
        output='predictions.json'
    ))
    def test_args_parser(self, mock_parse_args):
        """ Test args_parser function

        Args:
            mock_parse_args (MagicMock): Mock of argparse.ArgumentParser.parse_args
        """
        args = args_parser()
        mock_parse_args.assert_called_once()

        self.assertIsInstance(args, argparse.Namespace)
        self.assertEqual(args.path, ['Data/Test'])
        self.assertEqual(args.model, 'Models/yolov8l-seg.pt')
        self.assertEqual(args.output, 'predictions.json')



class TestYourModule(unittest.TestCase):
    """ Class Test for traverse_directories and folder_contains_media_files functions"""
    def test_traverse_directories(self):
        """ Test traverse_directories function"""
        with tempfile.TemporaryDirectory() as temp_dir:
            dir1 = os.path.join(temp_dir, 'dir1')
            dir2 = os.path.join(temp_dir, 'dir2')
            subdir1 = os.path.join(dir1, 'subdir1')
            subdir2 = os.path.join(dir2, 'subdir2')
            dir3 = os.path.join(temp_dir, 'dir3')

            file1 = os.path.join(dir1, 'file1.png')
            file2 = os.path.join(dir2, 'file2.jpeg')
            file3 = os.path.join(subdir1, 'file3.txt')
            file4 = os.path.join(subdir2, 'file4.webp')
            file5 = os.path.join(dir3, 'file5.txt')

            os.makedirs(dir1)
            os.makedirs(dir2)
            os.makedirs(subdir1)
            os.makedirs(subdir2)
            os.makedirs(dir3)

            Path(file1).touch()
            Path(file2).touch()
            Path(file3).touch()
            Path(file4).touch()
            Path(file5).touch()

            expected_directories = [dir1, dir2, subdir2]

            directories = traverse_directories([temp_dir])

            self.assertListEqual(sorted(directories), sorted(expected_directories))

    def test_folder_contains_media_files(self):
        """ Test folder_contains_media_files function"""
        with tempfile.TemporaryDirectory() as temp_dir:
            Path(os.path.join(temp_dir, 'file1.jpg')).touch()
            Path(os.path.join(temp_dir, 'file2.mp4')).touch()
            Path(os.path.join(temp_dir, 'file3.webp')).touch()
            self.assertTrue(folder_contains_media_files(temp_dir))

        with tempfile.TemporaryDirectory() as temp_dir:
            Path(os.path.join(temp_dir, 'file4.txt')).touch()
            Path(os.path.join(temp_dir, 'file5.docx')).touch()
            Path(os.path.join(temp_dir, 'file6.xlsx')).touch()
            self.assertFalse(folder_contains_media_files(temp_dir))

        with tempfile.TemporaryDirectory() as temp_dir:
            Path(os.path.join(temp_dir, 'file7.txt')).touch()
            Path(os.path.join(temp_dir, 'file8.jpeg')).touch()
            Path(os.path.join(temp_dir, 'file9.png')).touch()
            self.assertTrue(folder_contains_media_files(temp_dir))



if __name__ == "__main__":
    unittest.main()
