import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ultralytics import YOLO

from PotholeMonitor import Ui_Form   # 导入刚生成的界面类


class PotholeMonitor(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)                      # 构建界面
        self.model = YOLO('runs/detect/pothole_v1-4/weights/best.pt')
        self.result_path = None

        # 关联按钮（objectName 要和 Designer 里设置的一致！）
        self.pb_open.clicked.connect(self.open_and_detect)
        self.pb_save.clicked.connect(self.save_snapshot)

    def open_and_detect(self):
        path, _ = QFileDialog.getOpenFileName(
            self, '选择路面图片', '', '图片文件 (*.jpg *.png *.bmp)')
        if not path:
            return
        results = self.model(path)                      # YOLO 推理
        self.result_path = 'result.jpg'
        results[0].save(filename=self.result_path)      # 保存带框结果图

        pixmap = QPixmap(self.result_path)
        self.label_img.setPixmap(
            pixmap.scaled(self.label_img.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        num = len(results[0].boxes)
        self.label_tip.setText(f'提示：检测到 {num} 处坑洼')

    def save_snapshot(self):
        if self.result_path:
            QPixmap(self.result_path).save('snapshot.jpg')
            QMessageBox.information(self, 'Notice', '快照已保存！')
        else:
            QMessageBox.warning(self, 'Notice', '还没有检测结果，请先打开图片！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PotholeMonitor()
    win.show()
    sys.exit(app.exec_())