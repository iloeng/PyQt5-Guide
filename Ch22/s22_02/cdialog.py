# -*- coding: utf-8 -*-
"""
	案例代码
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QDir, QEvent
from Ch22.s22_02.ui_dialog import *
from Ch22.s22_02.recvthread import *
from Ch22.s22_02.sendthread import *


class CDialog(QDialog, Ui_CDialog):
    recvThread = CRecvThread()
    sendThread = CSendThread()

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('多线程')

        strDir = 'test/'
        dir = QDir()
        if not dir.exists(strDir):
            dir.mkpath(strDir)

        self.btnStartThread.clicked.connect(self.slot_startThread)
        self.btnStopThread.clicked.connect(self.slot_stopThread)
        self.sendThread.setDialog(self)

    def __del__(self):
        self.slot_stopthread()

    def slot_startThread(self):
        self.recvThread.start()
        self.sendThread.start()

    def slot_stopThread(self):
        self.recvThread.exitThread()
        self.sendThread.exitThread()

    def customEvent(self, event):
        if event.type() == (QEvent.User + 1):
            strText = "teacher:{0}, student:{1}".format(event.getTeacherNumber(),
                                                        event.getStudentNumber())
            self.label.setText(strText)
