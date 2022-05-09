# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlError, QSqlQuery
from PyQt5.QtGui import QPainter, QPaintEvent, QBrush, QPixmap
from PyQt5.QtWidgets import QMessageBox, QFrame
from PyQt5.QtCore import QPointF, QByteArray, pyqtSignal
from Ch24.s24_03.config import *
from Ch24.s24_03.ui_task import *
from enum import IntEnum, Enum


# 各个状态的枚举
class ETaskState(IntEnum):
    ETaskState_Todo = 0
    ETaskState_Doing = 1
    ETaskState_Finished = 2


class CWidgetTask(QFrame, Ui_CWidgetTask):
    m_nEstimateWorkload = 0
    m_nBacklogId = -1
    m_nId = -1
    m_nState = 0
    m_strTask = str()
    m_strDeveloper = str()
    sig_refresh = pyqtSignal()
    sig_enter = pyqtSignal(str)
    sig_leave = pyqtSignal(str)

    def __init__(self, eState, parent=None):
        super(CWidgetTask, self).__init__(parent)
        self.setupUi(self)
        m_nState = eState
        if ETaskState.ETaskState_Todo == eState:
            self.btnFinished.hide()
        elif ETaskState.ETaskState_Doing == eState:
            self.btnAccept.hide()
            self.btnSave.hide()
        elif ETaskState.ETaskState_Finished == eState:
            self.btnSave.hide()
            self.btnAccept.hide()
            self.btnFinished.hide()
        self.btnSave.clicked.connect(self.slot_save)
        self.btnAccept.clicked.connect(self.slot_accept)
        self.btnFinished.clicked.connect(self.slot_finish)

    def enterEvent(self, event):
        QFrame.enterEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到编号
        tStr = tStr[0:idx]
        self.sig_enter.emit(tStr)

    def leaveEvent(self, event):
        QFrame.leaveEvent(self, event)
        tStr = self.objectName()
        idx = tStr.find("_")  # 找到编号
        tStr = tStr[0:idx]
        self.sig_leave.emit(tStr)

    def setId(self, id):
        self.m_nId = id
        self.labelTask.setText(self.tr("task:%d" % (id)))

    def setEstimateWorkload(self, days):
        self.m_nEstimateWorkload = days
        self.leEstimatedWorkload.setText("%d" % (days))

    def setTask(self, tStr):
        self.m_strTask = tStr
        self.pleTask.setPlainText(tStr)

    def slot_save(self):
        config = CConfig()
        self.m_strDeveloper = config.getUser()
        if not len(self.m_strDeveloper):
            QMessageBox.information(self, self.tr("task"), self.tr("please login"))
            return
        self.save()
        self.sig_refresh.emit()

    def save(self):
        strTask = self.pleTask.toPlainText()
        self.m_nEstimateWorkload = int(self.leEstimatedWorkload.text())
        # print(strTask)
        sql_query = QSqlQuery()
        strSql = "update tasks set task=:task, workloade=:workloade where id=:id"
        sql_query.prepare(strSql)
        sql_query.bindValue(":task", strTask)  # backlog
        sql_query.bindValue(":workloade", self.m_nEstimateWorkload)  # 估计工作量
        sql_query.bindValue(":id", self.m_nId)  # id
        sql_query.exec_()  # 插入记录

    # print(sql_query.lastError().text())

    def slot_accept(self):
        config = CConfig()
        self.m_strDeveloper = config.getUser()
        if not len(self.m_strDeveloper):
            QMessageBox.information(self, self.tr("task"), self.tr("please login"))
            return
        self.save()
        sql_query = QSqlQuery()
        strSql = "update tasks set state=:state, developer=:developer where id=:id"
        sql_query.prepare(strSql)
        sql_query.bindValue(":state", int(ETaskState.ETaskState_Doing))  # state
        sql_query.bindValue(":developer", self.m_strDeveloper)  # developer
        sql_query.bindValue(":id", self.m_nId)  # id
        sql_query.exec_()  # 执行
        self.sig_refresh.emit()

    def setDeveloper(self, strDeveloper):
        self.m_strDeveloper = strDeveloper
        byteArray = QByteArray()
        sql_query = QSqlQuery()
        strSql = "select photo from users where name = \'"
        strSql += strDeveloper
        strSql += "\'"
        # print(strSql)
        if sql_query.exec(strSql):
            if sql_query.first():
                byteArray = sql_query.value(0)
            else:
                print(sql_query.lastError().text())
        else:
            print(sql_query.lastError().text())
        pixmap = QPixmap()
        pixmap.loadFromData(byteArray)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(self.labelDeveloper.width(), self.labelDeveloper.height())
        self.labelDeveloper.setPixmap(pixmap)
        self.sig_refresh.emit()

    def slot_finish(self):
        sql_query = QSqlQuery()
        strSql = "update tasks set state=:state where id=:id"
        sql_query.prepare(strSql)
        sql_query.bindValue(":state", int(ETaskState.ETaskState_Finished))  # backlog
        sql_query.bindValue(":id", self.m_nId)  # id
        sql_query.exec_()  # 插入记录
        self.sig_refresh.emit()

    def slot_back(self):
        self.sig_refresh.emit()
