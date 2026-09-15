from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")

    model.train(
        data="C:/Users/Administrator/Downloads/Pothole-bumps/data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        workers=2,
        name="pothole_v1"
    )