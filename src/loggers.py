"""Logging module

Manages the format of log messages and handles log files.
"""

import logging
from configparser import SectionProxy

log_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def config_logging(log_config: SectionProxy) -> None:
    """Sets initial configuration of the logging module.

    Args:
        log_config (SectionProxy): The "LOG" section of the 'config.ini' file.
    """
    logging.basicConfig(
        filename=log_config["FILE"],
        format="[{asctime}][{levelname}] {funcName}({filename}): {message}",
        style="{",
        level=log_level.get(log_config["LEVEL"], logging.WARNING),
        encoding="UTF-8",
    )
