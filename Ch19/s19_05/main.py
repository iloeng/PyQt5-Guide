#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.06   21:19
-------------------------------------------------------------------------------
   @Change:   2022.05.06
-------------------------------------------------------------------------------
"""

import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream

from Ch19.s19_05.textedit import CTextEdit
from Ch19.s19_05.mainwindow import CMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = CMainWindow(None)
    mainWindow.show()

    sys.exit(app.exec_())
