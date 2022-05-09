# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from PyQt5.QtCore import QDir
import os
import types


class CSingleton(type):
    _instance = None

    def __call__(self, *args, **kw):
        if self._instance is None:
            self._instance = super().__call__(*args, **kw)
        return self._instance


def singleton(cls, *args, **kwargs):
    instances = {}

    def wrapper():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class CConfig():
    m_bAuthorized = False
    m_database = None
    m_strUser = str()
    m_styleSheetLeftDark = 'QWidget{background-color:rgb(17, 149, 189);border-top-left-radius:5px;border-bottom-left-radius:5px;border:1px solid black}'
    m_styleSheetRightDark = 'background-color:rgb(17, 149, 189);border-top-right-radius:5px;border-bottom-right-radius:5px;border-width:1px; border-style:solid'
    m_styleSheetBaseDark = 'background-color:rgb(17, 149, 189);border-width:1px;border-style:solid'
    m_styleSheetLeft = 'background-color: rgb(17, 149, 189);border-top-left-radius:5px;border-bottom-left-radius:5px;border-width:1px;border-style:dashed'
    m_styleSheetRight = 'background-color: rgb(17, 149, 189);border-top-right-radius:5px;border-bottom-right-radius:5px;border-width:1px;border-style:dashed'
    m_styleSheetBase = 'background-color:rgb(17, 149, 189);border-width:1px;border-style:dashed'
    m_styleSheetA = 'background-color: rgb(255, 255, 255);border-radius:5px;border:1px'
    m_styleSheetB = "background-color: rgb(255, 255, 255)"

    def __init__(self):
        # 创建并打开数据库
        self.m_database = QSqlDatabase.addDatabase("QSQLITE")
        strFile = "ks24_03_database.dbfile"
        self.m_database.setDatabaseName(strFile)
        self.m_database.setUserName("admin")  # 数据库用户名
        self.m_database.setPassword("admin")  # 数据库密码
        bOpen = self.m_database.open()
        if not bOpen:
            print("Error: Failed to add database." + self.m_database.lastError().text())
        else:
            print("Info: Succeed to add database.")

    ''' 获取左侧控件样式 '''

    def getStyleSheetLeft(self):
        return self.m_styleSheetLeft

    ''' 获取左侧控件样式 '''

    def getStyleSheetLeftDark(self):
        return self.m_styleSheetLeftDark

    ''' 获取右侧控件样式 '''

    def getStyleSheetRight(self):
        return self.m_styleSheetRight

    ''' 获取右侧控件样式 '''

    def getStyleSheetRightDark(self):
        return self.m_styleSheetRightDark

    ''' 获取基准控件样式 '''

    def getStyleSheetBase(self):
        return self.m_styleSheetBase

    ''' 获取基准控件样式 '''

    def getStyleSheetBaseDark(self):
        return self.m_styleSheetBaseDark

    ''' 获取普通控件样式A '''

    def getStyleSheetA(self):
        return self.m_styleSheetA

    ''' 获取普通控件样式B '''

    def getStyleSheetB(self):
        return self.m_styleSheetB

    ''' 连接到数据库 '''

    def connectToDatabase(self):
        pass

    # self.m_database.open()

    ''' 设置标志：是否已登录 '''

    def setAuthorized(self, b):
        self.m_bAuthorized = b

    ''' 是否已登录 '''

    def isAuthorized(self):
        return self.m_bAuthorized

    ''' 设置登录人员 '''

    def setUser(self, strUser):
        self.m_strUser = strUser

    ''' 获取登录人员 '''

    def getUser(self):
        return self.m_strUser
