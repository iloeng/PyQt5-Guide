#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.04   22:27
-------------------------------------------------------------------------------
   @Change:   2022.05.04
-------------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile
from Ch18.s18_05.delegate import *
from Ch18.s18_05.treeview import *
from Ch18.s18_05.tablemodel import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 构建模型，并设置一些属性
    model = CTableModel(int(CTableModel.EAttrIndex.Eattr_Max), 2)
    treeView = CTreeView(None)
    treeView.setModel(model)
    treeView.setAlternatingRowColors(True)
    file = QFile(":/qss/treeview.qss")
    bok = file.open(QFile.ReadOnly)
    if bok:
        styleSheet = file.readAll()
        treeView.setStyleSheet(styleSheet)
    model.setHeaderData(0, Qt.Horizontal, '属性名')
    model.setHeaderData(1, Qt.Horizontal, '属性值')

    delegate = CDelegate()
    treeView.setItemDelegate(delegate)

    treeView.setWindowTitle("属性窗")
    treeView.show()
    # 设置第0列
    indexRoot = model.invisibleRootItem().index()
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Id), 0, indexRoot)
    model.setData(indexItem, 'id', Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Descrition), 0, indexRoot)
    model.setData(indexItem, '描述', Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Checked), 0, indexRoot)
    model.setData(indexItem, '是否已验证', Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_LastOneFlag), 0, indexRoot)
    model.setData(indexItem, '是否最后一个', Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.Eattr_Animate), 0, indexRoot)
    model.setData(indexItem, '动画', Qt.EditRole)
    model.insertRows(0, 2, indexItem)  # 插入两个子数据项
    model.insertColumns(0, 2, indexItem)  # 插入两列(属性名、属性值)
    indexSubItem = model.index(int(CTableModel.EAttrIndexAnimate.EattrAnimate_AnimateType), 0,
                               indexItem)
    model.setData(indexSubItem, '类型', Qt.EditRole)
    indexSubItem = model.index(int(CTableModel.EAttrIndexAnimate.EattrAnimate_AnimateSpeed), 0,
                               indexItem)
    model.setData(indexSubItem, '速度', Qt.EditRole)
    # 设置第1列
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Id), 1, indexRoot)
    model.setData(indexItem, 100, Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Descrition), 1, indexRoot)
    model.setData(indexItem, '备注', Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Checked), 1, indexRoot)
    model.setData(indexItem, 0, Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_LastOneFlag), 1, indexRoot)
    model.setData(indexItem, False, Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.Eattr_Animate), 0, indexRoot)
    indexSubItem = model.index(int(CTableModel.EAttrIndexAnimate.EattrAnimate_AnimateType), 1,
                               indexItem)
    model.setData(indexSubItem, 1, Qt.EditRole)
    indexSubItem = model.index(int(CTableModel.EAttrIndexAnimate.EattrAnimate_AnimateSpeed), 1,
                               indexItem)
    model.setData(indexSubItem, int(CTableModel.EAnimateSpeed.EAnimateSpeed_Fast), Qt.EditRole)

    sys.exit(app.exec_())
