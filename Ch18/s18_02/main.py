#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.03   17:55
-------------------------------------------------------------------------------
   @Change:   2022.05.03
-------------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 构建模型，并设置一些属性
    model = QStandardItemModel(4,  2)
    tableView = QTableView(None)
    tableView.setModel(model)
    tableView.setAlternatingRowColors(True)
    tableView.horizontalHeader().setStretchLastSection(True)

    tableView.setWindowTitle("属性窗")
    tableView.show()

    indexRoot = model.invisibleRootItem().index()
    model.setData(model.index(0, 0, indexRoot), 'id')
    model.setData(model.index(1, 0, indexRoot),  '描述')
    model.setData(model.index(2, 0, indexRoot), '验证')
    model.setData(model.index(3, 0, indexRoot),  '动画速度')
    model.setData(model.index(0, 1, indexRoot),   100)
    model.setData(model.index(1, 1, indexRoot),  '备注')
    model.setData(model.index(2, 1, indexRoot),  True)
    model.setData(model.index(3, 1, indexRoot),  2)

    sys.exit(app.exec_())

