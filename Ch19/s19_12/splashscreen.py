# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QSplashScreen, QProgressBar
from PyQt5.QtGui import QPixmap


class CSplashScreen(QSplashScreen):
    progressBar = None

    def __init__(self, pixmap):
        super(CSplashScreen, self).__init__(pixmap)
        self.progressBar = QProgressBar(self)
        # 设置进度条的位置
        self.progressBar.setGeometry(0, pixmap.height() - 50, pixmap.width(), 30)
        # 设置进度条的样式
        self.progressBar.setStyleSheet('''QProgressBar {color:black font:30px text-align:center } 
        QProgressBar::chunk {background-color: rgb(200, 160, 16)}''')
        # 设置进度条的范围
        self.progressBar.setRange(0, 100)
        # 设置进度条的当前进度（默认值）
        self.progressBar.setValue(0)

    def slot_setProgress(self, step):
        self.progressBar.setValue(step % 101)
