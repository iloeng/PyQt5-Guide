# -*- coding: utf-8 -*-
import os

from PyQt5.QtWidgets import (
    QMainWindow, QAction, QActionGroup, QMenu, QLabel, QFrame, QMessageBox,
    QDockWidget, QListWidget
)
from PyQt5.QtGui import QIcon, QKeySequence, QTextCursor
from PyQt5.QtCore import Qt, QFile, QTextStream, pyqtSignal, QThread

from Ch19.s19_09.textedit import CTextEdit
from Ch19.s19_09.listwidget import CListWidget
from Ch19.s19_09.splashscreen import CSplashScreen


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
    sig_progress = pyqtSignal(int)  # 信号
    paragraphsList = None

    def __init__(self, splashScreen, parent=None):
        super(CMainWindow, self).__init__(parent)
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDockWindows()

        self.sig_progress.connect(splashScreen.slot_setProgress)

        self.initialize()

        self.setWindowTitle('拖放')
        self.setMinimumSize(160, 160)
        self.resize(480, 320)

    def initialize(self):
        # 构建视图对象
        self.textEdit = CTextEdit(self)
        file = QFile()
        strFile = 'input.txt'
        file.setFileName(strFile)
        strText = str()
        if (file.open(QFile.ReadOnly | QFile.Text)):
            input = QTextStream(file)
            input.setCodec('UTF-8')
            strText = input.readAll()
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

    def createDockWindows(self):
        dock = QDockWidget('Paragraphs', self)  # 构建浮动窗
        self.paragraphsList = CListWidget(dock)
        strList = ["I have learned how to use QDockWidget today.", "Thank for beging with me.",
                   "I will make some practice tonight."]
        self.paragraphsList.addItems(strList)
        dock.setWidget(self.paragraphsList)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)

    # 关联信号-槽
    def connectSignalAndSlot(self):
        # 关联信号-槽
        self.textEdit.sig_viewMouseMove.connect(self.slot_mouseMoveInView)
        self.textEdit.selectionChanged.connect(self.slot_selectionChanged)
        self.paragraphsList.currentTextChanged.connect(self.slot_addParagraph)

    def slot_addParagraph(self, paragraph):
        print(paragraph)
        if not paragraph.strip():
            return
        cursor = self.textEdit.textCursor()
        if cursor.isNull():
            return
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.PreviousBlock, QTextCursor.MoveAnchor, 0)
        cursor.insertBlock()
        cursor.insertText(paragraph)
        cursor.insertBlock()
        cursor.endEditBlock()
