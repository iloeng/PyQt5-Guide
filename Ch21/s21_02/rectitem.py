# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QRectF
from Ch21.s21_02.graphicsitem import EGraphItemType


class CGraphRectItem(QGraphicsItem):
    m_width = float()
    m_height = float()

    def __init__(self, parentItem):
        super(CGraphRectItem, self).__init__(parentItem)

    def type(self):
        return EGraphItemType.EGraphItemType_Rect

    def setWidth(self, dW):
        self.m_width = dW

    def getWidth(self):
        return self.m_width

    def setHeight(self, dH):
        self.m_height = dH

    def getHeight(self):
        return self.m_height

    def paint(self, painter, option, widget):
        painter.drawRect(self.boundingRect())

    def boundingRect(self):
        boundRt = QRectF(self.m_width / (-2.0) - 2, self.m_height / (-2.0) - 2, self.m_width + 4,
                         self.m_height + 4)
        return boundRt

    def shape(self):
        paintPath = QPainterPath()
        paintPath.addRect(self.boundingRect())
        return paintPath

    def getItemRect(self):
        rct = QRectF(self.m_width / (-2.0), self.m_height / (-2.0), self.m_width, self.m_height)
        return rct
