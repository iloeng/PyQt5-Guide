# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from Ch16.s16_07.ui_step3 import *


class CStep3(QWidget, Ui_CStep3):
    sig_showPage = pyqtSignal(int)
    sig_closeWindow = pyqtSignal()

    def __init__(self, parent=None):
        super(CStep3, self).__init__(parent)
        self.setupUi(self)
        self.btnPrevious.clicked.connect(self.slot_previous)
        self.btnClose.clicked.connect(self.slot_close)

    def slot_previous(self):
        self.sig_showPage.emit(1)  # 序号从0开始, step3界面是第2个，所以上一步要显示第1个。

    def slot_close(self):
        self.sig_closeWindow.emit()
