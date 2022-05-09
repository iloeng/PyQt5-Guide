# -*- coding: utf-8 -*-
'''
案例代码
'''
import sys
from PyQt5.QtSql import QSqlError, QSqlQuery
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QSizePolicy
from PyQt5.QtCore import QDate, pyqtSignal, QSize
from Ch24.s24_03.config import *
from Ch24.s24_03.cprojectinfo import *
from Ch24.s24_03.custombar import *
from Ch24.s24_03.customlabel import *
from Ch24.s24_03.customwidget import *
from Ch24.s24_03.ctask import *
from Ch24.s24_03.ui_projects import *
import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import MultipleLocator


class CWidgetProjects(QWidget, Ui_CWidgetProjects):
    m_nProjectIndex = 3
    sig_getBack = pyqtSignal()
    sig_pressed = pyqtSignal(str)
    axes = None

    def __init__(self, parent=None):
        super(CWidgetProjects, self).__init__(parent)
        self.setupUi(self)
        config = CConfig()
        # 样式
        strStyleSheetLeft = config.getStyleSheetLeftDark()
        strStyleSheetRight = config.getStyleSheetRightDark()
        strStyleSheetBase = config.getStyleSheetBaseDark()
        self.frame_ProjectName.setStyleSheet(strStyleSheetLeft)
        self.frame_timeProgress.setStyleSheet(strStyleSheetBase)
        self.frame_workloadProgress.setStyleSheet(strStyleSheetBase)
        self.frame_sprintCycle.setStyleSheet(strStyleSheetBase)
        self.frame_burnDownChart.setStyleSheet(strStyleSheetRight)

        # 华丽的分割线
        line = QFrame(self)
        line.setObjectName("line")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(line, 2, 0, 1, 5)

        projectsinfo = CProjectInfo()
        strList = projectsinfo.getProjects()
        for string in strList:
            self.add(string)

    def getFinishedWorkload(strProjectCode):
        finishedWorkLoad = 0
        sql_query = QSqlQuery()
        strSql = "select workloadfinished from projects where code='"
        strSql += strProjectCode
        strSql += "\'"
        # print(strSql)
        if sql_query.exec(strSql):
            if sql_query.first():
                finishedWorkLoad = sql_query.value(0)
                if finishedWorkLoad == '':
                    finishedWorkLoad = 0
        return finishedWorkLoad

    def add(self, strProjectCode):
        dtStart = QDate()
        dtEnd = QDate()
        nEstimatedWorkload = 0
        finishedWorkLoad = CWidgetProjects.getFinishedWorkload(strProjectCode)
        strProductOwner = str()
        strScrumMaster = str()
        strTester = str()
        nSprintCycle = 1
        strDevelopTeam = str()
        sql_query = QSqlQuery()
        strSql = "select name,startdate,enddate,sprintcycle,workloade,po,sm,tester,devteam from projects where code='"
        strSql += strProjectCode
        strSql += "\'"
        # print(strSql)
        if sql_query.exec(strSql):
            if sql_query.first():
                strProjectName = sql_query.value(0)
                dtStart = QDate.fromString(sql_query.value(1))
                dtEnd = QDate.fromString(sql_query.value(2))
                nSprintCycle = sql_query.value(3)
                nEstimatedWorkload = sql_query.value(4)
                strProductOwner = sql_query.value(5)
                strScrumMaster = sql_query.value(6)
                strTester = sql_query.value(7)
                strDevelopTeam = sql_query.value(8)
            else:
                return
        else:
            print(sql_query.lastError().text())
            return
        config = CConfig()
        # 样式
        strStyleSheetLeft = config.getStyleSheetLeft()
        strStyleSheetRight = config.getStyleSheetRight()
        strStyleSheetBase = config.getStyleSheetBase()
        strStyleSheet = config.getStyleSheetA()
        string = str()
        ft = QFont()
        ft.setPointSizeF(18)
        # 项目名称
        widgetbase_ProjectName = CCustomWidget(self)
        widgetbase_ProjectName.setObjectName(strProjectCode + "_" + "widgetbaseProjectName")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetbase_ProjectName.sizePolicy().hasHeightForWidth())
        widgetbase_ProjectName.setSizePolicy(sizePolicy)
        widgetbase_ProjectName.setMaximumSize(QSize(16777215, 100))
        widgetbase_ProjectName.setStyleSheet(strStyleSheetLeft)
        gridLayout_11 = QGridLayout(widgetbase_ProjectName)
        gridLayout_11.setObjectName(strProjectCode + "_" + "gridLayout11")
        projectName = CCustomLabel(widgetbase_ProjectName)
        projectName.setText(strProjectName)
        projectName.setObjectName(strProjectCode + "_" + "projectName")
        sizePolicy.setHeightForWidth(projectName.sizePolicy().hasHeightForWidth())
        projectName.setSizePolicy(sizePolicy)
        projectName.setStyleSheet(strStyleSheet)
        projectName.setAlignment(Qt.AlignCenter)
        projectName.setFont(ft)
        gridLayout_11.addWidget(projectName, 0, 0, 1, 1)
        self.gridLayout.addWidget(widgetbase_ProjectName, self.m_nProjectIndex, 0, 1, 1)
        widgetbase_ProjectName.sig_enter.connect(self.slot_enterProject)
        widgetbase_ProjectName.sig_leave.connect(self.slot_leaveProject)
        widgetbase_ProjectName.sig_pressed.connect(self.sig_pressed)
        projectName.sig_pressed.connect(self.sig_pressed)
        # 项目的时间进度
        widgetbase_timeProgress = CCustomWidget(self)
        widgetbase_timeProgress.setObjectName(strProjectCode + "_" + "widgetbasetimeProgress")
        widgetbase_timeProgress.setMaximumSize(QSize(150, 16777215))
        widgetbase_timeProgress.setStyleSheet(strStyleSheetBase)
        gridLayout_12 = QGridLayout(widgetbase_timeProgress)
        gridLayout_12.setObjectName(strProjectCode + "_" + "gridLayout12")
        gridLayout_12.setHorizontalSpacing(7)
        # 项目启动日期
        projectStartDate = CCustomLabel(widgetbase_timeProgress)
        projectStartDate.setObjectName(strProjectCode + "_" + "projectStartDate")
        projectStartDate.setMaximumSize(QSize(80, 30))
        projectStartDate.setStyleSheet(strStyleSheet)
        string = "{0}/{1}".format(dtStart.year(), dtStart.month())
        projectStartDate.setText(string)
        gridLayout_12.addWidget(projectStartDate, 0, 0, 1, 1)
        widgetbase_timeProgress.sig_enter.connect(self.slot_enterProject)
        widgetbase_timeProgress.sig_leave.connect(self.slot_leaveProject)
        widgetbase_timeProgress.sig_pressed.connect(self.sig_pressed)
        projectStartDate.sig_pressed.connect(self.sig_pressed)
        # 项目结束日期
        projectEndDate = CCustomLabel(widgetbase_timeProgress)
        projectEndDate.setObjectName(strProjectCode + "_" + "projectEndDate")
        projectEndDate.setMaximumSize(QSize(80, 16777215))
        projectEndDate.setStyleSheet(strStyleSheet)
        string = "{0}/{1}".format(dtEnd.year(), dtEnd.month())
        projectEndDate.setText(string)
        gridLayout_12.addWidget(projectEndDate, 0, 1, 1, 1)
        projectEndDate.sig_pressed.connect(self.sig_pressed)
        # 项目进度棒图
        graphicsView_timeProgress = CCustomBar(widgetbase_timeProgress)
        graphicsView_timeProgress.setObjectName(strProjectCode + "_" + "graphicsViewtimeProgress")
        sizePolicy.setHeightForWidth(graphicsView_timeProgress.sizePolicy().hasHeightForWidth())
        graphicsView_timeProgress.setSizePolicy(sizePolicy)
        graphicsView_timeProgress.setMaximumSize(QSize(150, 30))
        graphicsView_timeProgress.setStyleSheet(strStyleSheet)
        gridLayout_12.addWidget(graphicsView_timeProgress, 1, 0, 1, 2)
        self.gridLayout.addWidget(widgetbase_timeProgress, self.m_nProjectIndex, 1, 1, 1)
        dtNow = QDate.currentDate()
        graphicsView_timeProgress.setValue(0, dtStart.daysTo(dtEnd), dtStart.daysTo(dtNow))
        # 项目的工作量进度
        widgetbase_workloadProgress = CCustomWidget(self)
        widgetbase_workloadProgress.setObjectName(
            strProjectCode + "_" + "widgetbaseworkloadProgress")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHeightForWidth(widgetbase_workloadProgress.sizePolicy().hasHeightForWidth())
        widgetbase_workloadProgress.setSizePolicy(sizePolicy1)
        widgetbase_workloadProgress.setMaximumSize(QSize(300, 16777215))
        widgetbase_workloadProgress.setStyleSheet(strStyleSheetBase)
        gridLayout_13 = QGridLayout(widgetbase_workloadProgress)
        gridLayout_13.setObjectName(strProjectCode + "_" + "gridLayout13")
        workloadProgress = CCustomLabel(widgetbase_workloadProgress)
        workloadProgress.setObjectName(strProjectCode + "_" + "workloadProgress")
        workloadProgress.setMinimumSize(QSize(0, 0))
        workloadProgress.setMaximumSize(QSize(300, 30))
        string = self.tr("Estimated:%d man-day,finished:%d") % (
        nEstimatedWorkload, finishedWorkLoad)
        workloadProgress.setText(string)
        workloadProgress.setStyleSheet(strStyleSheet)
        gridLayout_13.addWidget(workloadProgress, 0, 0, 1, 1)
        # 项目的工作量图示
        graphicsView_workloadProgress = CCustomBar(widgetbase_workloadProgress)
        graphicsView_workloadProgress.setObjectName(
            strProjectCode + "_" + "graphicsViewworkloadProgress")
        sizePolicy.setHeightForWidth(
            graphicsView_workloadProgress.sizePolicy().hasHeightForWidth())
        graphicsView_workloadProgress.setSizePolicy(sizePolicy)
        graphicsView_workloadProgress.setMaximumSize(QSize(16777215, 30))
        graphicsView_workloadProgress.setStyleSheet(strStyleSheet)
        gridLayout_13.addWidget(graphicsView_workloadProgress, 1, 0, 1, 1)
        self.gridLayout.addWidget(widgetbase_workloadProgress, self.m_nProjectIndex, 2, 1, 1)
        graphicsView_workloadProgress.setValue(0, nEstimatedWorkload, finishedWorkLoad)
        widgetbase_workloadProgress.sig_enter.connect(self.slot_enterProject)
        widgetbase_workloadProgress.sig_leave.connect(self.slot_leaveProject)
        widgetbase_workloadProgress.sig_pressed.connect(self.sig_pressed)
        # 项目迭代周期
        widgetbase_sprintCycle = CCustomWidget(self)
        widgetbase_sprintCycle.setObjectName(strProjectCode + "_" + "widgetbasesprintCycle")
        widgetbase_sprintCycle.setStyleSheet(strStyleSheetBase)
        gridLayout_14 = QGridLayout(widgetbase_sprintCycle)
        gridLayout_14.setObjectName(strProjectCode + "_" + "gridLayout14")
        sprintCycle = CCustomLabel(widgetbase_sprintCycle)
        sprintCycle.setObjectName(strProjectCode + "_" + "sprintCycle")
        sprintCycle.setStyleSheet(strStyleSheet)
        sprintCycle.setAlignment(Qt.AlignCenter)
        sprintCycle.setText("%d Weeks" % (nSprintCycle))
        gridLayout_14.addWidget(sprintCycle, 0, 0, 1, 1)
        self.gridLayout.addWidget(widgetbase_sprintCycle, self.m_nProjectIndex, 3, 1, 1)
        widgetbase_sprintCycle.sig_enter.connect(self.slot_enterProject)
        widgetbase_sprintCycle.sig_leave.connect(self.slot_leaveProject)
        # 项目燃尽图
        widgetbase_burnDownChart = CCustomWidget(self)
        widgetbase_burnDownChart.setObjectName(strProjectCode + "_" + "widgetbaseburnDownChart")
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(widgetbase_burnDownChart.sizePolicy().hasHeightForWidth())
        widgetbase_burnDownChart.setSizePolicy(sizePolicy1)
        widgetbase_burnDownChart.setMaximumSize(QSize(100, 100))
        widgetbase_burnDownChart.setStyleSheet(strStyleSheetRight)
        gridLayout_15 = QGridLayout(widgetbase_burnDownChart)
        gridLayout_15.setObjectName(strProjectCode + "_" + "gridLayout15")

        fig = Figure(figsize=(10, 10), dpi=100)
        # 建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = fig.add_subplot(111)
        self.axes.grid('on')
        pPlot_burnDown = FigureCanvas(fig)
        pPlot_burnDown.setObjectName(strProjectCode + "_" + "plotburnDown")
        sizePolicy1.setHeightForWidth(pPlot_burnDown.sizePolicy().hasHeightForWidth())
        pPlot_burnDown.setSizePolicy(sizePolicy1)
        pPlot_burnDown.setStyleSheet(strStyleSheet)
        gridLayout_15.addWidget(pPlot_burnDown, 0, 0, 1, 1)
        self.gridLayout.addWidget(widgetbase_burnDownChart, self.m_nProjectIndex, 4, 1, 1)
        self.setBurnDown(pPlot_burnDown, strProjectCode, nSprintCycle)
        widgetbase_burnDownChart.sig_enter.connect(self.slot_enterProject)
        widgetbase_burnDownChart.sig_leave.connect(self.slot_leaveProject)
        widgetbase_burnDownChart.sig_pressed.connect(self.sig_pressed)
        # 华丽的分割线
        line = QFrame(self)
        line.setObjectName(strProjectCode + "_" + "line")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(line, self.m_nProjectIndex + 1, 0, 1, 5)
        self.m_nProjectIndex += 2

    def slot_enterProject(self, strProjectCode):
        config = CConfig()
        strStyleSheetLeft = config.getStyleSheetLeftDark()
        strStyleSheetRight = config.getStyleSheetRightDark()
        strStyleSheetBase = config.getStyleSheetBaseDark()
        objList = self.children()
        for childObject in objList:
            strName = childObject.objectName()
            if strName.find(strProjectCode) != 0:
                continue
            if strName.find("widgetbaseProjectName") >= 0:
                childObject.setStyleSheet(strStyleSheetLeft)
            elif strName.find("widgetbase_burnDownChart") >= 0:
                childObject.setStyleSheet(strStyleSheetRight)
            else:
                childObject.setStyleSheet(strStyleSheetBase)

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

    def slot_leaveProject(self, strProjectCode):
        config = CConfig()
        strStyleSheetLeft = config.getStyleSheetLeft()
        strStyleSheetRight = config.getStyleSheetRight()
        strStyleSheetBase = config.getStyleSheetBase()
        objList = self.children()
        for childObject in objList:
            strName = childObject.objectName()
            if strName.find(strProjectCode) != 0:
                continue
            if strName.find("widgetbaseProjectName") >= 0:
                childObject.setStyleSheet(strStyleSheetLeft)
            elif strName.find("widgetbase_burnDownChart") >= 0:
                childObject.setStyleSheet(strStyleSheetRight)
            else:
                childObject.setStyleSheet(strStyleSheetBase)
