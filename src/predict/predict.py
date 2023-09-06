"""Predict the class of a list of images, and return a json file with the prediction"""

import json
from sys import exit as sys_exit
# from time import sleep

from ultralytics import YOLO

from src.file_generator import create_file


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

    def add_prdiction_to_json(file, dict_predictions) -> None:
        """Add the prediction to the json file.
        args:
            file (file): json file
            dict_predictions (dict): prediction
        """
        file.seek(0)
        dict_predictions.append({
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
        json.dump(dict_predictions, file, indent=4)
        file.truncate()


    with open(output_file, 'r+', encoding='utf8') as file:
        dict_predictions = []
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
                    add_prdiction_to_json(file, dict_predictions)
            except AttributeError as att_error:
                file.seek(0)
                dict_predictions.append(
                    {
                        "status": "error",
                        "error_name": str(att_error.__class__.__name__),
                        "message": str(att_error),
                    }
                )
                json.dump(dict_predictions, file, indent=4)
                file.truncate()
