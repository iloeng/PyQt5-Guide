#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.06   20:58
-------------------------------------------------------------------------------
   @Change:   2022.05.06
-------------------------------------------------------------------------------
"""

import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QFile, QTextStream

from Ch19.s19_02.textedit import CTextEdit


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow(None)
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

