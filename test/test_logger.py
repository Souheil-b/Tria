"""Test the logger module."""
import unittest
from unittest.mock import patch, MagicMock
from configparser import SectionProxy
import logging

from src.loggers import config_logging

class TestWorker(unittest.TestCase):
    """Test the logger module."""
    def test_config_logging(self):
        """Test of the config_logging function."""
        log_config = MagicMock(spec=SectionProxy)
        log_config.__getitem__.side_effect = lambda key: {
            "FILE": "test.log",
            "LEVEL": "DEBUG"
        }[key]

        with patch('logging.basicConfig') as mock_basic_config:
            config_logging(log_config)

            mock_basic_config.assert_called_once_with(
                filename="test.log",
                format="[{asctime}][{levelname}] {funcName}({filename}): {message}",
                style="{",
                level=logging.DEBUG,
                encoding="UTF-8"
            )

if __name__ == "__main__":
    unittest.main()
