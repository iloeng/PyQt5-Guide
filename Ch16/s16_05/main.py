#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.30   11:10
-------------------------------------------------------------------------------
   @Change:   2022.04.30
-------------------------------------------------------------------------------
"""

import sys

from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton
from PyQt5.QtCore import QTime, QTimer, QSize

from Ch16.s16_05.ui_maindialog import Ui_CMainDialog
from Ch16.s16_05.ks16_05_rc import *
from Utils.Paths import ICON_PATH


class CMainDialog(QDialog, Ui_CMainDialog):
    idx = 0
    timer = None
    movie = None
    pictures = [None, None, None, None]

    def __init__(self, parent=None):
        super(CMainDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.pushButton.toggled.connect(self.onStartStop)
        self.movie = QMovie(":/images/rainman.gif")
        self.movie.setScaledSize(QSize(300, 300))
        self.label_gif.setMovie(self.movie)
        self.movie.start()

        self.pictures[0] = QPixmap(":/images/pic1.png").scaled(300, 300)
        self.pictures[1] = QPixmap(":/images/pic2.png").scaled(300, 300)
        self.pictures[2] = QPixmap(":/images/pic3.png").scaled(300, 300)
        self.pictures[3] = QPixmap(":/images/pic4.png").scaled(300, 300)
        self.label_png.setPixmap(self.pictures[0])

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.slot_timeOut)
        self.timer.setInterval(300) 	# 设置定时器周期。单位:毫秒
        # self.timer.start();
        # 启动定时器
        self.pushButton.setText("start")

    def onStartStop(self):
        if self.pushButton.isChecked():
            self.timer.start()
            self.movie.start()
            self.pushButton.setText('stop')
        else:
            self.timer.stop()
            self.movie.stop()
            self.pushButton.setText('start')

    def slot_timeOut(self):
        tm = QTime.currentTime()
        strText = tm.toString("hh:mm:ss")
        self.label.setText(strText)
        # 更新图片
        self.label_png.setPixmap(self.pictures[self.idx])
        self.idx += 1
        if self.idx > 3:
            self.idx = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CMainDialog()
    widget.show()
    sys.exit(app.exec_())
