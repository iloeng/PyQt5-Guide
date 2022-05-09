# -*- coding: utf-8 -*-
'''
案例代码
'''
import matplotlib
from PyQt5.QtWidgets import QSizePolicy

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


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
