# -*- coding: utf-8 -*-
"""
PyQt5 demo
"""

from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel
from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtCore import QPointF, Qt
from Ch17.s17_01.ui_dialog import *
from Ch17.s17_01.ccustomwidget import CCustomWidget


class CDialog(QDialog, Ui_CDialog):
    customWidget = None

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)

        gridLayout = QGridLayout(self.widget)
        gridLayout.setObjectName("gridLayout")
        self.customWidget = CCustomWidget(self)
        gridLayout.addWidget(self.customWidget, 0, 0)
        # 下面代码构造的QLabel对象将覆盖在 customWidget 的上方。因此得出结论，先创建的控件在下，后创建的控件在上。
        newLabel = QLabel(self)
        newLabel.setStyleSheet("color:rgb(0, 255,0)")
        newLabel.setText("Hi..................I'm label in CDialog.")
        newLabel.setGeometry(0, 45, 400, 30)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def paintEvent(self, evt):
        painter = QPainter()
        painter.begin(self)
        ft = QFont()
        ft.setPointSizeF(30)
        painter.setFont(ft)
        painter.setPen(Qt.blue)
        # 下面代码绘制的文本始终显示在本控件的底层,在m_pWidget的下层。
        painter.drawText(QPointF(0, self.customWidget.geometry().bottom() + 5),
                         "draw text in cdialog.")
        painter.end()
