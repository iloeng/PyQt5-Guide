# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QRectF

from Ch19.s19_12.graphicsitem import EGraphItemType


class CGraphEllipseItem(QGraphicsItem):
    m_width = 0
    m_height = 0

    def __init__(self, parentItem):
        super(CGraphEllipseItem, self).__init__(parentItem)

    def type(self):
        return EGraphItemType.EGraphItemType_Ellipse

    def setWidth(self, dW):
        self.m_width = dW

    def getWidth(self):
        return self.m_width

    def setHeight(self, dH):
        self.m_height = dH

    def getHeight(self):
        return self.m_height

    def paint(self, painter, option, widget):
        painter.drawEllipse(self.boundingRect())

    def boundingRect(self):
        boundRt = QRectF(self.m_width / (-2.0), self.m_height / (-2.0), self.m_width,
                         self.m_height)
        return boundRt

    def shape(self):
        paintPath = QPainterPath()
        paintPath.addEllipse(self.boundingRect())
        return paintPath
