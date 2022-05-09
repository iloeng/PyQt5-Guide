# -*- coding: utf-8 -*-
"""
案例代码
"""

import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QSizePolicy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Ch24.s24_02.ui_dialog import *

matplotlib.use("Qt5Agg")  # 声明使用QT5


class CustomFigureCanvas(FigureCanvas):
    """CustomFigureCanvas是一个窗口部件，即QWidget, 也是FigureCanvasAgg"""

    def __init__(self, parent=None, width=10, height=10, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        # 建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = fig.add_subplot(111)
        self.axes.grid('on')
        # 调用父类的初始化接口
        super(CustomFigureCanvas, self).__init__(fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 更新控件的尺寸
        # FigureCanvas.updateGeometry(self)
        # self.updateGeometry()
        # 生成图表用的数据
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)


class CDialog(QDialog, Ui_CDialog):
    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('matplotlib')

        layout = QVBoxLayout(self.widget)
        customFig = CustomFigureCanvas(self.widget)
        figToolbar = NavigationToolbar(customFig, self)
        layout.addWidget(customFig)
        layout.addWidget(figToolbar)
