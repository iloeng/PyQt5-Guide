#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.06   21:11
-------------------------------------------------------------------------------
   @Change:   2022.05.06
-------------------------------------------------------------------------------
"""

import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream

from Ch19.s19_03.textedit import CTextEdit
from Ch19.s19_03.mainwindow import CMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = CMainWindow(None)
    textEdit = CTextEdit(mainWindow)
    file = QFile()

    strFile = 'input.txt'
    file.setFileName(strFile)
    strText = str()
    if file.open(QFile.ReadOnly | QFile.Text):
        inputs = QTextStream(file)
        inputs.setCodec('UTF-8')
        strText = inputs.readAll()

    textEdit.setText(strText)
    mainWindow.setCentralWidget(textEdit)
    mainWindow.show()

    sys.exit(app.exec_())

