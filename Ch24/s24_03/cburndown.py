# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy
from PyQt5.QtCore import pyqtSignal
from Ch24.s24_03.config import *
from Ch24.s24_03.cprojectinfo import *
import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import MultipleLocator
from Ch24.s24_03.ui_burndown import *


class CWidgetBurndown(QWidget, Ui_CWidgetBurndown):
    m_nSprintIndex = -1
    fig = Figure(figsize=(10, 10), dpi=100)
    axes = None
    m_pPlotBurnDown = None
    sig_getBackToSprint = pyqtSignal()

    def __init__(self, parent=None):
        super(CWidgetBurndown, self).__init__(parent)
        self.setupUi(self)
        self.initialize()
        self.btnGetback.clicked.connect(self.sig_getBackToSprint)

    def clear(self):
        self.label_projectName.setText("")
        self.label_sprintNo.setText("")

    # x = []
    # y = []
    # self.m_pPlotBurnDown.plot(x, y)

    def setSprintInfo(self, strProjectCode, sprintId):
        self.clear()
        self.m_strProjectCode = strProjectCode
        self.m_nSprintIndex = sprintId
        self.label_sprintNo.setText(self.tr("Sprint:%d" % (self.m_nSprintIndex)))
        sql_query = QSqlQuery()
        strSql = "select name from projects where code=\'%s\'" % (strProjectCode)
        if sql_query.exec(strSql):
            if sql_query.next():
                strName = sql_query.value(0)
                self.label_projectName.setText(strName)
        self.load(self.m_strProjectCode, self.m_nSprintIndex)

    def initialize(self):
        self.label_projectName.setText("")
        config = CConfig()
        strStyleSheet = config.getStyleSheetA()
        gridLayout_15 = QGridLayout(self.widget)
        gridLayout_15.setObjectName("gridLayout_15")
        # 建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.fig = Figure(figsize=(10, 10), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.axes.grid('on')
        self.m_pPlotBurnDown = FigureCanvas(self.fig)
        self.m_pPlotBurnDown.setParent(self.widget)
        self.m_pPlotBurnDown.setSizePolicy(
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.m_pPlotBurnDown.setObjectName("graphicsView_burnDown")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHeightForWidth(self.m_pPlotBurnDown.sizePolicy().hasHeightForWidth())
        self.m_pPlotBurnDown.setSizePolicy(sizePolicy1)
        self.m_pPlotBurnDown.setStyleSheet(strStyleSheet)
        gridLayout_15.addWidget(self.m_pPlotBurnDown, 0, 0, 1, 1)

    def load(self, strProjectCode, sprintId):
        self.setBurnDown(self.m_pPlotBurnDown, strProjectCode, sprintId)

    def setBurnDown(self, pCustomPlot, strProjectCode, nSprintCycle):
        # 获取指定项目的当前迭代
        currentSprint = CProjectInfo.getCurrentSprint(strProjectCode)
        nSprintDays = nSprintCycle * 5
        # 获取指定项目当前迭代的燃尽图数据
        nCount, lstDate, lstData = CProjectInfo.getBurndownData(strProjectCode, currentSprint)
        s = lstData
        # 设定右上角图形标注隐藏
        # pCustomPlot.legend.setVisible(False)
        min = 99999
        max = 0
        nData = 0
        for nData in s:
            if nData > max:
                max = nData
            if nData < min:
                min = nData
        if min > 0:
            min = 0
        max += 5
        x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
        y_major_locator = MultipleLocator(10)  # 把y轴的刻度间隔设置为10, 并存在变量里
        # ax = pCustomPlot.gca()#ax为两条坐标轴的实例
        self.axes.xaxis.set_major_locator(x_major_locator)  # 把x轴的主刻度设置为1的倍数
        self.axes.yaxis.set_major_locator(y_major_locator)  # 把y轴的主刻度设置为10的倍数
        # pCustomPlot.xlim(0.5, nSprintDays)#把x轴的刻度范围设置为-0.5到nSprintDays，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
        # pCustomPlot.ylim(min-5, max)#把y轴的刻度范围设置为min-5到max，同理，-5不会标出来，但是能看到一点空白
        # 设置X轴文字标注
        self.axes.set_xlabel("date")  # xlabel、ylabel：分别设置X、Y轴的标题文字
        # 设置Y轴文字标注
        self.axes.set_ylabel(self.tr("workload"))
        #	pCustomPlot.set_title(self.tr("burndown curve"), fontsize=24) # 设置图的标题
        # 传入数据
        t = range(0, nCount)
        self.axes.plot(t, s)
