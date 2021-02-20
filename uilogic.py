# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from mainWindow import Ui_MainWindow
from PIL import Image
import numpy as np
import sys

class MyMainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    #select file
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)

if __name__ == '__main__':
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QtWidgets.QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())