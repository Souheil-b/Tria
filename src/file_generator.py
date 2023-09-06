"""File generator module.

    Raises:
        FileExistsError: The file already exists.
        FileNotFoundError: The file does not exist.
        PermissionError: The user does not have the permission to write in the file.

    Returns:
        True: If the file has been created or written.
        False: If the file has not been created or written.
    """

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
        permissions = os.W_OK | os.R_OK
        if os.access("./", permissions):
            with open(filename, "w", encoding="UTF-8") as file:
                file.write("")
            return True
        raise PermissionError("Access denied.")
    except FileExistsError as already_exists:
        logging.error(already_exists)
        return False
    except PermissionError as access_denied:
        logging.error(access_denied)
        return False
