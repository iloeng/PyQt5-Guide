#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.23   17:42
-------------------------------------------------------------------------------
   @Change:   2022.04.23
-------------------------------------------------------------------------------
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QAbstractItemView, QListWidgetItem

from Ch15.s15_11.ui_dialog import Ui_CDialog
from Utils.Paths import ICON_PATH


class CDialog(QDialog, Ui_CDialog):

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.listWidgetLeft.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidgetRight.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidgetLeft.addItem('C++')
        self.listWidgetLeft.addItem('Python')
        self.listWidgetLeft.addItem('Java')
        self.listWidgetLeft.addItem('C#')
        self.listWidgetLeft.addItem('Ruby')
        self.listWidgetLeft.addItem('Go')
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.btn2Left.clicked.connect(self.slot_move2Left)
        self.btn2Right.clicked.connect(self.slot_move2Right)
        self.btnAscending.clicked.connect(self.slot_ascending)
        self.btnDescending.clicked.connect(self.slot_descending)
        self.listWidgetLeft.itemClicked.connect(self.slot_leftItemClicked)
        self.listWidgetLeft.itemDoubleClicked.connect(self.slot_leftItemDoubleClicked)
        self.listWidgetLeft.currentItemChanged.connect(self.slot_leftCurrentItemChanged)

    def slot_move2Left(self):
        # 右侧列表允许复选
        # 首先得到右侧列表中选中的项的集合
        selectedItems = self.listWidgetRight.selectedItems()
        idx = 0
        # 遍历该集合， 并将项移动到左侧列表
        for item in selectedItems:
            idx = self.listWidgetRight.row(item)
            self.listWidgetRight.takeItem(idx)
            self.listWidgetLeft.addItem(item)

    def slot_move2Right(self):
        # 左侧列表只允许单选
        # 得到左侧列表当前选中的项
        pItem = self.listWidgetLeft.currentItem()
        if pItem is None:
            return
        idx = self.listWidgetLeft.row(pItem)
        self.listWidgetLeft.takeItem(idx)
        self.listWidgetRight.addItem(pItem)

    def slot_ascending(self):
        self.listWidgetRight.sortItems(Qt.AscendingOrder)

    def slot_descending(self):
        self.listWidgetRight.sortItems(Qt.DescendingOrder)

    def slot_leftItemClicked(self, item):
        str = 'My Favorite Program Language Is '
        str += item.text()
        self.label.setText(str)
        # 同时将选中项字体加粗
        ft = item.font()
        ft.setBold(True)
        item.setFont(ft)

    def slot_leftItemDoubleClicked(self, item: QListWidgetItem):
        # 双击时， 将左侧列表中被单击的项移动到右侧列表
        idx = self.listWidgetLeft.row(item)
        self.listWidgetLeft.takeItem(idx)
        self.listWidgetRight.addItem(item)

    def slot_leftCurrentItemChanged(self, current, previous: QListWidgetItem):
        # 将之前选中项的字体粗体恢复
        if not (previous is None):
            ft = previous.font()
            ft.setBold(False)
            previous.setFont(ft)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())




