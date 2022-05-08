# -*- coding: utf-8 -*-
import sys	   
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QMutex, QMutexLocker, QThread, QFile
from config import CConfig
from customevent import CCustomEvent

class CSendThread(QThread): 
	bWorking = False
	bFinished = True
	mtxRunning = QMutex()
	mainDialog = None # 主窗口
	def __init__(self) :
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

			event = CCustomEvent()
			event.setStudentNumber(config.getStudentNumber())
			event.setTeacherNumber(config.getTeacherNumber())
			QApplication.postEvent(self.mainDialog, event)
		self.bFinished = True

	def setDialog(self, dialog):
		self.mainDialog = dialog

	def isWorking(self):
		locker = QMutexLocker(self.mtxRunning)
		return self.bWorking
	
	def exitThread(self):
		self.mtxRunning.lock()
		self.bWorking = False
		self.mtxRunning.unlock()
		while not self.bFinished:
			QThread.msleep(10)
