from ultralytics import YOLO
# from ultralytics.nn.autoshape import 
import json
from time import sleep
model = YOLO("yolov8n-seg.pt")

files = ["../../Data/", "../../Data/null", "../../Data/mouton.HEIC"]

predictions = []
for file in files:

    results = model(file, stream=True, show=True)

    try:
        for result in results:
            for box in result.boxes:
                predictions.append({
                    "status": "success",
                    "class": model.names[int(box.cls)],
                    "confidence": box.conf[0].numpy().item(),
                    "filename": "waiting for response",
                })
        sleep(100)
    except Exception as e:
        predictions.append({
            "status": "error",
            "error_name": str(e.__class__.__name__),
            "message": str(e),
        })
        

print(json.dumps(predictions))