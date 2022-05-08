# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QPainter, QFont, QColor, QMouseEvent
from PyQt5.QtCore import Qt, QPointF, QFile, QTextStream
from PyQt5.QtCore import pyqtSignal


class CTextEdit(QTextEdit):
    sig_viewMouseMove = pyqtSignal(QMouseEvent)  # 定义一个信号
    strFileName = ''

    def __init__(self, parent=None):
        super(CTextEdit, self).__init__(parent)
        self.setMouseTracking(True)

    def paintEvent(self, evt):
        painter = QPainter()
        painter.begin(self.viewport())
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(Qt.blue)
        painter.fillRect(evt.rect(), QColor(0, 255, 255, 100))
        ft = QFont("宋体", 18)
        painter.setFont(ft)
        painter.drawText(QPointF(100, 100), "file read ok!")
        painter.end()
        QTextEdit.paintEvent(self, evt)

    def mouseMoveEvent(self, evt):
        QTextEdit.mouseMoveEvent(self, evt)  # 首先，调用基类接口
        self.sig_viewMouseMove.emit(evt)

    def openFile(self, strFileName):
        file = QFile()
        file.setFileName(strFileName)
        print(strFileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            self.setText('')
            self.strFileName = ''
            return False
        input = QTextStream(file)
        input.setCodec("GBK")
        str = input.readAll()
        self.setText(str)
        self.strFileName = strFileName
        return True

    # 获取当前打开的文件的名字,全路径。
    def currentFileName(self):
        return self.strFileName
