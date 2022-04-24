#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.24   22:17
-------------------------------------------------------------------------------
   @Change:   2022.04.24
-------------------------------------------------------------------------------
"""

import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QSizePolicy, QStyle, QFileDialog, QSlider
)
from PyQt5.QtGui import QMovie, QPalette, QIcon
from PyQt5.QtCore import Qt, QFileInfo

from Ch15.s15_12.ui_dialog import Ui_CDialog
from Utils.Paths import ICON_PATH


class CDialog(QDialog, Ui_CDialog):

    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.currentDirectory = ''
        # 初始化控件
        self.initialControls()
        # 连接信号槽
        self.connectSignalsAndSlots()
        # 设置按钮状态
        self.slot_updateButtons()
        self.resize(500, 500)

    def initialControls(self):
        self.movie = QMovie(self)
        # 当动画播放完一遍后， 就完成了缓存， 可以通过滑动条来调整视频播放进度
        self.movie.setCacheMode(QMovie.CacheAll)
        # 为标签设置对齐方式和尺寸策略
        self.movieLabel.setAlignment(Qt.AlignCenter)
        self.movieLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.movieLabel.setBackgroundRole(QPalette.Dark)
        # 初始化滑动条
        self.frameSlider.setTickPosition(QSlider.TicksBelow)  # 设置刻度位置
        self.frameSlider.setTickInterval(10)
        # 设置滑动条初始位置
        self.slot_updateFrameSlider()
        # 设置 label， 将内容缩放以填满控件
        self.movieLabel.setScaledContents(True)
        # 设置按钮
        self.openButton.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        self.openButton.setToolTip('Open File')
        self.pauseButton.setCheckable(True)
        self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pauseButton.setToolTip('Pause')
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.setToolTip('Stop')
        self.quitButton.setIcon(self.style().standardIcon(QStyle.SP_DialogCloseButton))
        self.quitButton.setToolTip('Quit')

    def slot_updateFrameSlider(self):
        self.frameSlider.blockSignals(True)
        bHasFrames = (self.movie.currentFrameNumber() >= 0)
        if bHasFrames:
            self.frameSlider.setValue(self.movie.currentFrameNumber())
        self.frameSlider.setEnabled(bHasFrames)
        self.frameSlider.blockSignals(False)

    def connectSignalsAndSlots(self):
        self.openButton.clicked.connect(self.slot_open)
        self.pauseButton.clicked.connect(self.slot_pause)
        self.stopButton.clicked.connect(self.movie.stop)
        self.quitButton.clicked.connect(self.close)
        self.movie.stateChanged.connect(self.slot_updateButtons)
        self.movie.frameChanged.connect(self.slot_updateFrameSlider)
        self.frameSlider.valueChanged.connect(self.slot_gotoFrame)

    def slot_gotoFrame(self, value):
        if value >= self.movie.frameCount():
            return
        self.movie.blockSignals(True)
        # 播放过的动画响应比较快， 还没被播放过的部分会稍微慢些
        self.movie.jumpToFrame(value)
        # 需要更新 label 对象
        self.movieLabel.update()
        self.movie.blockSignals(False)

    def openFile(self, fileName):
        self.currentDirectory = QFileInfo(fileName).path()
        self.movie.stop()
        self.movieLabel.setMovie(self.movie)
        self.movie.setFileName(fileName)
        self.movie.start()
        self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.pauseButton.setToolTip('Pause')
        # 更新按钮状态
        self.slot_updateButtons()
        # 更新滑动条最值
        self.changeFrameSliderMaxMin()

    def changeFrameSliderMaxMin(self):
        bHasFrames = (self.movie.currentFrameNumber() >= 0)
        if bHasFrames:
            if self.movie.frameCount() > 0:
                self.frameSlider.setMaximum(self.movie.frameCount() - 1)
            # 加上一层保护
            elif self.movie.currentFrameNumber() > self.frameSlider.maximum():
                self.frameSlider.setMaximum(self.movie.currentFrameNumber())
        else:
            self.frameSlider.setMaximum(0)

    def slot_open(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, 'Open a GIF', self.currentDirectory)
        if fileName:
            self.openFile(fileName)

    def slot_updateButtons(self):
        self.pauseButton.setChecked(self.movie.state() == QMovie.Paused)
        self.stopButton.setEnabled(self.movie.state() != QMovie.NotRunning)

    def slot_pause(self, bPause):
        self.movie.setPaused(bPause)
        if bPause:
            self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.pauseButton.setToolTip('Play')
        else:
            self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.pauseButton.setToolTip('Pause')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())
