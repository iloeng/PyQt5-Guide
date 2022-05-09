# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlError, QSqlQuery
from PyQt5.QtGui import QPainter, QPaintEvent, QBrush, QFont
from PyQt5.QtWidgets import QMessageBox, QWidget, QSpacerItem, QSizePolicy, QGridLayout
from PyQt5.QtCore import QDate, QPointF, pyqtSignal, QSize
from Ch24.s24_03.config import *
from Ch24.s24_03.ctask import *
from Ch24.s24_03.customwidget import *
from Ch24.s24_03.cbacklog import *
from Ch24.s24_03.ui_sprint import *

c_startRow = 4


class CWidgetSprint(QWidget, Ui_CWidgetSprint):
    m_strProjectCode = str()
    m_nSprintIndex = 0
    m_nIndex = c_startRow
    sig_getBack = pyqtSignal()
    sig_burndown = pyqtSignal(str, int)

    def __init__(self, id, parent=None):
        super(CWidgetSprint, self).__init__(parent)
        self.setupUi(self)
        self.m_nSprintIndex = id
        config = CConfig()
        # 样式
        strStyleSheetLeft = config.getStyleSheetLeftDark()
        strStyleSheetRight = config.getStyleSheetRightDark()
        strStyleSheetBase = config.getStyleSheetBaseDark()
        self.frame_2.setStyleSheet(strStyleSheetLeft)
        self.frame_7.setStyleSheet(strStyleSheetBase)
        self.frame_10.setStyleSheet(strStyleSheetRight)
        self.label_sprintNo.setText("Sprint:{0}".format(self.m_nSprintIndex))
        self.btnAddBacklog.clicked.connect(self.slot_addBacklog)
        self.btnGetback.clicked.connect(self.sig_getBack)
        self.btnFinish.clicked.connect(self.slot_finish)
        self.btnBurndown.clicked.connect(self.slot_showBurndown)

    def slot_finish(self):
        # 作业:
        #     根据backlog的完成情况，更新burdown表中本次迭代的燃尽图数据
        pass

    def slot_showBurndown(self):
        self.sig_burndown.emit(self.m_strProjectCode, self.m_nSprintIndex)

    def slot_addBacklog(self):
        config = CConfig()
        if not config.isAuthorized():
            QMessageBox.information(self, self.tr("task"), self.tr("please login"))
            return
        sql_query = QSqlQuery()
        sql_query.prepare("insert into backlogs(projectcode,sprintid,workloade,workloadr,state) "
                          " values(:projectcode,:sprintid,:workloade,:workloadr,:state)")
        sql_query.bindValue(":projectcode", self.m_strProjectCode)
        sql_query.bindValue(":sprintid", self.m_nSprintIndex)
        sql_query.bindValue(":workloade", 1)
        sql_query.bindValue(":workloadr", 1)
        sql_query.bindValue(":state", 1)
        if sql_query.exec_():
            print(sql_query.lastError().text())
        self.initialize()

    def clear(self):
        pLayoutItem = None
        for r in range(c_startRow, self.gridLayout.rowCount()):
            for c in range(0, self.gridLayout.columnCount()):
                pLayoutItem = self.gridLayout.itemAtPosition(r, c)
                if pLayoutItem is None:
                    continue
                pWidget = pLayoutItem.widget()
                if pWidget is None:
                    continue
                self.gridLayout.removeWidget(pWidget)

    def initialize(self):
        self.clear()
        sql_query = QSqlQuery()
        strSql = "select id from backlogs where projectcode=\'%s\' and sprintid=%d" % (
            self.m_strProjectCode, self.m_nSprintIndex)
        # print(strSql)
        lstValues = []
        if sql_query.exec(strSql):
            while sql_query.next():
                lstValues.append(sql_query.value(0))
        for value in lstValues:
            self.add(value)

    def setSprintInfo(self, strProjectCode, sprintId):
        self.m_strProjectCode = strProjectCode
        self.m_nSprintIndex = sprintId
        self.label_sprintNo.setText(self.tr("Sprint:%d" % (self.m_nSprintIndex)))
        sql_query = QSqlQuery()
        strSql = "select name from projects where code=\'%s\'" % (strProjectCode)
        if sql_query.exec(strSql):
            if sql_query.next():
                strName = sql_query.value(0)
                self.label_projectName.setText(strName)

    def add(self, nBacklogId):
        strBacklogId = "%d" % (nBacklogId)
        strBacklog = str()
        dtStart = QDate()
        dtEnd = QDate()
        strTask = str()
        sql_query = QSqlQuery()
        nEstimateWorkload = 0
        strSql = "select backlog,workloade from backlogs where id=%d" % (nBacklogId)
        # print(strSql)
        if sql_query.exec(strSql):
            if sql_query.first():
                strBacklog = sql_query.value(0)
                nEstimateWorkload = sql_query.value(1)
            else:
                return
        else:
            print(sql_query.lastError().text())
            return
        config = CConfig()
        # 样式
        stStyleSheetLeft = config.getStyleSheetLeftDark()
        stStyleSheetRight = config.getStyleSheetRightDark()
        stStyleSheetBase = config.getStyleSheetBaseDark()
        stStyleSheet = config.getStyleSheetB()
        ft = QFont()
        ft.setPointSizeF(18)
        # backlog
        widgetbase_Backlog = CCustomWidget(self)
        widgetbase_Backlog.setObjectName(strBacklogId + "_" + "widgetbase_Backlog")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widgetbase_Backlog.sizePolicy().hasHeightForWidth())
        widgetbase_Backlog.setSizePolicy(sizePolicy)
        widgetbase_Backlog.setMaximumSize(QSize(600, 16667777))
        widgetbase_Backlog.setStyleSheet(stStyleSheetBase)
        gridLayout_11 = QGridLayout(widgetbase_Backlog)
        gridLayout_11.setObjectName("gridLayout_11")
        backlogText = CWidgetBacklog(self.m_strProjectCode, nBacklogId, ETaskState.ETaskState_Todo,
                                     widgetbase_Backlog)
        backlogText.setEstimateWorkload(nEstimateWorkload)
        backlogText.setBacklog(strBacklog)
        backlogText.setObjectName("backlogText")
        sizePolicy.setHeightForWidth(backlogText.sizePolicy().hasHeightForWidth())
        backlogText.setSizePolicy(sizePolicy)
        backlogText.setStyleSheet(stStyleSheet)
        gridLayout_11.addWidget(backlogText, 0, 0, 1, 1)
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        gridLayout_11.addItem(verticalSpacer, 1, 0, 1, 1)
        self.gridLayout.addWidget(widgetbase_Backlog, self.m_nIndex, 0, 1, 1)
        backlogText.sig_saved.connect(self.initialize)
        backlogText.sig_taskAdded.connect(self.initialize)
        # tasks - Doing
        widgetbase_Task = CCustomWidget(self)
        widgetbase_Task.setObjectName(strBacklogId + "_" + "widgetbase_Task")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(widgetbase_Task.sizePolicy().hasHeightForWidth())
        widgetbase_Task.setSizePolicy(sizePolicy1)
        widgetbase_Task.setMaximumSize(QSize(600, 16667777))
        widgetbase_Task.setStyleSheet(stStyleSheetBase)
        gridLayout_12 = QGridLayout(widgetbase_Task)
        gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout.addWidget(widgetbase_Task, self.m_nIndex, 1, 1, 1)
        nId = 0
        nEstimateWorkload = 0
        strDeveloper = str()
        strSql = "select id, task, workloade, developer from tasks where projectcode=\'%s\' and backlogid=%d and  state=%d" % (
            self.m_strProjectCode, nBacklogId, ETaskState.ETaskState_Doing)
        # print(strSql)
        index = 0
        if sql_query.exec(strSql):
            while sql_query.next():
                nId = sql_query.value(0)
                strTask = sql_query.value(1)
                nEstimateWorkload = sql_query.value(2)
                strDeveloper = sql_query.value(3)
                taskWidget = CWidgetTask(ETaskState.ETaskState_Doing, widgetbase_Task)
                taskWidget.setId(nId)
                taskWidget.setEstimateWorkload(nEstimateWorkload)
                taskWidget.setTask(strTask)
                taskWidget.setDeveloper(strDeveloper)
                taskWidget.setObjectName("taskWidget")
                taskWidget.setStyleSheet(stStyleSheet)
                gridLayout_12.addWidget(taskWidget, index, 0, 1, 1)
                index += 1
                taskWidget.sig_refresh.connect(self.initialize)
            verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            gridLayout_12.addItem(verticalSpacer, index, 0, 1, 1)
        # tasks - Finished
        widgetbase_TaskFinished = CCustomWidget(self)
        widgetbase_TaskFinished.setObjectName(strBacklogId + "_" + "widgetbase_TaskFinished")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(widgetbase_TaskFinished.sizePolicy().hasHeightForWidth())
        widgetbase_TaskFinished.setSizePolicy(sizePolicy2)
        widgetbase_TaskFinished.setMaximumSize(QSize(600, 16667777))
        widgetbase_TaskFinished.setStyleSheet(stStyleSheetBase)
        gridLayout_13 = QGridLayout(widgetbase_TaskFinished)
        gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout.addWidget(widgetbase_TaskFinished, self.m_nIndex, 2, 1, 1)
        #
        backlogTextFinished = CWidgetBacklog(self.m_strProjectCode, nBacklogId,
                                             ETaskState.ETaskState_Finished, widgetbase_Backlog)
        backlogTextFinished.setEstimateWorkload(nEstimateWorkload)
        backlogTextFinished.setBacklog(strBacklog)
        backlogTextFinished.setObjectName("backlogText")
        sizePolicy.setHeightForWidth(backlogText.sizePolicy().hasHeightForWidth())
        backlogTextFinished.setSizePolicy(sizePolicy)
        backlogTextFinished.setStyleSheet(stStyleSheet)
        gridLayout_13.addWidget(backlogTextFinished, 0, 0, 1, 1)
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        gridLayout_13.addItem(verticalSpacer, 1, 0, 1, 1)
        # 华丽的分割线
        line = QFrame(self)
        line.setObjectName("line")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(line, self.m_nIndex + 1, 0, 1, 3)
        self.m_nIndex += 2
