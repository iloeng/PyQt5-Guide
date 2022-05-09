# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlError, QSqlQuery
from PyQt5.QtGui import QPainter, QPaintEvent, QBrush
from PyQt5.QtWidgets import QMessageBox, QGridLayout
from PyQt5.QtCore import QPointF, pyqtSignal
from Ch24.s24_03.config import *
from Ch24.s24_03.ctask import *
from Ch24.s24_03.ui_backlog import *


class CWidgetBacklog(QFrame, Ui_CWidgetBacklog):
    m_strProjectCode = str()
    m_nEstimateWorkload = 0
    m_nId = -1
    m_eState = ETaskState.ETaskState_Todo
    sig_saved = pyqtSignal()
    sig_taskAdded = pyqtSignal()
    sig_enter = pyqtSignal(str)
    sig_leave = pyqtSignal(str)
    sig_pressed = pyqtSignal(str)

    def __init__(self, strProjectCode, backlogId, eState, parent=None):
        super(CWidgetBacklog, self).__init__(parent)
        self.setupUi(self)
        self.m_strProjectCode = strProjectCode
        self.m_nId = backlogId
        self.m_eState = eState
        self.initialize()
        self.btnSave.clicked.connect(self.slot_save)
        self.btnAddTask.clicked.connect(self.slot_addTask)

    def initialize(self):
        if ETaskState.ETaskState_Finished == self.m_eState:
            self.btnSave.hide()
            self.btnAddTask.hide()

        self.labelBacklog.setText(self.tr("backlog:%d" % (self.m_nId)))
        config = CConfig()
        stStyleSheet = config.getStyleSheetB()
        nId = 0
        nEstimateWorkload = 0
        sql_query = QSqlQuery()
        strSql = "select id, task, workloade, developer from tasks where projectcode=\'%s\' and backlogid=%d and state=%d" % (
            self.m_strProjectCode, self.m_nId, self.m_eState)
        # print(strSql)
        index = 0
        gridLayout_1 = QGridLayout(self.frameTasks)
        gridLayout_1.setObjectName("gridLayout_1")
        if sql_query.exec(strSql):
            while sql_query.next():
                nId = sql_query.value(0)
                strTask = sql_query.value(1)
                nEstimateWorkload = sql_query.value(2)
                strDeveloper = sql_query.value(3)
                taskWidget = CWidgetTask(self.m_eState, self.frameTasks)
                taskWidget.setId(nId)
                taskWidget.setEstimateWorkload(nEstimateWorkload)
                taskWidget.setTask(strTask)
                taskWidget.setDeveloper(strDeveloper)
                taskWidget.setObjectName("taskWidget")
                taskWidget.setStyleSheet(stStyleSheet)
                gridLayout_1.addWidget(taskWidget, index, 0, 1, 1)
                index += 1
                taskWidget.sig_refresh.connect(self.sig_taskAdded)

    def slot_addTask(self):
        config = CConfig()
        strDeveloper = config.getUser()
        if not len(strDeveloper):
            QMessageBox.information(self, self.tr("task"), self.tr("please login"))
            return
        sql_query = QSqlQuery()
        sql_query.prepare(
            "insert into tasks(task,projectcode,backlogid,developer,workloade,workloadr,state) "
            " values(\'\', :projectcode,:backlogid,:developer,:workloade,:workloadr,:state)")
        sql_query.bindValue(":projectcode", self.m_strProjectCode)
        sql_query.bindValue(":backlogid", self.m_nId)
        sql_query.bindValue(":developer", "")
        sql_query.bindValue(":workloade", 1)
        sql_query.bindValue(":workloadr", 1)
        sql_query.bindValue(":state", int(ETaskState.ETaskState_Todo))
        if not sql_query.exec_():
            print(sql_query.lastError().text())
        self.sig_taskAdded.emit()

    def slot_save(self):
        config = CConfig()
        strDeveloper = config.getUser()
        if not len(strDeveloper):
            QMessageBox.information(self, self.tr("task"), self.tr("please login"))
            return
        strBacklog = self.pleBacklog.toPlainText()
        self.m_nEstimateWorkload = self.leEstimatedWorkload.text()
        sql_query = QSqlQuery()
        strSql = "update backlogs set backlog=:backlog, workloade=:workloade where id=:id"
        sql_query.prepare(strSql)
        sql_query.bindValue(":backlog", strBacklog)  # backlog
        sql_query.bindValue(":workloade", self.m_nEstimateWorkload)  # 估计工作量
        sql_query.bindValue(":id", self.m_nId)  # id
        if not sql_query.exec_():
            print(sql_query.lastError().text())
        self.sig_saved.emit()

    def setBacklog(self, tStr):
        self.m_strBacklog = tStr
        self.pleBacklog.setPlainText(tStr)

    def setProjectCode(self, strProjectCode):
        self.m_strProjectCode = strProjectCode

    def setEstimateWorkload(self, days):
        self.m_nEstimateWorkload = days
        self.leEstimatedWorkload.setText("%d" % (days))

    def setId(self, id):
        self.m_nId = id
        self.labelBacklog.setText(self.tr("backlog:%d" % (id)))

    def enterEvent(self, event):
        QFrame.enterEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]

    #	self.sig_enter.emit(tStr)

    def leaveEvent(self, event):
        QFrame.leaveEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]

    #	self.sig_leave.emit(tStr)

    def mousePressEvent(self, event):
        QFrame.mousePressEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到项目编号
        tStr = tStr[0:idx]
        self.sig_pressed.emit(tStr)
