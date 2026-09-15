from ultralytics import YOLO

if __name__ == "__main__":
    # 加载训练好的模型（注意用 best.pt，不是 yolov8n.pt）
    model = YOLO("C:/Users/Administrator/Downloads/Pothole-bumps/runs/detect/pothole_v1-4/weights/best.pt")

    # 检测一张图片（换成你自己的图片路径）
    results = model.predict(
        source="test/images/某张测试图.jpg",  # 项目 test 文件夹里挑一张
        save=True,   # 保存带检测框的结果图
        conf=0.4     # 置信度阈值，低于此值的框不显示
    )

    # 打印检测结果
    for r in results:
        for box in r.boxes:
            cls = model.names[int(box.cls)]
            conf = float(box.conf)
            print(f"检测到: {cls}，置信度 {conf:.2f}")