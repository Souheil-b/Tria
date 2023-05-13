"""Configuration module

Loads configuration parameters from the 'config.ini' file.
To use, import the module and read variable stored in the 'config' variable.
"""

from configparser import ConfigParser
from .loggers import config_logging

worker_config = ConfigParser()

def set_config() -> None:
    """Parse the config file and set configuration of the Worker modules.
    """
    worker_config.read("config.ini", "UTF-8")
    config_logging(worker_config["LOG"])
