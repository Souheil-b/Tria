#!/usr/bin/env python3
"""File to train the model with YOLOV8"""
import argparse

from ultralytics import YOLO


def train_model(yaml_path: str) -> None:
    """Train the model with data.yaml"""
    model = YOLO("../../Models/yolov8l.pt")
    model.train(
        data=yaml_path,
        epochs=100,
        imgsz=640,
        save=True,
        name="yolo_detct_face_humain_v",
    )


if __name__ == "__main__":
    args = argparse.ArgumentParser(
        description="Train model with YOLOV8",
        epilog="Command example:\n\t\tpython train.py -d [path to data.yaml]",
    )
    args.add_argument(
        "--data", "-d", type=str, help="Path to the data.yaml file to train a new model"
    )
    args = args.parse_args()
    train_model(args.data)
