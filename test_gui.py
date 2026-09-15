import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)          # 1. 应用程序对象（必须有，且只有一个）
label = QLabel("Hello, YOLOv8!")      # 2. 一个控件（这里是文字标签）
label.show()                          # 3. 显示它
sys.exit(app.exec_())                 # 4. 事件循环，直到窗口关闭