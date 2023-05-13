"""File generator module.

    Raises:
        FileExistsError: The file already exists.
        FileNotFoundError: The file does not exist.
        PermissionError: The user does not have the permission to write in the file.

    Returns:
        True: If the file has been created or written.
        False: If the file has not been created or written.
    """

import json
import logging
import os


def create_file(filename) -> bool:
    """File creation function.

    Args:
        filename (str): Path to the file to create.

    Raises:
        FileExistsError: If the file already exists.

    Returns:
        True: If the file has been created.
        False: If the file has not been created.
    """
    try:
        if os.path.exists(filename):
            raise FileExistsError(f"File {filename} already exists.")
        with open(filename, "w", encoding="UTF-8") as file:
            file.write("")
        return True
    except FileExistsError:
        logging.error("File %s already exists.", filename)
        return False


def write_in_file(filename, json_list) -> bool:
    """Write in a file.

    Args:
        filename (str): Path to the file to write in.
        text (str): Text to write in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user does not have the permission to write in the file.

    Returns:
        True: If the file has been written.
        False: If the file has not been written.
    """
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} does not exist.")
        if not os.access(filename, os.W_OK):
            raise PermissionError("Access denied.")
        with open(filename, "w", encoding="UTF-8") as pred_file:
            json.dump(json_list, pred_file, indent=4, ensure_ascii=False)
        return True
    except FileNotFoundError:
        logging.error("File %s not found", filename)
        return False
    except PermissionError:
        logging.error("Access denied to file %s", filename)
        return False
