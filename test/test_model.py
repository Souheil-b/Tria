"""Test model.py"""

import json
import os

from src.predict.predict import get_prediction

MODEL = "Models/yolov8l-seg.pt"
OUTPUT_FILE = "predictions.json"
TEST_FILE_1 = "Data/Test/cat.png"
TEST_FILE_2 = "Data/Test/zoo.jpeg"



def test_get_prediction():
    """Test get_prediction function"""
    get_prediction(list_folder=[TEST_FILE_1], model_file=MODEL, output_file=OUTPUT_FILE)

    assert os.path.isfile(OUTPUT_FILE)
    with open(OUTPUT_FILE, "r", encoding="UTF-8") as outfile:
        predictions = json.load(outfile)
    expected_result = [
        {
            "status": "success",
            "filename": os.path.join(os.getcwd(), "Data/Test/cat.png"),
            "detected": {"cat": 0.96},
        }
    ]
    assert predictions == expected_result
    os.remove(OUTPUT_FILE)


def test_get_prediction_list():
    """Test get_prediction function"""
    get_prediction(list_folder=[TEST_FILE_2], model_file=MODEL, output_file=OUTPUT_FILE)

    assert os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, "r", encoding="UTF-8") as outfile:
        prediction = json.load(outfile)
        expected_result = [
            {
                "status": "success",
                "filename": os.path.join(os.getcwd(), "Data/Test/zoo.jpeg"),
                "detected": {
                    "elephant": 0.96,
                    "zebra": 0.92,
                    "bird": 0.89,
                    "giraffe": 0.87,
                    "sheep": 0.53,
                },
            }
        ]

        os.remove(OUTPUT_FILE)

        assert prediction == expected_result
