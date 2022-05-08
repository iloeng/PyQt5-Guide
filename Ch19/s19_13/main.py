# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread

from Ch19.s19_13.mainwindow import CMainWindow
from Ch19.s19_13.ks19_13_rc import *
from Ch19.s19_13.splashscreen import CSplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pixmap = QPixmap(":images/logo.png").scaled(600, 400)
    splashScreen = CSplashScreen(pixmap)
    splashScreen.show()
    QThread.msleep(10)  # 保证在Linux上可以正常显示出来，否则只有进度100%时才能显示。
    app.processEvents()  # 保证显示启动画面的同时仍可以正常响应鼠标、键盘等操作
    mainWindow = CMainWindow(splashScreen, None)
    splashScreen.finish(mainWindow)  # 等待主窗口初始化完毕，然后隐藏splashScreen
    mainWindow.showMaximized()

    sys.exit(app.exec_())
