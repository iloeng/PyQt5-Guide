# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtGui import QPainter, QPaintEvent, QBrush
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import pyqtSignal


class CCustomWidget(QFrame):
    sig_enter = pyqtSignal(str)
    sig_leave = pyqtSignal(str)
    sig_pressed = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CCustomWidget, self).__init__(parent)

    def enterEvent(self, event):
        QFrame.enterEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]
        self.sig_enter.emit(tStr)

    def leaveEvent(self, event):
        QFrame.leaveEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]
        self.sig_leave.emit(tStr)

    def mousePressEvent(self, event):
        QFrame.mousePressEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]
        self.sig_pressed.emit(tStr)
