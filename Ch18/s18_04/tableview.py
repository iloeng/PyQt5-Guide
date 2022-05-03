# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QModelIndex


class CTableView(QTableView):
    indexLast = QModelIndex()

    def __init__(self, parent=None):
        super(CTableView, self).__init__(parent)

    def mousePressEvent(self, evt):
        pt = evt.pos()
        index = self.indexAt(pt)
        # 如果本次选择和上次不一样，需要关闭上次的编辑器
        if index != self.indexLast and self.indexLast.isValid():
            self.closePersistentEditor(self.indexLast)
        self.indexLast = index
        # 新的序号有效，且是允许编辑的列
        if index.isValid() and 1 == index.column():
            self.openPersistentEditor(index)
        QTableView.mousePressEvent(self, evt)
