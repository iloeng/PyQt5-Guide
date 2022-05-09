# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlError, QSqlQuery
from PyQt5.QtCore import pyqtSignal
from Ch24.s24_03.config import *
from Ch24.s24_03.cuser import *
from Ch24.s24_03.ui_projectinfo import *


class CProjectInfo(QWidget, Ui_CProjectInfo):
    m_bModify = False
    sig_getBack = pyqtSignal()

    def __init__(self, parent=None):
        super(CProjectInfo, self).__init__(parent)
        self.setupUi(self)
        self.initialize()
        self.btnSave.clicked.connect(self.slot_save)
        self.btnGetback.clicked.connect(self.sig_getBack)

    def setModifyMode(self, b):
        self.m_bModify = b
        if b:
            self.btnSave.setText(tr("save"))
        else:
            self.btnSave.setText(tr("add"))

    def initialize(self):
        users = CWidgetUser()
        strList = users.getUsers()
        for tStr in strList:
            self.cbProductOwner.addItem(tStr)
            self.cbScrumMaster.addItem(tStr)
            self.cbTest.addItem(tStr)

    def getProjects(self):
        strList = []
        sql_query = QSqlQuery()
        strSql = "select code from projects"
        if sql_query.exec(strSql):
            while sql_query.next():
                strName = sql_query.value(0)
                strList.append(strName)
        else:
            print(sql_query.lastError().text())
        return strList

    def getCurrentSprint(strProjectCode):
        nCurrentSprint = 0
        sql_query = QSqlQuery()
        strSql = "select currentsprint from projects where code = \'"
        strSql += strProjectCode
        strSql += "\'"
        # print(strSql)
        if sql_query.exec(strSql):
            if sql_query.first():
                nCurrentSprint = sql_query.value(0)
        else:
            print(sql_query.lastError().text())
        return nCurrentSprint

    def getSprintCycle(self, strProjectCode):
        nSprintCycle = 0
        sql_query = QSqlQuery()
        strSql = "select sprintcycle from projects where code = \'"
        strSql += strProjectCode
        strSql += "\'"
        ''' print(strSql) '''
        if sql_query.exec(strSql):
            if sql_query.first():
                nSprintCycle = sql_query.value(0)
        else:
            print(sql_query.lastError().text())
        return nSprintCycle

    def getBurndownData(strProjectCode, sprintId):
        lstDate = []
        lstData = []
        sql_query = QSqlQuery()
        strSql = "select date,workload from burndown where projectcode = \'"
        strSql += strProjectCode
        strSql += "\' and sprintid="
        strSql += "%d" % (sprintId)
        strSql += " order by date"
        # print(strSql)
        nData = 0
        if sql_query.exec(strSql):
            while sql_query.next():
                lstDate.append(sql_query.value(0))
                nData = sql_query.value(1)
                lstData.append(nData)
        else:
            print(sql_query.lastError().text())
        return len(lstDate), lstDate, lstData

    def clear(self):
        self.leProjectCode.setText("")
        self.leProjectName.setText("")
        self.leEstimatedWorkload.setText("1")
        self.cbProductOwner.setCurrentIndex(-1)
        self.cbScrumMaster.setCurrentIndex(-1)
        self.cbTest.setCurrentIndex(-1)
        self.spinBoxSprintCycle.setValue(2)
        self.leDevelopTeam.setText("")

    def slot_save(self):
        strProjectCode = self.leProjectCode.text()
        strProjectName = self.leProjectName.text()
        dtStart = self.dtStart.date()
        dtEnd = self.dtEnd.date()
        nEstimatedWorkload = int(self.leEstimatedWorkload.text())
        nCurrentSprint = int(self.leCurrentSprint.text())
        strProductOwner = self.cbProductOwner.currentText()
        strScrumMaster = self.cbScrumMaster.currentText()
        strTester = self.cbTest.currentText()
        nSprintCycle = self.spinBoxSprintCycle.value()
        strDevelopTeam = self.leDevelopTeam.text()
        sql_query = QSqlQuery()
        strSql = "select name from projects where code=\'"
        strSql += strProjectCode
        strSql += "\'"
        self.m_bModify = False
        if sql_query.exec(strSql):
            if sql_query.first():
                self.m_bModify = True
        if self.m_bModify:
            sql_query.prepare(
                "update projects set name=:name,startdate=:startdate,enddate=:enddate,currentsprint=:currentsprint,sprintcycle=:sprintcycle,workloade=:workloade,po=:po,sm=:sm,tester=:tester,devteam=:devteam where code=:code")
            sql_query.bindValue(":name", strProjectName)
            sql_query.bindValue(":startdate", dtStart.toString())
            sql_query.bindValue(":enddate", dtEnd.toString())
            sql_query.bindValue(":currentsprint", nCurrentSprint)
            sql_query.bindValue(":sprintcycle", nSprintCycle)
            sql_query.bindValue(":workloade", nEstimatedWorkload)
            sql_query.bindValue(":po", strProductOwner)
            sql_query.bindValue(":sm", strScrumMaster)
            sql_query.bindValue(":tester", strTester)
            sql_query.bindValue(":devteam", strDevelopTeam)
            sql_query.bindValue(":code", strProjectCode)
        else:
            sql_query.prepare(
                "insert into projects (name,code,startdate,enddate,currentsprint,sprintcycle,workloade,po,sm,tester,devteam) "
                "values (:name,:code,:startdate,:enddate,:currentsprint,:sprintcycle,:workloade,:po,:sm,:tester,:devteam)")
            sql_query.bindValue(":name", strProjectName)
            sql_query.bindValue(":code", strProjectCode)
            sql_query.bindValue(":startdate", dtStart.toString())
            sql_query.bindValue(":enddate", dtEnd.toString())
            sql_query.bindValue(":currentsprint", 1)
            sql_query.bindValue(":sprintcycle", nSprintCycle)
            sql_query.bindValue(":workloade", nEstimatedWorkload)
            sql_query.bindValue(":po", strProductOwner)
            sql_query.bindValue(":sm", strScrumMaster)
            sql_query.bindValue(":tester", strTester)
            sql_query.bindValue(":devteam", strDevelopTeam)
        sql_query.exec_()  # 插入记录
        if sql_query.exec_():  # 插入记录
            QMessageBox.information(self, self.tr("projectinfo"),
                                    self.tr("operation finished successfully."))
        else:
            QMessageBox.information(self, self.tr("projectinfo"), sql_query.lastError.text())
