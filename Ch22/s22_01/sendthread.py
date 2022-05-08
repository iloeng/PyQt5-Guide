# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import QMutex, QMutexLocker, QThread, QFile
from Ch22.s22_01.config import CConfig


class CSendThread(QThread):
    bWorking = False
    bFinished = True
    mtxRunning = QMutex()

    def __init__(self):
        super(CSendThread, self).__init__()

    def run(self):
        self.bFinished = False
        self.bWorking = True
        strFileName = 'test/send.txt'
        file = QFile(strFileName)
        strContent = str()
        config = CConfig()
        while self.isWorking():
            QThread.sleep(1)
            strContent = "teacher:{0}, student:{1}".format(config.getTeacherNumber(),
                                                           config.getStudentNumber())
            if not file.open(QFile.WriteOnly | QFile.Truncate | QFile.Text):
                continue
            file.write(strContent.encode('UTF-8'))
            file.close()
        self.bFinished = True

    def isWorking(self):
        locker = QMutexLocker(self.mtxRunning)
        return self.bWorking

    def exitThread(self):
        self.mtxRunning.lock()
        self.bWorking = False
        self.mtxRunning.unlock()
        while not self.bFinished:
            QThread.msleep(10)
