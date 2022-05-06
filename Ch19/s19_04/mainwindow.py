# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QAction, QActionGroup, QMenu, QLabel, QFrame, QMessageBox
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt
from Ch19.s19_04.ks19_04_rc import *


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

    def __init__(self, parent=None):
        super(CMainWindow, self).__init__(parent)
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.infoLabel = QLabel('')
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.statusBar().addPermanentWidget(self.infoLabel)
        self.setWindowTitle('菜单')
        self.setMinimumSize(160, 160)
        self.resize(480, 320)

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

    def bold(self):
        self.infoLabel.setText('Invoked <b>Edit|Format|Bold</b>')

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
