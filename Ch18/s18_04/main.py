#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.03   22:50
-------------------------------------------------------------------------------
   @Change:   2022.05.03
-------------------------------------------------------------------------------
"""
import sys
from PyQt5.QtWidgets import QApplication
from Ch18.s18_04.delegate import *
from Ch18.s18_04.tableview import *
from Ch18.s18_04.tablemodel import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 构建模型，并设置一些属性
    model = CTableModel(int(CTableModel.EAttrIndex.Eattr_Max),  2)
    tableView = CTableView(None)
    tableView.setModel(model)
    tableView.setAlternatingRowColors(True)
    tableView.horizontalHeader().setStretchLastSection(True);
    model.setHeaderData(0, Qt.Horizontal, '属性名')
    model.setHeaderData(1, Qt.Horizontal, '属性值')

    delegate = CDelegate()
    tableView.setItemDelegate(delegate)

    tableView.setWindowTitle("属性窗")
    tableView.show()
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
    indexItem = model.index(int(CTableModel.EAttrIndex.Eattr_AnimateSpeed), 0, indexRoot)
    model.setData(indexItem, '动画速度', Qt.EditRole)
    # 设置第1列
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Id), 1, indexRoot)
    model.setData(indexItem, 100, Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Descrition), 1, indexRoot)
    model.setData(indexItem, '备注', Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_Checked), 1, indexRoot)
    model.setData(indexItem, 0, Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.EAttr_LastOneFlag), 1, indexRoot)
    model.setData(indexItem, False, Qt.EditRole)
    indexItem = model.index(int(CTableModel.EAttrIndex.Eattr_AnimateSpeed), 1, indexRoot)
    model.setData(indexItem, 2, Qt.EditRole)

    sys.exit(app.exec_())



