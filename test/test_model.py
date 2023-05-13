"""Test model.py"""

import json
import os
import tempfile

from src.predict.predict import get_folder, get_prediction

MODEL = "Models/yolov8l-seg.pt"
OUTPUT_FILE = "predictions.json"
TEST_FILE_1 = "Data/Test/cat.png"
TEST_FILE_2 = "Data/Test/zoo.jpeg"


def test_get_folder():
    """Test get_folder function"""
    expected_result = ["test_dir"]
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = os.path.join(tmpdir, "test_dir")
        os.makedirs(test_dir, exist_ok=True)
        actual_result = get_folder(test_dir)
        actual_result = [os.path.basename(p) for p in actual_result]
        assert actual_result == expected_result


def test_get_prediction():
    """Test get_prediction function"""
    get_prediction(list_folder=[TEST_FILE_1], model_file=MODEL, output_file=OUTPUT_FILE)

    assert os.path.isfile(OUTPUT_FILE)
    with open(OUTPUT_FILE, "r", encoding="UTF-8") as outfile:
        predictions = json.load(outfile)
    expected_result = [
        {
            "status": "success",
            "filename": os.getcwd() + "/Data/Test/cat.png",
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
                "filename": os.getcwd() + "/Data/Test/zoo.jpeg",
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
