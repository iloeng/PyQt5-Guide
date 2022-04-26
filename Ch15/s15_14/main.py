#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.26   21:52
-------------------------------------------------------------------------------
   @Change:   2022.04.26
-------------------------------------------------------------------------------
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox, QLineEdit


def example01():
    # 获取文本
    strText, ok = QInputDialog.getText(None, 'QInputDialog 示例', '请输入文本')
    if ok:
        QMessageBox.information(None, '您输入的文本是：', strText)
    else:
        QMessageBox.information(None, '您输入的文本是：', '您选择了放弃.')
    strText = QInputDialog.getText(None, 'QInputDialog 示例', '请输入密码', QLineEdit.Password)
    QMessageBox.information(None, '您输入的密码是：', '我不告诉你！')


def example02():
    # 获取多行文本
    strText, ok = QInputDialog.getMultiLineText(None, 'QInputDialog 示例', '请输入多行文本')
    QMessageBox.information(None, '您输入的文本是：', strText)
    # 将多行文本拆分
    strList = strText.split('\n')
    for i in strList:
        QMessageBox.information(None, '您输入的文本是：', i)


def example03():
    # 获取条目
    strList = ['苹果', '香蕉', 'orange', 'pear']
    strText, ok = QInputDialog.getItem(None, 'QInputDialog 示例', '请选择你喜欢的水果', strList, 2, True)
    if ok:
        QMessageBox.information(None, '您的选择是：', strText)
    else:
        QMessageBox.information(None, '您的选择是：', '您选择了放弃。')


def example04():
    # 获取整数
    data, ok = QInputDialog.getInt(None, 'QInputDialog 示例', '请输入整数:', 20, -100, 200, 10)
    if ok:
        QMessageBox.information(None, 'QInputDialog 示例', '您输入的整数是:%d' %data)
    else:
        QMessageBox.information(None, '您的选择是', '您选择了放弃。')


def example05():
    # 获取浮点数
    data, ok = QInputDialog.getDouble(None, 'QInputDialog 示例', '请输入浮点数:', 100.32, -12.4, 200.5, 5)
    if ok:
        QMessageBox.information(None, 'QInputDialog 示例', '您输入的浮点数是:{:g}'.format(data))
    else:
        QMessageBox.information(None, '您的选择是', '您选择了放弃。')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if True:
        example01()
    if True:
        example02()
    if True:
        example03()
    if True:
        example04()
    if True:
        example05()
    sys.exit()
