# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDockWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

from Ch19.s19_11.logevt import SLog


class CLogDockWidget(QDockWidget):
    tableWidget = None
    maxLogNum = 1000  # 日志窗口显示的最大日志数目

    def __init__(self, title, parent=None, flags=Qt.WindowFlags(0)):
        super(CLogDockWidget, self).__init__(title, parent, flags)
        self.ableWidget = QTableWidget(self)
        self.ableWidget.setColumnCount(3)
        font = self.ableWidget.horizontalHeader().font()  # 设置表头字体加粗
        font.setBold(True)
        self.ableWidget.horizontalHeader().setFont(font)
        self.ableWidget.horizontalHeader().setFixedHeight(25)  # 设置表头的高度
        self.ableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ableWidget.setHorizontalHeaderLabels(["级别", "时间", "内容"])
        self.ableWidget.setColumnWidth(0, 100)  # 设置第0列的列宽
        self.ableWidget.setColumnWidth(1, 100)  # 设置第1列的列宽
        self.ableWidget.horizontalHeader().setStretchLastSection(True)
        self.ableWidget.setShowGrid(False)  # 设置不显示格子线
        self.ableWidget.verticalHeader().setHidden(True)  # 设置垂直表头不可见
        strStyle = "QHeaderView.sectionbackground:skyblue"
        self.ableWidget.horizontalHeader().setStyleSheet(strStyle)  # 设置表头背景色
        self.setWidget(self.ableWidget)

    def customEvent(self, evt):
        if evt is None:
            return
        log = evt.getLog()
        rowIndex = self.ableWidget.rowCount()
        while rowIndex >= self.maxLogNum:  # 删除最后的记录
            self.ableWidget.removeRow(rowIndex - 1)
            rowIndex = rowIndex - 1

        # 新增的永远加到最前面
        self.ableWidget.insertRow(0)
        self.ableWidget.setItem(0, 0, QTableWidgetItem(SLog.translateLevel(log.level)))
        self.ableWidget.setItem(0, 1, QTableWidgetItem(log.time.toString()))
        self.ableWidget.setItem(0, 2, QTableWidgetItem(log.msg))
