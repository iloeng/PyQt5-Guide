# -*- coding: utf-8 -*-
'''
案例代码
'''
from PyQt5.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from PyQt5.QtGui import QPaintEvent, QBrush, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QStackedLayout, QAction, QMenu
from PyQt5.QtCore import QPointF, QPropertyAnimation, QEasingCurve, QPoint, QByteArray, Qt
from Ch24.s24_03.cprojects import *
from Ch24.s24_03.cprojectinfo import *
from Ch24.s24_03.cburndown import *
from Ch24.s24_03.config import *
from Ch24.s24_03.cuser import *
from Ch24.s24_03.csprint import *
from Ch24.s24_03.caddsprint import *
from Ch24.s24_03.clogindialog import *
from Ch24.s24_03.ui_mainwidget import *


class CMainWidget(QWidget, Ui_CMainWidget):
    m_pMenu = None  # 主菜单
    m_pProjectBrowserAct = None  # 项目总览
    m_pAddProjectAct = None  # 添加项目
    m_pAddSprintAct = None  # 添加迭代
    m_pAddUserAct = None  # 添加人员
    m_pModifyPasswordAct = None  # 修改密码
    m_pAboutAct = None  # 关于
    m_pExitAct = None  # 退出
    m_pInfoLabel = None  # 信息标签
    m_pAnimaMenuShow = None  # 菜单动画
    m_bShowMenu = True  # 显示菜单
    m_pWidgetProjects = None  # 主窗体
    m_pStackedLayout = None  # 布局对象
    m_pWidgetProjectInfo = None  # 项目信息界面
    m_pWidgetUser = None  # 人员界面
    m_pWidgetSprint = None  # 迭代界面
    m_pWidgetAddSprint = None  # 添加迭代界面
    m_pWidgetBurndown = None  # 燃尽图界面

    def __init__(self, parent=None):
        super(CMainWidget, self).__init__(parent)
        self.setupUi(self)
        self.initialize()
        self.createActions()
        self.createMenus()
        self.connectSignalAndSlot()
        self.setWindowTitle(self.tr("Scrum Bulletin Board"))
        self.setMinimumSize(160, 160)
        self.showMaximized()

    def initialize(self):
        ''' 初始化数据库 '''
        self.initialize_database()
        # self.btnLogin.setIconSize(self.btnLogin.size())
        ''' 构建项目一览控件 '''
        self.m_pWidgetProjects = CWidgetProjects(self)
        ''' 构建项目信息界 '''
        self.m_pWidgetProjectInfo = CProjectInfo(self)
        ''' 构建人员界面 '''
        self.m_pWidgetUser = CWidgetUser(self)
        ''' 构建迭代界面 '''
        self.m_pWidgetSprint = CWidgetSprint(1, self)
        ''' 构建添加迭代界面 '''
        self.m_pWidgetAddSprint = CWidgetAddSprint(self)
        ''' 构建燃尽图界面 '''
        self.m_pWidgetBurndown = CWidgetBurndown(self)
        ''' 构建QStackedLayout布局对象 '''
        self.m_pStackedLayout = QStackedLayout(self.widget)
        ''' 将子面对象添加到堆栈布局 '''
        self.m_pStackedLayout.addWidget(self.m_pWidgetProjects)  # 0
        self.m_pStackedLayout.addWidget(self.m_pWidgetProjectInfo)  # 1
        self.m_pStackedLayout.addWidget(self.m_pWidgetUser)  # 2
        self.m_pStackedLayout.addWidget(self.m_pWidgetSprint)  # 3
        self.m_pStackedLayout.addWidget(self.m_pWidgetAddSprint)  # 4
        self.m_pStackedLayout.addWidget(self.m_pWidgetBurndown)  # 5
        ''' 设置默认页 '''
        self.m_pStackedLayout.setCurrentIndex(0)
        self.widget.setLayout(self.m_pStackedLayout)

    def connectSignalAndSlot(self):
        self.btnMenu.clicked.connect(self.slot_menu)
        self.btnLogin.clicked.connect(self.slot_login)
        self.m_pWidgetUser.sig_getBack.connect(self.slot_getBack)
        self.m_pWidgetProjectInfo.sig_getBack.connect(self.slot_getBack)
        self.m_pWidgetProjects.sig_pressed.connect(self.slot_pressedProject)
        self.m_pWidgetAddSprint.sig_getBack.connect(self.slot_getBack)
        self.m_pWidgetSprint.sig_getBack.connect(self.slot_getBack)
        self.m_pWidgetSprint.sig_burndown.connect(self.slot_showBurndown)
        self.m_pWidgetBurndown.sig_getBackToSprint.connect(self.slot_getBackToSprint)

    def about(self):
        self.m_pInfoLabel.setText(self.r("Invoked <b>Help|About</b>"))

    def createActions(self):
        ''' file operation action '''
        self.m_pProjectBrowserAct = QAction(self.tr("projectBrowser"), self)
        self.m_pProjectBrowserAct.setStatusTip(self.tr("projectBrowser"))
        self.m_pProjectBrowserAct.triggered.connect(self.slot_projectBrowser)

        self.m_pAddProjectAct = QAction(self.tr("addProject"), self)
        self.m_pAddProjectAct.setStatusTip(self.tr("addProject"))
        self.m_pAddProjectAct.triggered.connect(self.slot_addProject)

        self.m_pAddSprintAct = QAction(self.tr("addSprint"), self)
        self.m_pAddSprintAct.setStatusTip(self.tr("addSprint"))
        self.m_pAddSprintAct.triggered.connect(self.slot_addSprint)

        # file operation action
        self.m_pAddUserAct = QAction(self.tr("addUser"), self)
        self.m_pAddUserAct.setStatusTip(self.tr("addUser"))
        self.m_pAddUserAct.triggered.connect(self.slot_addUser)

        self.m_pModifyPasswordAct = QAction(self.tr("modifyUser"), self)
        self.m_pModifyPasswordAct.setStatusTip(self.tr("modifyUser"))
        self.m_pModifyPasswordAct.triggered.connect(self.slot_changePassword)

        self.m_pAboutAct = QAction(self.tr("about"), self)
        self.m_pAboutAct.setStatusTip(self.tr("about"))
        self.m_pAboutAct.triggered.connect(self.slot_about)

        self.m_pExitAct = QAction(self.tr("exit"), self)
        self.m_pExitAct.setStatusTip(self.tr("exit"))
        self.m_pExitAct.triggered.connect(self.slot_exit)

    def createMenus(self):
        self.m_pMenu = QMenu(self.tr("&File"), self)
        self.m_pMenu.setMouseTracking(True)  # 接收鼠标事件
        styleSheet = '''QMenu{border:1px solid black;color:black}
						QMenu::hover{border:1px solid black;background-color:lightgray}
						QMenu::pressed{border:1px solid black;background-color:gray}'''
        self.m_pMenu.setStyleSheet(styleSheet)
        ''' flag设置为tool和无边框，消除qmenu的popup效果 '''
        self.m_pMenu.setWindowFlags(Qt.CustomizeWindowHint | Qt.Tool | Qt.FramelessWindowHint)
        self.m_pMenu.addAction(self.m_pProjectBrowserAct)
        self.m_pMenu.addAction(self.m_pAddProjectAct)
        self.m_pMenu.addAction(self.m_pAddSprintAct)
        self.m_pMenu.addAction(self.m_pAddUserAct)
        self.m_pMenu.addAction(self.m_pModifyPasswordAct)
        self.m_pMenu.addAction(self.m_pAboutAct)
        self.m_pMenu.addAction(self.m_pExitAct)

    def slot_menu(self):
        s_MenubarHeight = self.btnMenu.mapToGlobal(self.btnMenu.pos()).y() + self.btnMenu.height()
        s_MenuWidth = self.m_pMenu.width()
        if None == self.m_pAnimaMenuShow:
            self.m_pAnimaMenuShow = QPropertyAnimation(self.m_pMenu, b"pos", self)
            self.m_pAnimaMenuShow.finished.connect(self.slot_animationMenuFinished)
            self.m_pAnimaMenuShow.setDuration(400)
            self.m_pAnimaMenuShow.setEasingCurve(QEasingCurve.Linear)

        if self.m_bShowMenu:  # 单击时弹出菜单
            self.m_pMenu.show()
            offsetY = s_MenubarHeight
            self.m_pAnimaMenuShow.setStartValue(
                QPoint(self.x() + self.width(), self.y() + offsetY))
            self.m_pAnimaMenuShow.setEndValue(
                QPoint(self.x() + self.width() - s_MenuWidth, self.y() + offsetY))
            self.m_pAnimaMenuShow.start()

        else:  # 再次单击时隐藏菜单
            offsetY = s_MenubarHeight
            self.m_pAnimaMenuShow.setStartValue(
                QPoint(self.x() + self.width() - s_MenuWidth, self.y() + offsetY))
            self.m_pAnimaMenuShow.setEndValue(QPoint(self.x() + self.width(), self.y() + offsetY))
            self.m_pAnimaMenuShow.start()

    def slot_animationMenuFinished(self):
        if not self.m_bShowMenu:
            self.m_pMenu.hide()

        self.m_bShowMenu = not self.m_bShowMenu

    def slot_addUser(self):
        self.m_pWidgetUser.clear()
        self.m_pStackedLayout.setCurrentIndex(2)
        self.m_pWidgetUser.setModifyMode(False)
        self.slot_animationMenuFinished()

    def slot_changePassword(self):
        config = CConfig()
        strDeveloper = config.getUser()
        if not config.isAuthorized():
            self.slot_animationMenuFinished()
            QMessageBox.information(self, self.tr("task"), self.tr("please login"))
            return

        self.m_pStackedLayout.setCurrentIndex(2)
        self.m_pWidgetUser.setModifyMode(True)
        self.m_pWidgetUser.loadUser(strDeveloper)
        self.slot_animationMenuFinished()

    def updateLoginIcon(self):
        icon = QIcon()
        config = CConfig()
        strDeveloper = config.getUser()
        if not config.isAuthorized():
            icon = QIcon(":/images/login.png")
            self.btnLogin.setIcon(icon)
            return
        byteArray = QByteArray()
        sql_query = QSqlQuery()
        strSql = "select photo from users where name = \'"
        strSql += config.getUser()
        strSql += "\'"
        if sql_query.exec(strSql):
            # int role = 0
            if sql_query.first():
                byteArray = sql_query.value(0)
            else:
                print(sql_query.lastError().text())
        else:
            print(sql_query.lastError().text())

        pixmap = QPixmap()
        pixmap.loadFromData(byteArray)
        icon = QIcon()
        if not pixmap.isNull():
            icon = pixmap.scaled(self.btnLogin.width(), self.btnLogin.height())
        self.btnLogin.setIcon(QIcon(icon))

    def slot_addProject(self):
        config = CConfig()
        if not config.isAuthorized():
            self.slot_animationMenuFinished()
            QMessageBox.information(self, self.tr("task"), self.tr("please login"))
            return
        self.m_pStackedLayout.setCurrentIndex(1)
        self.m_pWidgetProjectInfo.initialize()
        self.slot_animationMenuFinished()

    def slot_addSprint(self):
        config = CConfig()
        if not config.isAuthorized():
            self.slot_animationMenuFinished()
            QMessageBox.information(self, self.tr("task"), self.tr("please login"))
            return
        self.m_pStackedLayout.setCurrentIndex(4)
        self.m_pWidgetSprint.initialize()
        self.slot_animationMenuFinished()

    def slot_login(self):
        dlg = CLoginDialog(self)
        dlg.exec()
        config = CConfig()
        config.setAuthorized(dlg.isAuthorized())
        config.setUser(dlg.getUser())
        self.updateLoginIcon()

    def slot_about(self):
        QMessageBox.information(self, self.tr("Agile"), self.tr("Scrum Bulletin Board"))
        self.slot_animationMenuFinished()

    def slot_exit(self):
        self.close()

    def slot_getBack(self):
        self.m_pStackedLayout.setCurrentIndex(0)

    def slot_getBackToSprint(self):
        self.m_pStackedLayout.setCurrentIndex(3)

    def slot_showBurndown(self, strProjectCode, sprintId):
        self.m_pWidgetBurndown.setSprintInfo(strProjectCode, sprintId)
        self.m_pStackedLayout.setCurrentIndex(5)

    def slot_projectBrowser(self):
        self.m_pStackedLayout.setCurrentIndex(0)
        self.slot_animationMenuFinished()

    def initialize_database(self):
        config = CConfig()
        # 创建表
        # 创建项目表
        sql_query = QSqlQuery()
        if not sql_query.exec(
                "create table if not exists projects(id integer primary key autoincrement, name text unique, code text unique,startdate text, enddate text, sprintcycle int default 1, workloade  integer default 0,workloadfinished integer default 1, po text, sm text, tester text,currentsprint integer, devteam text)"):
            print(sql_query.lastError().text())
        # 创建人员表
        if not sql_query.exec(
                "create table if not exists users(id integer primary key autoincrement, name text unique, password text, role int, photo blob)"):
            print(sql_query.lastError().text())
        # 创建迭代表
        if not sql_query.exec(
                "create table if not exists sprints( id integer primary key autoincrement, projectcode text, startdate text, enddate text, workloade integer, completion_date text)"):
            print(sql_query.lastError().text())
        # 创建燃尽图表
        if not sql_query.exec(
                "create table if not exists burndown(projectcode text, sprintid integer, date text, workload integer)"):
            print(sql_query.lastError().text())
        # 创建待办事项表
        if not sql_query.exec(
                "create table if not exists backlogs(id integer primary key autoincrement, projectcode text, sprintid integer, backlog text, workloade int, workloadr integer, state integer, info text)"):
            print(sql_query.lastError().text())
        # 创建分解任务表
        if not sql_query.exec(
                "create table if not exists tasks(id integer primary key autoincrement, task text default \'\', projectcode text,  backlogid integer, developer text, workloade integer, workloadr integer, state integer default 0)"):
            print(sql_query.lastError().text())

    def slot_pressedProject(self, strProjectCode):
        nSprintId = 1
        self.m_pWidgetSprint.setSprintInfo(strProjectCode, nSprintId)
        self.m_pWidgetSprint.initialize()
        # 找到项目的当前迭代，初始化后显示。
        self.m_pStackedLayout.setCurrentIndex(3)
