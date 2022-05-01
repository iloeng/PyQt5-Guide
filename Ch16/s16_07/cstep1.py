# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from Ch16.s16_07.ui_step1 import *

class CStep1(QWidget, Ui_CStep1):	
	sig_showPage = pyqtSignal(int)
	def __init__(self, parent=None) :
		super(CStep1, self).__init__(parent)
		self.setupUi(self)
		self.btnNext.clicked.connect(self.slot_next)
	
	def slot_next(self):
		self.sig_showPage.emit(1) # 序号从0开始, step1界面是第0个，所以下一步要显示第1个。
