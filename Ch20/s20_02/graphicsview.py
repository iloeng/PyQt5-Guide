# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QMenu, \
    QAction, QGraphicsScene
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QMimeData, QPointF, QByteArray, QTextStream
from PyQt5.QtCore import pyqtSignal, Qt, QIODevice, QRectF, pyqtSignal, QFile, QDir
from PyQt5.QtXml import QDomDocument
from Ch20.s20_02.graphicsitem import EGraphItemType
from Ch20.s20_02.rectitem import CGraphRectItem
from Ch20.s20_02.ellipseitem import CGraphEllipseItem
import os


class CGraphicsView(QGraphicsView):
    sceneOfView = None  # 场景
    sequenceNumber = 1  # 全局文档索引号
    strFileName = ''  # 文件名
    ptScene = QPointF()  # 鼠标点击时的场景坐标
    sig_viewMouseMove = pyqtSignal(QPointF)
    sig_viewClose = pyqtSignal(QGraphicsView)
    cutAct = None  # 【剪切】子菜单
    copyAct = None  # 【拷贝】子菜单
    pasteAct = None  # 【粘贴】子菜单
    saveGraphAct = None  # 【保存为TXT图形文件】菜单项
    openGraphAct = None  # 【打开TXT图形文件】菜单项
    sig_openGraphFile = pyqtSignal(str)

    def __init__(self, fileName='', parent=None):
        super(CGraphicsView, self).__init__(None, parent)
        self.setMouseTracking(True)
        self.sceneOfView = QGraphicsScene(self)
        self.setScene(self.sceneOfView)
        rct = QRectF(0, 0, 400, 400)
        self.sceneOfView.setSceneRect(rct)
        self.createActions()
        if len(fileName) == 0:
            curFile = "File{0}".format(CGraphicsView.sequenceNumber)
            CGraphicsView.sequenceNumber += 1
            self.strFileName = curFile
        else:
            self.strFileName = fileName
            curFile = self.strFileName
            self.openGraph(curFile)
        self.setWindowTitle(curFile + "[*]")

    def getFileName(self):
        return self.strFileName

    def closeEvent(self, event):
        event.accept()
        QGuiApplication.restoreOverrideCursor()  # 关闭视图后需要恢复光标，否则可能因为意外导致光标处于某个操作状态而无法恢复。
        self.sig_viewClose.emit()

    def isValid(self):
        if self.scene is None:
            return False
        else:
            return True

    def mouseMoveEvent(self, event):
        pt = self.mapToScene(event.localPos().toPoint())
        self.sig_viewMouseMove.emit(pt)  # 发射信号，以便可以在状态栏显示鼠标坐标

    def mousePressEvent(self, event):
        # matx = matrix()
        # matx.m11()
        ptView = event.localPos()
        self.ptScene = self.mapToScene(ptView.toPoint())

    def addRect(self):
        item = CGraphRectItem(None)
        item.setWidth(50)
        item.setHeight(50)
        item.setPos(self.ptScene)
        self.sceneOfView.addItem(item)

    def addEllipse(self):
        item = CGraphEllipseItem(None)
        item.setWidth(50)
        item.setHeight(50)
        item.setPos(self.ptScene)
        self.sceneOfView.addItem(item)

    def drawBackground(self, painter, rect):
        QGraphicsView.drawBackground(self, painter, rect)
        # 绘制一个矩形用来表示场景(scene)的占用区域
        rct = self.sceneRect()
        pn = painter.pen()
        pn.setColor(Qt.gray)
        painter.setPen(pn)
        painter.drawRect(rct)

    # ifndef QT_NO_CLIPBOARD
    def cut(self):
        lst = self.sceneOfView.items(self.ptScene)
        if len(lst) == 0:
            return
        # 剪切时采用隐藏图元、拷贝得到新图元的方法，也可以拷贝得到新图元后把原始图元删除。但是如果删除原始图元，则会影响redo/undo功能。
        for item in lst:
            item.setVisible(False)
        self.copyItems(lst)

    def copy(self):
        lst = self.sceneOfView.items(self.ptScene)
        if len(lst) == 0:
            return
        self.copyItems(lst)

    def copyItems(self, lst):
        # 清除剪贴板的原数据
        clipboard = QApplication.clipboard()
        clipboard.clear()
        # 如果没有图元可拷贝，则返回。
        if len(lst) == 0:
            return
        dataArr = QByteArray()
        # 拷贝的信息写到数据流
        stream = QTextStream(dataArr, QIODevice.WriteOnly)

        # 只拷贝选中图元中第一个图元
        item = lst[0]
        type = item.type()
        pt = item.pos()
        document = QDomDocument()
        root = document.createElement("doc")

        # 图元信息
        itemEle = document.createElement("item")
        itemEle.setAttribute("x", pt.x())
        itemEle.setAttribute("y", pt.y())

        if type == EGraphItemType.EGraphItemType_Rect:
            itemEle.setAttribute("type", QGraphicsItem.UserType + 1)
            rectItem = item
            itemEle.setAttribute("w", rectItem.getWidth())
            itemEle.setAttribute("h", rectItem.getHeight())
        elif type == EGraphItemType.EGraphItemType_Ellipse:
            itemEle.setAttribute("type", QGraphicsItem.UserType + 2)
            rectItem = item
            itemEle.setAttribute("w", rectItem.getWidth())
            itemEle.setAttribute("h", rectItem.getHeight())
        else:
            pass

        root.appendChild(itemEle)
        document.appendChild(root)
        stream << document
        data = QMimeData()
        data.setData("gp/copyItem", dataArr)
        clipboard.setMimeData(data)

    def paste(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if self.sceneOfView is None:
            return
        if not mimeData.hasFormat("gp/copyItem"):
            return
        doc = QDomDocument()
        doc.setContent(mimeData.data("gp/copyItem"))
        root = doc.firstChildElement()
        itemEle = root.firstChildElement()
        strTagName = itemEle.tagName()
        # qDebug() << strTagName
        if strTagName != "item":
            return
        strValue = itemEle.attribute("type", "0")
        type = int(strValue)
        type = EGraphItemType(type)
        pt = self.ptScene
        if itemEle.hasAttribute("w"):
            w = float(itemEle.attribute("w", "0"))
            h = float(itemEle.attribute("h", "0"))
            if type == EGraphItemType.EGraphItemType_Rect:
                # QPen pn(Qt.darkBlue)
                # QBrush brsh(Qt.darkBlue)
                item = CGraphRectItem(None)
                item.setWidth(w)
                item.setHeight(h)
                item.setPos(pt)
                self.sceneOfView.addItem(item)
            elif type == EGraphItemType.EGraphItemType_Ellipse:
                # QPen pn(Qt.darkBlue)
                # QBrush brsh(Qt.darkBlue)
                item = CGraphEllipseItem(None)
                item.setWidth(w)
                item.setHeight(h)
                item.setPos(pt)
                self.sceneOfView.addItem(item)

    def createActions(self):
        self.cutAct = QAction('剪切', self)
        self.cutAct.setStatusTip("Cut the current selection's contents to the clipboard")
        self.cutAct.triggered.connect(self.cut)

        self.copyAct = QAction('复制', self)
        self.copyAct.setStatusTip("Copy the current selection's contents to the clipboard")
        self.copyAct.triggered.connect(self.copy)

        self.pasteAct = QAction('粘贴', self)
        self.pasteAct.setStatusTip("Paste the clipboard's contents into the current selection")
        self.pasteAct.triggered.connect(self.paste)

        self.saveGraphAct = QAction('保存为TXT图形文件', self)
        self.saveGraphAct.setStatusTip("保存为TXT图形文件")
        self.saveGraphAct.triggered.connect(self.saveGraph)

        self.openGraphAct = QAction('打开TXT图形文件', self)
        self.openGraphAct.setStatusTip("打开TXT图形文件")
        self.openGraphAct.triggered.connect(self.openGraph)

    def contextMenuEvent(self, event):
        popMenu = QMenu(self)
        ptScene = self.mapToScene(event.pos())
        lst = self.sceneOfView.items(ptScene)
        if len(lst) != 0:
            popMenu.addAction(self.cutAct)
            popMenu.addAction(self.copyAct)
        else:
            popMenu.addAction(self.pasteAct)
        popMenu.addAction(self.saveGraphAct)
        popMenu.addAction(self.openGraphAct)
        # 判断一下有没有事先执行过剪切、复制操作
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if not mimeData.hasFormat("gp/copyItem"):
            self.pasteAct.setEnabled(False)
        else:
            self.pasteAct.setEnabled(True)
        popPt = event.globalPos()
        popMenu.move(popPt)
        popMenu.show()

    def saveGraph(self):
        lst = self.sceneOfView.items()
        if len(lst) == 0:
            return
        strDir = 'test/'
        dir = QDir()
        if not dir.exists(strDir):
            dir.mkpath(strDir)
        if self.strFileName.find("/") < 0:
            strFile = strDir
            strFile += self.strFileName
            strFile += ".txt"
        else:
            strFile = self.strFileName
        file = QFile(strFile)
        strFileContent = ''
        strTemp = ''
        if not file.open(QFile.WriteOnly | QFile.Truncate):
            return
        for item in lst:
            if not item.isVisible():
                continue
            strTemp = "graph item, type={0}\n".format(item.type())
            strFileContent += strTemp
        file.write(strFileContent.encode("utf-8"))
        file.close()

    def openGraph(self):
        strDir = 'test/'
        if self.strFileName.find("/") < 0:
            strFile = strDir
            strFile += self.strFileName
            strFile += ".txt"
        else:
            strFile = self.strFileName
        self.sig_openGraphFile.emit(strFile)
