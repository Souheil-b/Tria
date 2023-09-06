# IA

This is a project for making predictions on images using YOLOv8.

## Usage

To use this script, run the main.py file with the following arguments:
main.py [-h] [--path PATH] [--model MODEL] [--output OUTPUT]

| Option | Description | Default Value |
|--------|-------------|---------------|
| -h, --help | Show this help message and exit |  |
| --path PATH, -p PATH | Path to the folder with images | Data/Test |
| --model MODEL, -m MODEL | Path to the model | Models/yolov8n-seg.pt |
| --output OUTPUT, -o OUTPUT | Path to the output file | predictions.json |

## Project structure

The project contains the following directories and files:

* `Data/`: contains the dataset of images to predict on.
* `src/`: contains the processing code for making predictions.
* `Models/`: contains the trained models for making predictions.
* `main.py`: the main script for running the prediction.
* `requirements.txt`: the list of required packages to run the project.
* `dev-requirements.txt`: the list of required packages for development.

## Prediction results

After running the main.py script, a file named predictions.json will be created in the project directory. The file will contain the prediction results in the following format:

```json
[
    {
        "status": "success",
        "filename": "/path/to/image.jpg",
        "detected": {
            "banana": 0.81
        }
    },
    {
        "status": "success",
        "filename": "/path/to/another_image.jpg",
        "detected": {
            "hot dog": 0.83,
            "bottle": 0.4,
            "bowl": 0.62,
            "cup": 0.5,
            "dining table": 0.27
        }
    }
]
```
