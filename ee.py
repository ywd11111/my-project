from ultralytics import YOLO
m = YOLO('runs/detect/pothole_v1-4/weights/best.pt')
print(m.names)
r = m('test/D:\QQ\新建文件夹\测试1.jpg', conf=0.25)
print('检出框数:', len(r[0].boxes))