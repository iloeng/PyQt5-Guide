# -*- coding: utf-8 -*-
'''
案例代码
'''

from PyQt5.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from PyQt5.QtCore import QDateTime, pyqtSignal
from Ch24.s24_03.cuser import *
from Ch24.s24_03.config import *
from Ch24.s24_03.ui_addsprint import *


class CWidgetAddSprint(QWidget, Ui_CWidgetAddSprint):
    m_bModify = False
    sig_getBack = pyqtSignal()

    def __init__(self, parent=None):
        super(CWidgetAddSprint, self).__init__(parent)
        self.setupUi(self)
        self.btnSave.clicked.connect(self.slot_save)
        self.btnGetback.clicked.connect(self.sig_getBack)

    def clear(self):
        self.leProjectCode.setText("")
        self.leCurrentSprint.setText("1")
        self.leEstimatedWorkload.setText("1")
        self.dtStart.setDate(QDateTime.currentDateTime().date())
        self.dtEnd.setDate(QDateTime.currentDateTime().date())

    def slot_save(self):
        strProjectCode = self.leProjectCode.text()
        nCurrentSprint = int(self.leCurrentSprint.text())
        dtStart = self.dtStart.date()
        dtEnd = self.dtEnd.date()
        nEstimatedWorkload = int(self.leEstimatedWorkload.text())
        sql_query = QSqlQuery()
        sql_query.prepare("insert into sprints (projectcode,id, startdate,enddate,workloade) "
                          "values (:projectcode,:id, :startdate,:enddate,:workloade)")
        sql_query.bindValue(":projectcode", strProjectCode)
        sql_query.bindValue(":id", nCurrentSprint)
        sql_query.bindValue(":startdate", dtStart.toString())
        sql_query.bindValue(":enddate", dtEnd.toString())
        sql_query.bindValue(":workloade", nEstimatedWorkload)
        sql_query.exec_()  # 插入记录
# print(sql_query.lastError())
