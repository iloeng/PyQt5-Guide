# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from PyQt5.QtGui import QPainter, QPaintEvent, QBrush
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGridLayout, QDialog, QDialogButtonBox, QLineEdit, QMessageBox
from Ch24.s24_03.ui_logindialog import *


class CLoginDialog(QDialog, Ui_CLoginDialog):
    m_bAuthorized = False

    def __init__(self, parent=None):
        super(CLoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.slot_accept)
        self.buttonBox.rejected.connect(self.reject)
        # 设置密码的echoMode
        self.lePassword.setEchoMode(QLineEdit.Password)
        self.lePassword.setPlaceholderText("please input password.")

    ''' 获取用户 '''

    def getUser(self):
        return self.leName.text()

    ''' 授权是否有效 '''

    def isAuthorized(self):
        return self.m_bAuthorized

    ''' 槽函数-接受 '''

    def slot_accept(self):
        if self.varify():
            self.accept()
        else:
            QMessageBox.information(self, "login", "invalid password")

    ''' 验证授权 '''

    def varify(self):
        self.m_bAuthorized = False
        strName = self.leName.text()
        sql_query = QSqlQuery()
        strSql = "select password from users where name=\'"
        strSql += strName
        strSql += "\'"
        if not sql_query.exec(strSql):
            print(sql_query.lastError().text())
            return False
        if not sql_query.first():
            return False
        strPassword = sql_query.value(0)
        if strPassword == self.lePassword.text():
            self.m_bAuthorized = True
            return True
        else:
            return False
