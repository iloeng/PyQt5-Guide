# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QAction, QLabel, QFrame, QMessageBox, QGraphicsScene
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QRectF, QPointF
from Ch21.s21_02.splashscreen import CSplashScreen
from Ch21.s21_02.mdiarea import CEditMdiArea


class CMainWindow(QMainWindow):
    fileMenu = None  # 文件菜单
    editMenu = None  # 编辑菜单
    helpMenu = None  # 帮助菜单
    alignmentGroup = None  # 对齐菜单项组
    newAct = None  # 【新建】子菜单
    openAct = None  # 【打开】子菜单
    saveAct = None  # 【保存】子菜单
    exitAct = None  # 【退出】子菜单
    cutAct = None  # 【剪切】子菜单
    copyAct = None  # 【拷贝】子菜单
    pasteAct = None  # 【粘贴】子菜单
    ellipseAct = None  # 【添加椭圆】
    rectAct = None  # 【添加矩形】
    aboutAct = None  # 【帮助】子菜单
    infoLabel = None  # 信息标签
    fileToolBar = None  # 【文件】工具条
    editToolBar = None  # 【编辑】工具条
    mouseLabel = None  # 显示鼠标位置的标签
    sig_progress = pyqtSignal(int)
    mdiArea = None  # 多窗口管理对象

    def __init__(self, splashScreen, parent=None):
        super(CMainWindow, self).__init__(parent)
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.sig_progress.connect(splashScreen.slot_setProgress)
        self.initialize()
        self.setWindowTitle('MDI')
        self.setMinimumSize(160, 160)
        self.resize(480, 320)

    def initialize(self):
        # 构建视图对象
        self.mdiArea = CEditMdiArea(self)
        self.setCentralWidget(self.mdiArea)
        self.connectSignalAndSlot()

    # 模拟构造过程中的耗时操作
    def readData(self):
        self.sig_progress.emit(100)
        return
        QThread.sleep(1)  # 模拟耗时操作
        self.sig_progress.emit(10)

        QThread.sleep(1)
        self.sig_progress.emit(30)

        QThread.sleep(1)
        self.sig_progress.emit(50)

        QThread.sleep(1)
        self.sig_progress.emit(70)

        QThread.sleep(1)
        self.sig_progress.emit(100)

    def slot_addRect(self):
        self.mdiArea.addRect()

    def slot_addEllipse(self):
        self.mdiArea.addEllipse()

    def slot_new(self):
        self.infoLabel.setText('Invoked <b>File|New</b>')
        self.mdiArea.new()

    def slot_open(self):
        self.infoLabel.setText('Invoked <b>File|Open</b>')
        self.mdiArea.open()

    def slot_save(self):
        self.infoLabel.setText('Invoked <b>File|Save</b>')

    def slot_cut(self):
        self.infoLabel.setText('Invoked <b>Edit|Cut</b>')
        self.mdiArea.cut()

    def slot_copy(self):
        self.infoLabel.setText('Invoked <b>Edit|Copy</b>')
        self.mdiArea.copy()

    def slot_paste(self):
        self.infoLabel.setText('Invoked <b>Edit|Paste</b>')
        self.mdiArea.paste()

    def slot_about(self):
        self.infoLabel.setText('Invoked <b>Help|About</b>')
        QMessageBox.about(self,
                          'About Menu',
                          'The <b>Menu</b> example shows how to create menu-bar menus and context menus.')

    def createActions(self):
        self.newAct = QAction(QIcon(':/images/new.png'), '新建...', self)
        self.newAct.setShortcuts(QKeySequence.New)
        self.newAct.setStatusTip('New file')
        self.newAct.triggered.connect(self.slot_new)

        self.openAct = QAction(QIcon(':/images/open.png'), '打开...', self)
        self.openAct.setShortcuts(QKeySequence.Open)
        self.openAct.setStatusTip('Open an existing file')
        self.openAct.triggered.connect(self.slot_open)

        self.saveAct = QAction('保存', self)
        self.saveAct.setShortcuts(QKeySequence.Save)
        self.saveAct.setStatusTip('Save the document to disk')
        self.saveAct.triggered.connect(self.slot_save)

        self.exitAct = QAction('退出', self)
        self.exitAct.setShortcuts(QKeySequence.Quit)
        self.exitAct.setStatusTip('Exit the application')
        self.exitAct.triggered.connect(self.close)

        self.cutAct = QAction('剪切', self)
        self.cutAct.setShortcuts(QKeySequence.Cut)
        self.cutAct.setStatusTip("Cut the current selection's contents to the clipboard")
        self.cutAct.triggered.connect(self.slot_cut)

        self.copyAct = QAction('复制', self)
        self.copyAct.setShortcuts(QKeySequence.Copy)
        self.copyAct.setStatusTip("Copy the current selection's contents to the clipboard")
        self.copyAct.triggered.connect(self.slot_copy)

        self.pasteAct = QAction('粘贴', self)
        self.pasteAct.setShortcuts(QKeySequence.Paste)
        self.pasteAct.setStatusTip("Paste the clipboard's contents into the current selection")
        self.pasteAct.triggered.connect(self.slot_paste)

        self.rectAct = QAction('添加矩形', self)
        self.rectAct.setStatusTip("add rect to view")
        self.rectAct.triggered.connect(self.slot_addRect)

        self.ellipseAct = QAction('添加椭圆', self)
        self.ellipseAct.setStatusTip("add ellipse to view")
        self.ellipseAct.triggered.connect(self.slot_addEllipse)

        self.aboutAct = QAction('关于', self)
        self.aboutAct.setStatusTip("Show the application's About box")
        self.aboutAct.triggered.connect(self.slot_about)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('文件')
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)

        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu('编辑')
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)
        self.editMenu.addAction(self.rectAct)
        self.editMenu.addAction(self.ellipseAct)
        self.editMenu.addSeparator()

        self.helpMenu = self.menuBar().addMenu('帮助')
        self.helpMenu.addAction(self.aboutAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar('文件工具条')
        self.fileToolBar.setObjectName('file toolbar')
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)
        self.editToolBar = self.addToolBar('编辑工具条')
        self.editToolBar.setObjectName("edit toolbar")
        self.editToolBar.addAction(self.cutAct)
        self.editToolBar.addAction(self.copyAct)
        self.editToolBar.addAction(self.pasteAct)
        self.editToolBar.addAction(self.rectAct)
        self.editToolBar.addAction(self.ellipseAct)

    def createStatusBar(self):
        self.infoLabel = QLabel('')
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.statusBar().addPermanentWidget(self.infoLabel)
        self.mouseLabel = QLabel('', self.statusBar())
        self.mouseLabel.setMinimumWidth(100)
        self.statusBar().addPermanentWidget(self.mouseLabel)
        self.statusBar().show()

    def slot_mouseMoveInView(self, pt):
        strPos = str.format('{0},{1}', pt.x(), pt.y())
        self.mouseLabel.setText(strPos)

    # 关联信号-槽
    def connectSignalAndSlot(self):
        # 关联信号-槽
        self.mdiArea.sig_viewMouseMove.connect(self.slot_mouseMoveInView)
