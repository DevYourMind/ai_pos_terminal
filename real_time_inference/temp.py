import cv2
import numpy as np
import matplotlib.pyplot as plt
import onnxruntime as ort
from pathlib import Path
import supervision as sv
from ultralytics import YOLO
from time import sleep

def main():
    path_models = Path('../optimization_tests/models/')
    model_terminal_od = YOLO(path_models/'model_terminal_od.pt')
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )
    cap = cv2.VideoCapture(0)
    # cap.set(3, 720)
    # cap.set(4, 720)
    while True:
        sleep(1)
        ret, frame = cap.read()
        result = model_terminal_od(frame)[0]
        detections = sv.Detections.from_ultralytics(result)
        frame = box_annotator.annotate(scene=frame, detections=detections)
        cv2.imshow('temp', frame)

if __name__ == '__main__':
    main()