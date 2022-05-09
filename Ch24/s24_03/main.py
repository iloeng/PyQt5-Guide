# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator
from Ch24.s24_03.cmainwidget import *
import os

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 安装我们项目的翻译文件
    strDir = './ks24_03.qm'
    trans = QTranslator(None)
    trans.load('ks24_03', strDir)
    _app = QApplication.instance()
    _app.installTranslator(trans)

    mainwidget = CMainWidget(None)
    mainwidget.show()

    sys.exit(app.exec_())
