#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.23   15:44
-------------------------------------------------------------------------------
   @Change:   2022.04.23
-------------------------------------------------------------------------------
"""
import sys

from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QSize

from Ch15.s15_08.ui_dialog import Ui_CDialog
from Utils.Paths import ICON_PATH


class CDialog(QDialog, Ui_CDialog):
    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.show()

        movie = QMovie(":pic/images/rainman.gif")
        size = QSize(self.label.geometry().size())
        movie.setScaledSize(size)
        print("w=%d, h=%d" % (size.width(), size.height()))
        self.label.setMovie(movie)
        movie.start()


if __name__ == '__main__':
    import Ch15.s15_08.ks15_08_rc
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())


