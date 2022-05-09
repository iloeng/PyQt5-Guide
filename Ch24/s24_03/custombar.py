# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtGui import QPainter, QPaintEvent, QBrush, QColor
from PyQt5.QtCore import QPointF, pyqtSignal, QRectF, QSize, Qt
from PyQt5.QtWidgets import QFrame


class CCustomBar(QFrame):
    m_dMin = 0.
    m_dMax = 0.
    m_dValue = 0.
    sig_enter = pyqtSignal(str)
    sig_leave = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CCustomBar, self).__init__(parent)
        self.setMinimumSize(QSize(0, 20))

    def setValue(self, min, max, value):
        self.m_dMin = min
        self.m_dMax = max
        self.m_dValue = value
        self.update()

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

    def paintEvent(self, event):
        QFrame.paintEvent(self, event)
        sizeWidget = self.geometry().size()
        if abs(self.m_dMax - self.m_dMin) < 0.001:
            return
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        rct = QRectF(2, 2, (self.m_dValue - self.m_dMin) / (
                self.m_dMax - self.m_dMin) * sizeWidget.width() - 4, sizeWidget.height() - 4)
        brsh = QBrush()
        brsh.setStyle(Qt.SolidPattern)
        brsh.setColor(QColor(17, 149, 189))
        painter.setBrush(brsh)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rct, 5, 5)
        painter.end()
