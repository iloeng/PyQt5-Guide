# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMdiArea, QAction, QGraphicsScene, QWidget, QFileDialog, QMdiSubWindow
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, pyqtSignal, QRectF, QPointF, QFileInfo
from Ch20.s20_02.graphicsview import CGraphicsView
from Ch20.s20_02.textedit import CTextEdit
import types


class CEditMdiArea(QMdiArea):
    lastActivatedMdiChild = None  # 上一个活动子窗口
    mainWindow = None  # 父窗口
    graphicsView = None  # 视图
    sig_editViewChanged = pyqtSignal(QWidget)
    sig_viewMouseMove = pyqtSignal(QPointF)
    sig_viewClose = pyqtSignal(QWidget)

    def __init__(self, parent=None):
        super(CEditMdiArea, self).__init__(parent)
        self.setViewMode(QMdiArea.TabbedView)
        self.subWindowActivated.connect(self.slot_subWindowActivate)
        self.slot_subWindowActivate(None)

    def openFileByGraphview(self, fileName):
        bSucceeded = False
        if len(fileName) != 0:
            existing = self.findGraphViewMdiChild(fileName)
            if existing:
                self.setActiveSubWindow(existing)
                return True
            child = self.createGraphViewMdiChild(fileName)
            succeeded = child.isValid()
            if succeeded:
                child.showMaximized()
            else:
                if child.parent():
                    subWindow = QMdiSubWindow(child.parent())
                    subWindow and subWindow.close() or child.close()
                else:
                    child.close()
        return bSucceeded

    def openFileByTextview(self, fileName):
        bSucceeded = False
        if len(fileName) != 0:
            existing = self.findTexteditMdiChild(fileName)
            if existing:
                self.setActiveSubWindow(existing)
                return True
            child = self.createTexteditMdiChild(fileName)
            if isinstance(child, CGraphicsView):
                succeeded = child.isValid()
            else:
                succeeded = True
            if succeeded:
                child.showMaximized()
            else:
                if child.parent():
                    subWindow = QMdiSubWindow(child.parent())
                    subWindow and subWindow.close() or child.close()
                else:
                    child.close()
        return bSucceeded

    def slot_subWindowActivate(self, mdiChild):
        hasMdiChild = ((mdiChild is None) and False or True)
        if not hasMdiChild:
            return

        if mdiChild != self.lastActivatedMdiChild:
            if self.lastActivatedMdiChild:
                view = self.getActiveEditView(self.lastActivatedMdiChild)
                if isinstance(view, CGraphicsView):
                    # 需要把槽函数跟旧视图解除关联，防止旧视图信号继续触发槽函数
                    self.disconnectEditViewWithSlot_whenInActivate(view)

            view = self.getActiveEditView(mdiChild)
            if isinstance(view, CGraphicsView):
                self.sig_editViewChanged.emit(view)  # 发出信号
                # 将编辑视图挂接到多窗口区域的槽函数
                self.connectEditViewWithSlot(view)
        self.lastActivatedMdiChild = mdiChild

    # m_pPasteAct.setEnabled(hasMdiChild)

    def getMainWindow(self):
        return self.mainWindow

    def activeMdiChild(self):
        view = None
        tActiveSubWindow = self.activeSubWindow()
        if tActiveSubWindow is None:
            tActiveSubWindow = self.lastActivatedMdiChild
        if tActiveSubWindow:
            view = self.getActiveEditView(tActiveSubWindow)
        return view

    def createGraphViewMdiChild(self, fileName):
        view = CGraphicsView(fileName, self)
        if view and view.isValid():
            subWindow1 = QMdiSubWindow()
            subWindow1.setWidget(view)
            subWindow1.setAttribute(Qt.WA_DeleteOnClose)
            self.addSubWindow(subWindow1)
            view.setParent(subWindow1)
        return view

    def createTexteditMdiChild(self, fileName):
        textEdit = CTextEdit(self)
        if textEdit is None:
            return
        if len(fileName) > 0:
            textEdit.openFile(fileName)
            subWindow1 = QMdiSubWindow(self)
            subWindow1.setWidget(textEdit)
            subWindow1.setAttribute(Qt.WA_DeleteOnClose)
            self.addSubWindow(subWindow1)
            textEdit.setParent(subWindow1)
        return textEdit

    def findGraphViewMdiChild(self, fileName):
        strFileName = QFileInfo(fileName).fileName()
        for window in self.subWindowList():
            view = self.getActiveEditView(window)
            if isinstance(view, CGraphicsView) and (view.getFileName() == strFileName):
                return window
        return None

    def findTexteditMdiChild(self, fileName):
        strFileName = QFileInfo(fileName).fileName()
        for window in self.subWindowList():
            view = self.getActiveEditView(window)
            if view is None:
                continue
            if isinstance(view, CTextEdit) and (view.windowTitle() == strFileName):
                return window
        return None

    def getActiveEditView(self, mdiChild):
        if not mdiChild:
            return None
        view = None
        if mdiChild.widget():
            view = mdiChild.widget()
        return view

    def slot_viewClose(self, child):
        if child is None:
            return
        view = CGraphicsView(child)
        if view:
            self.disconnectEditViewWithSlot(view)  # 将编辑视图与多窗口区域的槽函数断开连接
        self.lastActivatedMdiChild = None
        self.sig_editViewClose.emit(child)
        self.lastActivatedMdiChild = None  # 防止其他对象对于 editViewClose 信号的处理导致触发activeSubWindow从而使self.lastActivatedMdiChild重新被赋值（为已关闭的窗口）

    def connectEditViewWithSlot(self, view):
        view.sig_viewMouseMove.connect(self.sig_viewMouseMove);
        view.sig_viewClose.connect(self.slot_viewClose)
        view.sig_openGraphFile.connect(self.slot_openTextGraphFile)

    def slot_openTextGraphFile(self, fileName):
        self.openFileByTextview(fileName)

    def disconnectEditViewWithSlot(self, view):
        self.disconnectEditViewWithSlot_whenInActivate(view)
        view.sig_viewClose.disconnect(self.slot_viewClose)
        view.sig_openGraphFile.disconnect(self.slot_openTextGraphFile)

    def disconnectEditViewWithSlot_whenInActivate(self, view):
        view.sig_viewMouseMove.disconnect(self.sig_viewMouseMove)

    def createActions(self):
        pass

    def createToolBars(self):
        pass

    def new(self):
        child = self.createGraphViewMdiChild("")
        if child is None:
            return
        bSucceeded = child.isValid()
        if bSucceeded:
            child.showMaximized()
        else:
            child.close()

    def open(self):
        strFilter = "text file(*.txt);;XML File(*.xml);;*(*.*)"
        fileName, _ = QFileDialog.getOpenFileName(self, 'select file to open', 'c:\\', strFilter,
                                                  "Txt File(*.txt)")
        self.openFileByGraphview(fileName)

    def save(self):
        view = self.activeMdiChild()
        if view is None:
            return
        if isinstance(view, CGraphicsView):
            view.saveGraph()

    # ifndef QT_NO_CLIPBOARD
    def cut(self):
        view = self.activeMdiChild()
        if view is None:
            return
        if isinstance(view, CGraphicsView):
            view.cut()

    def copy(self):
        view = self.activeMdiChild()
        if view is None:
            return
        if isinstance(view, CGraphicsView):
            view.copy()

    def paste(self):
        view = self.activeMdiChild()
        if view is None:
            return
        if isinstance(view, CGraphicsView):
            view.paste()

    # endif
    def addRect(self):
        view = self.activeMdiChild()
        if view is None:
            return
        if isinstance(view, CGraphicsView):
            view.addRect()

    def addEllipse(self):
        view = self.activeMdiChild()
        if view is None:
            return
        if isinstance(view, CGraphicsView):
            view.addEllipse()
