#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.01.28   15:32
-------------------------------------------------------------------------------
   @Change:   2022.01.28
-------------------------------------------------------------------------------
"""
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec_())

