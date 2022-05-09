# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlQuery, QSqlError
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, QFile, QByteArray
import os
from Ch24.s24_03.ui_user import *


class CWidgetUser(QWidget, Ui_CWidgetUser):
    m_bModify = False
    sig_getBack = pyqtSignal()

    def __init__(self, parent=None):
        super(CWidgetUser, self).__init__(parent)
        self.setupUi(self)
        self.btnSave.clicked.connect(self.slot_save)
        self.btnSelectPhoto.clicked.connect(self.slot_selectphoto)
        self.btnGetback.clicked.connect(self.sig_getBack)

    def setModifyMode(self, b):
        self.m_bModify = b
        if b:
            self.btnSave.setText(self.tr("save"))
        else:
            self.btnSave.setText(self.tr("add"))

    def clear(self):
        self.leId.setText("")
        self.leName.setText("")
        self.lePassword.setText("")
        self.label_photo.setPixmap(QPixmap())

    def getUsers(self):
        strList = []
        strName = str()
        sql_query = QSqlQuery()
        strSql = "select name from users"
        if sql_query.exec(strSql):
            while sql_query.next():
                strName = sql_query.value(0)
                strList.append(strName)
        else:
            print(sql_query.lastError().text())
        return strList

    def loadUser(self, strUser):
        id = 0
        strName = str()
        strPassword = str()
        byteArray = QByteArray()
        sql_query = QSqlQuery()
        strSql = f"select id,name,password,role,photo from users where name={strUser}"
        if sql_query.exec(strSql):
            role = 0
            if sql_query.first():
                id = sql_query.value(0)
                strName = sql_query.value(1)
                strPassword = sql_query.value(2)
                role = sql_query.value(3)
                byteArray = sql_query.value(4)
            else:
                print(sql_query.lastError().text())
        else:
            print(sql_query.lastError().text())
        strId = "%d" % (id)
        self.leId.setText(strId)
        self.leName.setText(strName)
        self.lePassword.setText(strPassword)
        # print("loadUser:password:" + strPassword)
        pixmap = QPixmap()
        pixmap.loadFromData(byteArray)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(self.label_photo.width(), self.label_photo.height())
        self.label_photo.setPixmap(pixmap)

    def slot_selectphoto(self):
        self.m_strFileName = ""
        trainDevHome = os.getenv('TRAINDEVHOME')
        if None is trainDevHome:
            trainDevHome = 'usr/local/gui'
        strDir = trainDevHome + '/test/chapter24/ks24_03/'
        strFilter = str("picture(*.png *.jpg)")
        fileName, _ = QFileDialog.getOpenFileName(self, self.tr("select file to open"), strDir,
                                                  strFilter)
        if not len(fileName):
            return
        file = QFile(fileName)
        if not file.open(QFile.ReadOnly):
            return
        self.m_strFileName = fileName
        pixmap = QPixmap(fileName)
        pixmap = pixmap.scaled(self.label_photo.width(), self.label_photo.height())
        self.label_photo.setPixmap(pixmap)

    def slot_save(self):
        strName = self.leName.text()
        strPassword = self.lePassword.text()
        byteArray = QByteArray()
        file = QFile(self.m_strFileName)
        if file.open(QFile.ReadOnly):
            byteArray = file.readAll()
        sql_query = QSqlQuery()
        # print("slot_save : password=" + strPassword)
        if self.m_bModify:
            strSql = "update users set password = :password, photo=:photo where name = \'"
            strSql += strName
            strSql += "\'"
            sql_query.prepare(strSql)
            sql_query.bindValue(":password", strPassword)  # 密码
            sql_query.bindValue(":photo", byteArray)  # 照片
        else:
            sql_query.prepare("insert into users (name, password,photo) "
                              "values (:name, :password, :photo)")
            sql_query.bindValue(":name", strName)  # 名字
            sql_query.bindValue(":password", strPassword)  # 密码
            sql_query.bindValue(":photo", byteArray)  # 照片
        if sql_query.exec_():  # 插入记录
            QMessageBox.information(self, self.tr("adduser"),
                                    self.tr("operation finished successfully."))
        else:
            QMessageBox.information(self, self.tr("adduser"), sql_query.lastError.text())
