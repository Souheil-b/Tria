"""Predict the class of a list of images, and return a json file with the prediction"""
import logging
import os
from sys import exit as sys_exit

from ultralytics import YOLO

from src.file_generator import create_file, write_in_file

def get_folder(top_path) -> list:
    """Get all subfolders of a folder

    Args:
        top_path (str): path of a folder

    Returns:
        list: list of subfolders
    """
    path_subdir_list = []
    if not os.path.exists(top_path):
        logging.error("Path %s does not exist", top_path)
        sys_exit(84)
    path_subdir_list.append(top_path)
    for root, folders, _ in os.walk(top_path):
        for folder_path in folders:
            path = os.path.join(root, folder_path)
            if os.path.exists(path):
                path_subdir_list.append(path)
    print(path_subdir_list)
    return path_subdir_list

def get_prediction(list_folder, model_file, output_file) -> None:
    """Get the prediction for a list of images

    Args:
        list_path (list): list of images
        model_file (str): path to the model
        output_file (str): path to the output file
    """
    if not create_file(output_file):
        sys_exit(84)
    model = YOLO(model_file)
    list_predictions = []
    print(list_folder)
    for folder in list_folder:
        # stream=True to get the prediction for each image
        # instead of trying to get all the predictions at once
        # show=False to not show the image with the prediction
        predictions = model(folder, stream=True, show=False)
        try:
            for result in predictions:
                confidence = []
                box_index = []
                for box in result.boxes:
                    confidence.append(box.conf[0].numpy().item())
                    box_index.append(int(box.cls))
                list_predictions.append(
                    {
                        "status": "success",
                        "filename": result.path,
                        "detected": {
                            # pylint: disable=E1136
                            model.names[class_name]: float(f"{round(conf, 2):.2f}")
                            # pylint: enable=E1136
                            for class_name, conf in zip(box_index, confidence)
                        },
                    }
                )
        except AttributeError as att_error:
            list_predictions.append(
                {
                    "status": "error",
                    "error_name": str(att_error.__class__.__name__),
                    "message": str(att_error),
                }
            )
    write_in_file(output_file, list_predictions)
