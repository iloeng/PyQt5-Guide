# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QPainter, QFont, QColor
from PyQt5.QtCore import Qt, QPointF

class CTextEdit(QTextEdit):	
	def __init__(self, parent=None) :
		super(CTextEdit, self).__init__(parent)
		
	def paintEvent(self, evt):
		painter = QPainter()
		painter.begin(self.viewport())
		painter.setRenderHint(QPainter.Antialiasing, True)	
		painter.setPen(Qt.blue)
		painter.fillRect(evt.rect(), QColor(0, 255, 255, 100))
		ft = QFont("宋体", 18)
		painter.setFont(ft)
		painter.drawText(QPointF(100,100), "file read ok!")
		painter.end()
		QTextEdit.paintEvent(self, evt)


