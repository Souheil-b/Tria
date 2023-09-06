"""Main of project, call the prediction function"""

import logging
from sys import exit as sys_exit

from src.config import set_config
from src.preprocessing import (
    args_parser,
    traverse_directories)

from src.predict.predict import get_prediction

def main() -> None:
    """Main function"""
    try:
        args = args_parser()
        set_config()
        folder = traverse_directories(args.path)
        if folder:
            get_prediction(
                list_folder=folder, model_file=args.model, output_file=args.output
            )
        else:
            logging.error("Folder is not a list or a string")
            sys_exit(84)
    # pylint: disable=W0703
    except Exception as exp:
        logging.error(exp)
    # pylint: enable=W0703


if __name__ == "__main__":
    main()
