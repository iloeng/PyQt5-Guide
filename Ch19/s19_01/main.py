#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.04   23:11
-------------------------------------------------------------------------------
   @Change:   2022.05.04
-------------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import QFile, QTextStream
import os


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow(None)
    textEdit = QTextEdit(mainWindow)
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
