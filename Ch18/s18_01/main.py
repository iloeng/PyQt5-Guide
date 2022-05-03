#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.03   17:41
-------------------------------------------------------------------------------
   @Change:   2022.05.03
-------------------------------------------------------------------------------
"""

import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor, QFont, QImage
from PyQt5.QtWidgets import QApplication, QTreeView
from PyQt5.QtCore import Qt, QSize


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 构建模型，并设置一些属性
    model = QStandardItemModel()
    treeView = QTreeView(None)
    treeView.setModel(model)
    treeView.setRootIsDecorated(True)  # 根分支是否可展开
    # treeView.header().setFirstSectionMovable(False)  # False:首列不允许被移动,True:首列允许移动
    treeView.header().setStretchLastSection(True)  # 将最后一列设置为自动拉伸,True:自动拉伸,False:不自动拉伸。

    treeView.setWindowTitle("树视图")
    treeView.show()

    # 将数据添加到模型，包括子数据
    # 得到根节点
    itemRoot = model.invisibleRootItem()
    # 得到根节点的序号
    indexRoot = itemRoot.index()
    # 构建country节点
    itemCountry = QStandardItem('中国')
    # 将country节点作为根节点的子节点
    itemRoot.appendRow(itemCountry)
    # 设置country的字体、字色
    ft = QFont('宋体', 16)
    ft.setBold(True)
    itemCountry.setData(ft, Qt.FontRole)
    itemCountry.setData(QColor(Qt.red), Qt.TextColorRole)
    image = QImage(":/images/china.png")
    itemCountry.setData(image.scaled(QSize(24, 24)), Qt.DecorationRole)

    # 设置 itemRoot 的列数以便显示省的个数
    COLUMNCOUNT = 2  # 列数
    itemRoot.setColumnCount(COLUMNCOUNT)
    # 必须在设置列数之后才能设置标题中该列的数据。当列不存在时，设置数据无效。
    model.setHeaderData(1, Qt.Horizontal, "子项个数", Qt.DisplayRole)

    # 在Country节点所在的行的第1列显示省的个数
    model.setData(model.index(0, 1, indexRoot), 2)

    idProvince = 0
    # 构建省节点1，并添加到国家节点的下级
    itemProvince = QStandardItem('山东')
    itemCountry.appendRow(itemProvince)

    # 设置Country的列数
    itemCountry.setColumnCount(COLUMNCOUNT)

    # 设置Province节点的第0列的文本颜色为蓝色
    model.setData(model.index(0, 0, itemCountry.index()),
                  QColor(Qt.blue),
                  Qt.TextColorRole)

    # 设置Country节点第1列数据为城市个数
    model.setData(model.index(0, 1, itemCountry.index()), 2)

    # 构建所有城市
    # 构建城市节点1
    itemCity = QStandardItem('济南')
    # 添加城市节点1
    itemProvince.appendRow(itemCity)
    # 构建城市节点2
    itemCity = QStandardItem('青岛')
    # 添加城市节点2
    itemProvince.appendRow(itemCity)

    # 构建省节点2，并添加到国家节点的下级
    itemProvince = QStandardItem('河北')
    itemCountry.appendRow(itemProvince)
    # 设置Province节点的第0列的文本颜色为蓝色
    model.setData(model.index(1, 0, itemCountry.index()),
                  QColor(Qt.blue),
                  Qt.TextColorRole)

    # 设置Country节点第1列数据为城市个数
    model.setData(model.index(1, 1, itemCountry.index()), 3)

    # 遍历所有城市
    # 构建城市节点1
    itemCity = QStandardItem('北戴河')
    # 添加城市节点1
    itemProvince.appendRow(itemCity)
    # 构建城市节点2
    itemCity = QStandardItem('张家口')
    # 添加城市节点2
    itemProvince.appendRow(itemCity)
    # 构建城市节点3
    itemCity = QStandardItem('保定')
    # 添加城市节点3
    itemProvince.appendRow(itemCity)

    sys.exit(app.exec_())
