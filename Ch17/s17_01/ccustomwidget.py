# -*- coding: utf-8 -*-
"""
PyQT5 demo
"""

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont, QMovie, QPainter
from PyQt5.QtCore import QSize, Qt, QPointF
from Ch17.s17_01.ui_customwidget import *


class CCustomWidget(QWidget, Ui_CCustomWidget):
    movie = None
    transparentLabel = None

    def __init__(self, parent=None):
        super(CCustomWidget, self).__init__(parent)
        self.setupUi(self)
        # 添加1个控件用来展示动画
        self.movie = QMovie(":/images/rainman.gif")
        self.movie.setScaledSize(QSize(self.label_gif.geometry().size()))
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        self.transparentLabel = QLabel(self)
        self.transparentLabel.setText("I'm transparent.")
        self.transparentLabel.setGeometry(80, 250, 200, 40)
        self.transparentLabel.setStyleSheet("color: rgb(255, 48, 190);border:none")

    def resizeEvent(self, evt):
        QWidget.resizeEvent(self, evt)  # 调用父类接口
        self.movie.setScaledSize(QSize(self.label_gif.geometry().size()))
        rctGif = self.label_gif.geometry()
        x = rctGif.x() + rctGif.width() / 3
        y = rctGif.y() + rctGif.height() / 6
        self.transparentLabel.setGeometry(x, y, 200, 40)

    def paintEvent(self, evt):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.red)
        ft = QFont()
        ft.setPointSizeF(30)
        painter.setFont(ft)
        pt = QPointF()
        pt = self.label_gif.geometry().bottomLeft() + QPointF(0, 20)
        # 下面代码绘制的文本始终显示在本控件的底层
        painter.drawText(pt, "Draw In Widget.")
        painter.end()
