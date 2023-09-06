"""Preprocessing module for the project"""
import argparse
import os
import logging


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
        help="Path to the folder with images default: Data/Test",
        nargs="+",
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

def traverse_directories(paths):
    """Traverse directories to get all subfolders containing media files
    Args:
        paths (str or list): path of a folder or list of paths
    Returns:
        list: list of subfolders containing media files
    """

    if paths is None:
        logging.error("No path provided")
        return None

    directories = []
    def recursive_traverse(current_paths):
        nonlocal directories
        for path in current_paths:
            if os.path.isdir(path):
                if folder_contains_media_files(path):
                    directories.append(path)
                recursive_traverse([os.path.join(path, name) for name in os.listdir(path)])
    if isinstance(paths, str):
        recursive_traverse([paths])
    else:
        recursive_traverse(paths)
    directories = list(set(directories))
    directories.sort()
    return directories

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
        continue
    return False
