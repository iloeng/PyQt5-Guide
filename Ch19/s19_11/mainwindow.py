# -*- coding: utf-8 -*-
import os

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QActionGroup, QMenu, QLabel,
    QFrame, QMessageBox, QTreeView, QDockWidget
)
from PyQt5.QtGui import (
    QIcon, QKeySequence, QStandardItemModel, QStandardItem, QColor, QFont,
    QImage
)
from PyQt5.QtCore import (
    Qt, QFile, QTextStream, pyqtSignal, QThread, QSize, QMutex, QMutexLocker,
    QTime
)

from Ch19.s19_11.textedit import CTextEdit
from Ch19.s19_11.splashscreen import CSplashScreen
from Ch19.s19_11.logdockwidget import CLogDockWidget
from Ch19.s19_11.logevt import CLogEvt, ELogLevel, SLog


class CMainWindow(QMainWindow):
    fileMenu = None  # 文件菜单
    editMenu = None  # 编辑菜单
    formatMenu = None  # 格式菜单
    helpMenu = None  # 帮助菜单
    alignmentGroup = None  # 对齐菜单项组
    openAct = None  # 【打开】子菜单
    saveAct = None  # 【保存】子菜单
    exitAct = None  # 【退出】子菜单
    cutAct = None  # 【剪切】子菜单
    copyAct = None  # 【拷贝】子菜单
    pasteAct = None  # 【粘贴】子菜单
    boldAct = None  # 【粗体】子菜单
    italicAct = None  # 【斜体】子菜单
    leftAlignAct = None  # 【左对齐】子菜单
    rightAlignAct = None  # 【右对齐】子菜单
    centerAct = None  # 【居中对齐】子菜单
    setLineSpacingAct = None  # 【设置行间距】子菜单
    setParagraphSpacingAct = None  # 【设置段间距】子菜单
    aboutAct = None  # 【帮助】子菜单
    infoLabel = None  # 信息标签
    fileToolBar = None  # 【文件】工具条
    editToolBar = None  # 【编辑】工具条
    mouseLabel = None  # 显示鼠标位置的标签
    textEdit = None  # 视图
    sig_progress = pyqtSignal(int)
    treeView = None  # 树视图
    logDockWidget = None  # 日志窗口
    mutex = None

    def __init__(self, splashScreen, parent=None):
        super(CMainWindow, self).__init__(parent)
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createTreeView()
        self.createLogDockWidget()
        self.sig_progress.connect(splashScreen.slot_setProgress)
        self.initialize()

        self.setWindowTitle('事项窗')
        self.setMinimumSize(160, 160)
        self.resize(480, 320)

    def initialize(self):
        mutex = QMutex()
        # 构建视图对象
        self.textEdit = CTextEdit(self)
        file = QFile()
        trainDevHome = os.getenv('TRAINDEVHOME')
        if None is trainDevHome:
            trainDevHome = 'usr/local/gui'
        strFile = trainDevHome + '/test/chapter19/ks19_02/input.txt'
        file.setFileName(strFile)
        strText = str()
        if file.open(QFile.ReadOnly | QFile.Text):
            inputs = QTextStream(file)
            inputs.setCodec('UTF-8')
            strText = inputs.readAll()
        self.textEdit.setText(strText)
        self.setCentralWidget(self.textEdit)
        self.readData()
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

    def open(self):
        self.infoLabel.setText('Invoked <b>File|Open</b>')

    def save(self):
        self.infoLabel.setText('Invoked <b>File|Save</b>')

    def cut(self):
        self.infoLabel.setText('Invoked <b>Edit|Cut</b>')

    def copy(self):
        self.infoLabel.setText('Invoked <b>Edit|Copy</b>')

    def paste(self):
        self.infoLabel.setText('Invoked <b>Edit|Paste</b>')

    def bold(self, bChecked):
        self.infoLabel.setText('Invoked <b>Edit|Format|Bold</b>')
        tc = self.textEdit.textCursor()  # 获取当前光标下的文本对象
        textCharFormat = tc.blockCharFormat()  # 获取该对象的格式信息
        ft = textCharFormat.font()  # 获取字体信息
        ft.setBold(bChecked)  # 根据按钮的状态设置字体的粗体信息
        textCharFormat.setFont(ft)  # 重新为格式信息对象设置字体
        self.textEdit.setCurrentCharFormat(textCharFormat)  # 为选中的文本更新格式

    def italic(self):
        self.infoLabel.setText('Invoked <b>Edit|Format|Italic</b>')

    def leftAlign(self):
        self.infoLabel.setText('Invoked <b>Edit|Format|Left Align</b>')

    def rightAlign(self):
        self.infoLabel.setText('Invoked <b>Edit|Format|Right Align</b>')

    def center(self):
        self.infoLabel.setText('Invoked <b>Edit|Format|Center</b>')

    def setLineSpacing(self):
        self.infoLabel.setText('Invoked <b>Edit|Format|Set Line Spacing</b>')

    def setParagraphSpacing(self):
        self.infoLabel.setText('Invoked <b>Edit|Format|Set Paragraph Spacing</b>')

    def about(self):
        self.infoLabel.setText('Invoked <b>Help|About</b>')
        QMessageBox.about(self,
                          'About Menu',
                          'The <b>Menu</b> example shows how to create menu-bar menus and context menus.')

    def createActions(self):
        self.openAct = QAction(QIcon(':/images/open.png'), '打开...', self)
        self.openAct.setShortcuts(QKeySequence.Open)
        self.openAct.setStatusTip('Open an existing file')
        self.openAct.triggered.connect(self.open)

        self.saveAct = QAction('保存', self)
        self.saveAct.setShortcuts(QKeySequence.Save)
        self.saveAct.setStatusTip('Save the document to disk')
        self.saveAct.triggered.connect(self.save)

        self.exitAct = QAction('退出', self)
        self.exitAct.setShortcuts(QKeySequence.Quit)
        self.exitAct.setStatusTip('Exit the application')
        self.exitAct.triggered.connect(self.close)

        self.cutAct = QAction('剪切', self)
        self.cutAct.setShortcuts(QKeySequence.Cut)
        self.cutAct.setStatusTip("Cut the current selection's contents to the clipboard")
        self.cutAct.triggered.connect(self.cut)

        self.copyAct = QAction('复制', self)
        self.copyAct.setShortcuts(QKeySequence.Copy)
        self.copyAct.setStatusTip("Copy the current selection's contents to the clipboard")
        self.copyAct.triggered.connect(self.copy)

        self.pasteAct = QAction('粘贴', self)
        self.pasteAct.setShortcuts(QKeySequence.Paste)
        self.pasteAct.setStatusTip("Paste the clipboard's contents into the current selection")
        self.pasteAct.triggered.connect(self.paste)

        self.boldAct = QAction('粗体', self)
        self.boldAct.setCheckable(True)
        self.boldAct.setShortcut(QKeySequence.Bold)
        self.boldAct.setStatusTip('Make the text bold')
        self.boldAct.triggered.connect(self.bold)

        boldFont = self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct = QAction('斜体', self)
        self.italicAct.setCheckable(True)
        self.italicAct.setShortcut(QKeySequence.Italic)
        self.italicAct.setStatusTip('Make the text italic')
        self.italicAct.triggered.connect(self.italic)

        italicFont = self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct = QAction('行间距...', self)
        self.setLineSpacingAct.setStatusTip('Change the gap between the lines of a paragraph')
        self.setLineSpacingAct.triggered.connect(self.setLineSpacing)

        self.setParagraphSpacingAct = QAction('段间距...', self)
        self.setParagraphSpacingAct.setStatusTip('Change the gap between paragraphs')
        self.setParagraphSpacingAct.triggered.connect(self.setParagraphSpacing)

        self.aboutAct = QAction('关于', self)
        self.aboutAct.setStatusTip("Show the application's About box")
        self.aboutAct.triggered.connect(self.about)

        self.leftAlignAct = QAction('左对齐', self)
        self.leftAlignAct.setCheckable(True)
        self.leftAlignAct.setShortcut('Ctrl+L')
        self.leftAlignAct.setStatusTip('Left align the selected text')
        self.leftAlignAct.triggered.connect(self.leftAlign)

        self.rightAlignAct = QAction('右对齐', self)
        self.rightAlignAct.setCheckable(True)
        self.rightAlignAct.setShortcut('Ctrl+R')
        self.rightAlignAct.setStatusTip('Right align the selected text')
        self.rightAlignAct.triggered.connect(self.rightAlign)

        self.centerAct = QAction('居中对齐', self)
        self.centerAct.setCheckable(True)
        self.centerAct.setShortcut('Ctrl+E')
        self.centerAct.setStatusTip('Center the selected text')
        self.centerAct.triggered.connect(self.center)

        self.alignmentGroup = QActionGroup(self)
        self.alignmentGroup.addAction(self.leftAlignAct)
        self.alignmentGroup.addAction(self.rightAlignAct)
        self.alignmentGroup.addAction(self.centerAct)
        self.leftAlignAct.setChecked(True)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('文件')
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)

        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu('编辑')
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)
        self.editMenu.addSeparator()

        self.helpMenu = self.menuBar().addMenu('帮助')
        self.helpMenu.addAction(self.aboutAct)

        self.formatMenu = self.editMenu.addMenu('格式化')
        self.formatMenu.addAction(self.boldAct)
        self.formatMenu.addAction(self.italicAct)
        self.formatMenu.addSeparator().setText('对齐')
        self.formatMenu.addAction(self.leftAlignAct)
        self.formatMenu.addAction(self.rightAlignAct)
        self.formatMenu.addAction(self.centerAct)
        self.formatMenu.addSeparator()
        self.formatMenu.addAction(self.setLineSpacingAct)
        self.formatMenu.addAction(self.setParagraphSpacingAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar('文件工具条')
        self.fileToolBar.setObjectName('file toolbar')
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)
        self.editToolBar = self.addToolBar('编辑工具条')
        self.editToolBar.setObjectName("edit toolbar")
        self.editToolBar.addAction(self.cutAct)
        self.editToolBar.addAction(self.copyAct)
        self.editToolBar.addAction(self.pasteAct)
        self.editToolBar.addAction(self.boldAct)

    def createStatusBar(self):
        self.infoLabel = QLabel('')
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.statusBar().addPermanentWidget(self.infoLabel)
        self.mouseLabel = QLabel('', self.statusBar())
        self.mouseLabel.setMinimumWidth(100)
        self.statusBar().addPermanentWidget(self.mouseLabel)
        self.statusBar().show()

    def slot_mouseMoveInView(self, evt):
        ptLocal = evt.localPos()
        pt = ptLocal.toPoint()
        strPos = str.format('{0},{1}', pt.x(), pt.y())
        self.mouseLabel.setText(strPos)

    def slot_selectionChanged(self):
        tc = self.textEdit.textCursor()  # 获取光标下选中的文本对象
        textCharFormat = tc.charFormat()  # 获取它的格式
        b = textCharFormat.font().bold()  # 获取字体的粗体信息
        # 必须先阻塞信号，否则，setChecked()调用将触发m_pBoldAct的triggered()信号
        self.boldAct.blockSignals(True)  # 阻塞信号
        self.boldAct.setChecked(b)  # 设置粗体按钮的状态
        self.boldAct.blockSignals(False)  # 解除信号阻塞

    # 关联信号-槽
    def connectSignalAndSlot(self):
        # 关联信号-槽
        self.textEdit.sig_viewMouseMove.connect(self.slot_mouseMoveInView)
        self.textEdit.selectionChanged.connect(self.slot_selectionChanged)
        self.treeView.doubleClicked.connect(self.slot_itemDoubleClicked)

    def slot_itemDoubleClicked(self, index):
        model = self.treeView.model()
        strs = model.data(index)
        self.openFile(strs)

    def openFile(self, strTitle):
        log = SLog()
        log.time = QTime.currentTime()
        if strTitle.strip():
            fileName = 'test/'
            fileName += strTitle
            fileName += '.txt'
            strs = self.textEdit.currentFileName()
            if strs == fileName:
                return
            if self.textEdit.openFile(fileName):
                self.infoLabel.setText("file has been loaded")
                if strTitle == fileName:
                    log.level = ELogLevel.ELogLevel_Warning
                    log.msg = "file: {0} already open!".format(fileName)
                    self.notify(log)
                else:
                    log.level = ELogLevel.ELogLevel_Warning
                    log.msg = "file: {0} open success!".format(fileName)
                    self.notify(log)
            else:
                log.level = ELogLevel.ELogLevel_Warning
                log.msg = "file: {0} can not open!".format(fileName)
                self.notify(log)

    def createTreeView(self):
        dock = QDockWidget('dock', self)  # 构建浮动窗
        # 构建模型，并设置一些属性
        model = QStandardItemModel()
        self.treeView = QTreeView(dock)
        dock.setWidget(self.treeView)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        self.treeView.setModel(model)
        self.treeView.setAlternatingRowColors(True)  # 每间隔一行颜色不一样，当有qss时该属性无效

        self.treeView.setRootIsDecorated(True)  # 根分支是否可展开
        # self.treeView.header().setFirstSectionMovable(False)  # False:首列不允许被移动,True:首列允许移动
        self.treeView.header().setStretchLastSection(True)  # 将最后一列设置为自动拉伸,True:自动拉伸,False:不自动拉伸。
        self.treeView.setEditTriggers(QTreeView.NoEditTriggers)  # 不能编辑数据项

        # 将数据添加到模型，包括子数据
        # 得到根节点
        itemRoot = model.invisibleRootItem()
        # 得到根节点的序号
        indexRoot = itemRoot.index()
        # 构建country节点
        itemCountry = QStandardItem('中国')
        # 将country节点作为根节点的子节点
        itemRoot.appendRow(itemCountry)
        # 设置country的字体、字色
        ft = QFont('宋体', 16)
        ft.setBold(True)
        itemCountry.setData(ft, Qt.FontRole)
        itemCountry.setData(QColor(Qt.red), Qt.TextColorRole)
        image = QImage(":/images/china.png")
        itemCountry.setData(image.scaled(QSize(24, 24)), Qt.DecorationRole)

        # 设置 itemRoot 的列数以便显示省的个数
        COLUMNCOUNT = 2  # 列数
        itemRoot.setColumnCount(COLUMNCOUNT)
        # 必须在设置列数之后才能设置标题中该列的数据。即列不存在时，设置数据无效。
        model.setHeaderData(1, Qt.Horizontal, "子项个数", Qt.DisplayRole)

        # 在Country节点所在的行的第1列显示省的个数
        model.setData(model.index(0, 1, indexRoot), 2)

        # 构建省节点1，并添加到国家节点的下级
        itemProvince = QStandardItem('山东')
        itemCountry.appendRow(itemProvince)

        # 设置Country的列数
        itemCountry.setColumnCount(COLUMNCOUNT)

        # 设置Province节点的第0列的文本颜色为蓝色
        model.setData(model.index(0, 0, itemCountry.index()),
                      QColor(Qt.blue),
                      Qt.TextColorRole)

        # 设置Country节点第1列数据为城市个数
        model.setData(model.index(0, 1, itemCountry.index()), 2)

        # 构建所有城市
        # 构建城市节点1
        itemCity = QStandardItem('济南')
        # 添加城市节点1
        itemProvince.appendRow(itemCity)
        # 构建城市节点2
        itemCity = QStandardItem('青岛')
        # 添加城市节点2
        itemProvince.appendRow(itemCity)

        # 构建省节点2，并添加到国家节点的下级
        itemProvince = QStandardItem('河北')
        itemCountry.appendRow(itemProvince)
        # 设置Province节点的第0列的文本颜色为蓝色
        model.setData(model.index(1, 0, itemCountry.index()),
                      QColor(Qt.blue),
                      Qt.TextColorRole)

        # 设置Country节点第1列数据为城市个数
        model.setData(model.index(1, 1, itemCountry.index()), 3)

        # 遍历所有城市
        # 构建城市节点1
        itemCity = QStandardItem('北戴河')
        # 添加城市节点1
        itemProvince.appendRow(itemCity)
        # 构建城市节点2
        itemCity = QStandardItem('张家口')
        # 添加城市节点2
        itemProvince.appendRow(itemCity)
        # 构建城市节点3
        itemCity = QStandardItem('保定')
        # 添加城市节点3
        itemProvince.appendRow(itemCity)

    def createLogDockWidget(self):
        self.logDockWidget = CLogDockWidget("日志输出窗口", self)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.logDockWidget)

    def notify(self, log):
        mutexLocker = QMutexLocker(self.mutex)
        if self.logDockWidget is None:
            return

        logEvt = CLogEvt(CLogEvt.ELogEvt_LogOut)
        logEvt.setLog(log)
        QApplication.postEvent(self.logDockWidget, logEvt)
