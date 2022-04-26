#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.26   22:58
-------------------------------------------------------------------------------
   @Change:   2022.04.26
-------------------------------------------------------------------------------
"""
import sys
import platform

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QDialog, QFileDialog, QMessageBox,
    QSystemTrayIcon, QMenu, QAction
)
from PyQt5.Qt import qApp
from PyQt5.QtCore import Qt

from Ch15.s15_16.ui_dialog import Ui_CDialog
from Ch15.s15_16.ks15_16_rc import *


class CDialog(QDialog, Ui_CDialog):

    tray = None              # 系统托盘对象
    icon = None              # 应用程序图标
    tray_menu = None         # 托盘中的菜单
    RestoreAction = None     # 托盘菜单项
    QuitAction = None        # 托盘菜单项

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.btnGetFileName.clicked.connect(self.getFileName)
        self.addSystemTray()
        self.setWindowFlags(self.windowFlags() or Qt.WindowMinimizeButtonHint)

    def addSystemTray(self):
        # 添加到托盘
        self.tray = QSystemTrayIcon(self)
        self.icon = QIcon(':/pic/images/my.ico')
        self.tray.setIcon(self.icon)
        self.setWindowIcon(self.icon)
        self.tray.activated.connect(self.slot_iconActivated)

        # 点击托盘中图标时弹出的菜单
        self.tray_menu = QMenu(QApplication.desktop())
        self.RestoreAction = QAction(u'还原', self, triggered=self.show)
        # 添加一级菜单动作选项（还原主窗口）
        self.QuitAction = QAction(u'退出', self, triggered=qApp.quit)
        # 添加一级菜单动作选项（退出程序）
        self.tray_menu.addAction(self.RestoreAction)  # 为菜单添加动作
        self.tray_menu.addAction(self.QuitAction)
        self.tray.setContextMenu(self.tray_menu)      # 设置系统托盘菜单
        self.tray.show()
        # 当单击提示信息时， 给出反馈
        self.tray.messageClicked.connect(self.slot_messageClicked)

    def slot_iconActivated(self, reason):
        if QSystemTrayIcon.Trigger == reason:
            self.show()
        elif QSystemTrayIcon.DoubleClick == reason:
            self.show()

    def closeEvent(self, event: QtCore.QEvent):
        if (not event.spontaneous()) or (not self.isVisible()):
            return
        if self.tray.isVisible():
            QMessageBox.information(
                self,
                '系统托盘应用',
                '程序将最小化到系统托盘中运行，如果希望恢复界面，\n请单击或右击托盘中的图标并选择相应的菜单项。',
            )
            self.hide()
            event.ignore()

    def changeEvent(self, event: QtCore.QEvent) -> None:
        if not event.WindowStateChange:
            QDialog.changeEvent(event)
            return
        if Qt.WindowMinimized == self.windowState():
            self.hide()
            self.setWindowFlags(Qt.Tool)
            self.tray.show()
            self.tray.showMessage(self.windowTitle(), '请单击')
            event.ignore()

    def showMessage(self, info):
        self.tray.showMessage('标题', info, self.icon, 5000)

    def slot_messageClicked(self):
        QMessageBox.information(None, '标题', '看来您已经阅读了软件发送的提示信息。')

    def getFileName(self):
        strFilter = 'text file(*.txt);;XML File(*.xml);;*(*.*)'
        sys = platform.system()
        if sys == 'Windows':
            fileName, _ = QFileDialog.getOpenFileName(
                self, 'select file to open',
                'C:\\', strFilter, 'XML File(*.xml)'
            )
        else:
            fileName, _ = QFileDialog.getOpenFileName(
                self, 'select file to open', '/usr/local/',
                strFilter, 'XML File(*.xml)', QFileDialog.DontUseNativeDialog
            )
        QMessageBox.information(None, '文件名', fileName)
        info = '打开的文件为：' + fileName
        self.showMessage(info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())


