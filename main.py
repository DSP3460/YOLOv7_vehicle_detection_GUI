from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from recognizition import *


if __name__ == '__main__':
    # 应用初始化
    app = QApplication([])
    # GUI实例化
    yolo = MyWindow()
    glo._init()
    # 全局变量值设置
    glo.set_value('yolo', yolo)
    Glo_yolo = glo.get_value('yolo')
    # yolo.show() 显示GUI
    Glo_yolo.show()
    app.exec()
