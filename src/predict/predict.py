import json
import os

from ultralytics import YOLO

MODEL = "yolov8n-seg.pt"
PATH = "../../Data/"
OUTPUT_FILE = "predictions.json"


def get_folder(parent_path=PATH):
    path_subdir_lsit = [parent_path]
    for root, folders, _ in os.walk(parent_path):
        for folder in folders:
            path_subdir_lsit.append(os.path.join(root, folder))
    return path_subdir_lsit


def get_prediction(files=PATH):
    model = YOLO(MODEL)

    predictions = []

    for file in files:
        results = model(file, stream=True, show=False)
        try:
            for result in results:
                for box in result.boxes:
                    predictions.append(
                        {
                            "status": "success",
                            "class": model.names[int(box.cls)],
                            "confidence": box.conf[0].numpy().item(),
                            "filename": result.path,
                        }
                    )
        except AttributeError as att_error:
            predictions.append(
                {
                    "status": "error",
                    "error_name": str(att_error.__class__.__name__),
                    "message": str(att_error),
                }
            )
    with open(OUTPUT_FILE, "w", encoding="UTF-8") as pred_file:
        json.dump(predictions, pred_file, indent=4, ensure_ascii=False)


def main():
    files = get_folder()
    get_prediction(files)


if __name__ == "__main__":
    main()
