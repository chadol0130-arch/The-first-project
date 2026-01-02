#!/usr/bin/env python3
"""Minimal RTSP + YOLOv8 demo for a first prototype.

Usage:
  python src/rtsp_yolo_demo.py --rtsp "rtsp://user:pass@ip:554/Streaming/Channels/102"

This script connects to an RTSP stream, runs YOLOv8 inference, and renders
bounding boxes for dogs/cats. It is intentionally simple so you can validate
RTSP connectivity and baseline detection before moving on to pose estimation
or behavior classification.
"""

from __future__ import annotations

import argparse
import time

import cv2
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RTSP + YOLOv8 first demo")
    parser.add_argument(
        "--rtsp",
        required=True,
        help="RTSP URL for your camera/NVR sub stream",
    )
    parser.add_argument(
        "--model",
        default="yolov8n.pt",
        help="YOLOv8 model weight file (default: yolov8n.pt)",
    )
    parser.add_argument(
        "--device",
        default="cpu",
        help="Inference device (cpu, cuda, or mps if available)",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Confidence threshold for detections",
    )
    parser.add_argument(
        "--view",
        action="store_true",
        help="Show a live window with detections",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    cap = cv2.VideoCapture(args.rtsp)
    if not cap.isOpened():
        raise RuntimeError("Failed to open RTSP stream. Check URL/network.")

    model = YOLO(args.model)
    last_log = 0.0

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                raise RuntimeError("Failed to read frame from RTSP stream.")

            results = model.predict(
                frame,
                device=args.device,
                conf=args.conf,
                verbose=False,
            )

            annotated = results[0].plot()

            now = time.time()
            if now - last_log > 2.0:
                names = results[0].names
                detected = [
                    names[int(box.cls[0])]
                    for box in results[0].boxes
                ]
                print(f"Detected: {detected}")
                last_log = now

            if args.view:
                cv2.imshow("RTSP + YOLOv8", annotated)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
