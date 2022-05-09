# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtGui import QPainter, QPaintEvent, QBrush
from PyQt5.QtCore import QPointF, pyqtSignal
from PyQt5.QtWidgets import QLabel


class CCustomLabel(QLabel):
    sig_enter = pyqtSignal(str)
    sig_leave = pyqtSignal(str)
    sig_pressed = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CCustomLabel, self).__init__(parent)

    def enterEvent(self, event):
        QLabel.enterEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]
        self.sig_enter.emit(tStr)

    def leaveEvent(self, event):
        QLabel.leaveEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]
        self.sig_leave.emit(tStr)

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]
        self.sig_pressed.emit(tStr)
