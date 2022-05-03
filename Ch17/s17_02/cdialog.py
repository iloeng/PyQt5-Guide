# -*- coding: utf-8 -*-
"""
PyQt5 demo
"""

from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel
from PyQt5.QtGui import QFont, QPainter, QImage, QPolygonF
from PyQt5.QtCore import QPointF, Qt, QLineF, QRectF
from Ch17.s17_02.ui_dialog import *
from Ch17.s17_02.ks17_02_rc import *


class CDialog(QDialog, Ui_CDialog):
    imageGif = None

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.imageGif = QImage(":/images/rainman.gif")
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def paintEvent(self, evt):
        painter = QPainter()
        painter.begin(self)
        # 头顶的帽子
        linef = QLineF(QPointF(100, 20), QPointF(400, 20))
        painter.drawLine(linef)

        # 脸
        rctf = QRectF(120, 50, 260, 120)
        painter.drawRect(rctf)

        # 左侧耳朵
        polygonLeft = QPolygonF(
            [QPointF(84, 70), QPointF(64, 100), QPointF(84, 130), QPointF(104, 100)])
        painter.drawPolygon(polygonLeft)

        # 右侧耳朵
        polygonRight = QPolygonF(
            [QPointF(422, 66), QPointF(402, 96), QPointF(422, 126), QPointF(442, 96)])
        painter.drawPolygon(polygonRight)

        # 嘴巴
        polyline = QPolygonF(
            [QPointF(154, 146), QPointF(172, 156), QPointF(325, 154), QPointF(344, 135)])
        painter.drawPolyline(polyline)

        # 眼睛
        painter.drawEllipse(154, 79, 32, 33)  # 左眼
        # 小试牛刀，体验一下坐标变换
        painter.save()  # 保存当前配置，包括画笔、画刷、字体、矩阵等。
        painter.translate(170, 95)  # 把瞳孔画在眼睛(椭圆)的中心位置
        painter.rotate(45)
        painter.drawRect(-5, -5, 10, 10)
        painter.restore()  # 恢复(这次save)之前的配置

        painter.drawEllipse(300, 79, 32, 33)  # 右眼
        # 右边也来一下
        painter.save()
        painter.translate(316, 95)  # 把瞳孔画在眼睛(椭圆)的中心位置
        painter.rotate(45)
        painter.drawRect(-5, -5, 10, 10)
        painter.restore()

        # 打招呼
        painter.drawText(QPointF(202, 266), "Hi, I'm ROBO!")

        # 鼻子
        rctChord = QRectF(219, 110, 45, 60)
        painter.drawChord(rctChord,
                          40 * 16,  # 起始角度，需要把角度(40)转换为弧度
                          103 * 16)  # 跨度

        # 左脚
        rctPieLeft = QRectF(20.5, 200.5, 269, 85)
        painter.drawPie(rctPieLeft,
                        90 * 16,  # 起始弧度
                        90 * 16)  # 跨度

        # 右脚
        rctPieRight = QRectF(221, 200.5, 269, 85)
        painter.drawPie(rctPieRight,
                        0 * 16,
                        90 * 16)

        # 来张动图? 其实drawImage（）显示的是静态图片
        rctImage = QRectF(51, 300.5, 300, 300)
        painter.drawImage(rctImage, self.imageGif)

        painter.end()
