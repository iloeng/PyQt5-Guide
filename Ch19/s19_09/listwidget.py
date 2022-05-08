# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtXml import QDomDocument

class CListWidget (QListWidget):	
	strFileName = ''
	def __init__(self, parent=None) :
		super(CListWidget, self).__init__(parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event) :
		if event.mimeData().hasFormat("dnd/format") :
			event.setDropAction(Qt.CopyAction)
			event.setAccepted(True)
		else:
			event.setAccepted(False)

	def dragMoveEvent(self, event) :
		if event.mimeData().hasFormat("dnd/format") :
			event.setDropAction(Qt.CopyAction)
			event.setAccepted(True)
		else:
			event.setAccepted(False)
			
	def dropEvent(self, event) :
		if ((event.mimeData() is None) or not event.mimeData().hasFormat("dnd/format")) :
			return
			
		mimeData = event.mimeData().data("dnd/format") 
		document = QDomDocument()
		document.setContent(mimeData)
		rootDoc = document.firstChildElement()
		if (rootDoc.isNull() or (rootDoc.tagName() != "root")):
			return
		eleDoc = rootDoc.firstChildElement()
		# 判断格式的合法性
		if (eleDoc.isNull() or (eleDoc.tagName() != "document")) :
			return
		strText = eleDoc.attribute("text")
		bBold = eleDoc.attribute("bold")
		item = QListWidgetItem(strText, self)
		ft = item.font()
		ft.setBold(int(bBold))
		item.setFont(ft)
		self.addItem(item)
		event.setDropAction(Qt.CopyAction)
		event.setAccepted(True)
