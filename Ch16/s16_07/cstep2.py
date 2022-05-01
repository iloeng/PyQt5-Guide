# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from Ch16.s16_07.ui_step2 import *


class CStep2(QWidget, Ui_CStep2):
    sig_showPage = pyqtSignal(int)

    def __init__(self, parent=None):
        super(CStep2, self).__init__(parent)
        self.setupUi(self)
        self.btnPrevious.clicked.connect(self.slot_previous)
        self.btnNext.clicked.connect(self.slot_next)

    def slot_previous(self):
        self.sig_showPage.emit(0)  # 序号从0开始, step2界面是第1个，所以上一步要显示第0个。

    def slot_next(self):
        self.sig_showPage.emit(2)  # 序号从0开始, step2界面是第1个，所以下一步要显示第2个。
