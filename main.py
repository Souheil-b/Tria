#!/usr/bin/env python3
"""Main of project, call the prediction function"""
import argparse
import logging
import os
from sys import exit as sys_exit

from src.config import set_config
from src.predict.predict import get_prediction


def args_parser() -> argparse.Namespace:
    """Argument parser for the script
    Returns:
        Namespace: Arguments parser with the arguments
    """
    parser = argparse.ArgumentParser(
        description="Script for prediction using YOLOV8",
        epilog="Command example:\n\t\tpython main.py -p Data/ -m \
        yolov8l-seg.pt -o predictions.json",
    )
    parser.add_argument(
        "--path",
        "-p",
        type=str,
        default="Data/Test",
        help="Path to the folder with images default: Data/",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default="Models/yolov8l-seg.pt",
        help="Path to the model default: Models/yolov8l-seg.pt",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="predictions.json",
        help="Path to the output file default: predictions.json",
    )
    return parser.parse_args()


def folder_contains_media_files(folder_path) -> bool:
    """Check if a folder contains media files with the right extension

    Args:
        folder_path (str): path of a folder

    Returns:
        bool: True if the folder contains media files, False otherwise
    """
    image_formats = (
        "bmp",
        "dng",
        "jpeg",
        "jpg",
        "mpo",
        "png",
        "tif",
        "tiff",
        "webp",
        "pfm",
    )
    video_formats = (
        "asf",
        "avi",
        "gif",
        "m4v",
        "mkv",
        "mov",
        "mp4",
        "mpeg",
        "mpg",
        "ts",
        "wmv",
    )

    for file_name in os.listdir(folder_path):
        extension = file_name.split(".")[-1].lower()
        if extension in image_formats or extension in video_formats:
            return True
    return False


def get_subfolder_paths(dir_path) -> list:
    """Get all subfolders of a folder

    Args:
        dir_path (str): path of a folder

    Returns:
        list: list of subfolders
    """
    subfolder_paths = []
    for root, directories, _ in os.walk(dir_path):
        for folder in directories:
            subfolder_path = os.path.join(root, folder)
            if folder_contains_media_files(subfolder_path):
                subfolder_paths.append(subfolder_path)
                subfolder_paths.extend(get_subfolder_paths(subfolder_path))
    return subfolder_paths


def main() -> None:
    """Main function"""
    try:
        args = args_parser()
        set_config()
        folder = get_subfolder_paths(args.path)
        if folder_contains_media_files(args.path):
            folder.insert(0, args.path)
        print(folder)
        if isinstance(folder, list):
            get_prediction(
                list_folder=folder, model_file=args.model, output_file=args.output
            )
        elif isinstance(folder, str):
            get_prediction(
                list_folder=[folder], model_file=args.model, output_file=args.output
            )
        else:
            logging.error("Folder is not a list or a string")
            sys_exit(84)
    # pylint: disable=W0703
    except Exception as exp:
        logging.error(exp)


if __name__ == "__main__":
    main()
