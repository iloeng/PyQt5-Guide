# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class CEditor(QLabel):
    sig_editFinished = pyqtSignal()

    def __init__(self, parent=None):
        super(CEditor, self).__init__(parent)
        self.setMouseTracking(True)
        self.setAutoFillBackground(True)

    def mousePressEvent(self, event):
        if self.text() == '否':
            self.setText('是')
        else:
            self.setText('否')
        self.sig_editFinished.emit()
