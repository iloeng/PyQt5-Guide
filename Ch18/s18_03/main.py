#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.03   21:43
-------------------------------------------------------------------------------
   @Change:   2022.05.03
-------------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel
from Ch18.s18_03.delegate import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 构建模型，并设置一些属性
    model = QStandardItemModel(EAttrIndex.Eattr_Max,  2)
    tableView = QTableView(None)
    tableView.setModel(model)
    tableView.setAlternatingRowColors(True)
    tableView.horizontalHeader().setStretchLastSection(True)

    delegate = CDelegate()
    tableView.setItemDelegate(delegate)

    tableView.setWindowTitle("属性窗")
    tableView.show()

    indexRoot = model.invisibleRootItem().index()
    model.setData(model.index(EAttrIndex.EAttr_Id, 0, indexRoot), 'id')
    model.setData(model.index(EAttrIndex.EAttr_Descrition, 0, indexRoot),  '描述')
    model.setData(model.index(EAttrIndex.EAttr_Id, 1, indexRoot),   100)
    model.setData(model.index(EAttrIndex.EAttr_Descrition, 1, indexRoot),  '备注')

    sys.exit(app.exec_())


