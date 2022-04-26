#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.26   22:15
-------------------------------------------------------------------------------
   @Change:   2022.04.26
-------------------------------------------------------------------------------
"""
import sys
import platform

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QApplication, QMessageBox, QDialog

from Ch15.s15_15.ui_dialog import Ui_CDialog
from Utils.Paths import ICON_PATH


class CDialog(QDialog, Ui_CDialog):

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.btnGetFileName.clicked.connect(self.getFileName)

    def getFileName(self):
        strFilter = 'text file(*.txt);;XML File(*.xml);;*(*.*)'
        sys = platform.system()
        if sys == 'Windows':
            fileName, _ = QFileDialog.getOpenFileName(
                self, 'select file to open', 'C:\\', strFilter, 'XML(*.xml)')
        else:
            fileName, _ = QFileDialog.getOpenFileName(
                self, 'select file to open', '/usr/local/', strFilter, 'XML(*.xml)',
                QFileDialog.DontUseNativeDialog
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())

