# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTextEdit, QApplication
from PyQt5.QtGui import QPainter, QFont, QColor, QMouseEvent, QDrag
from PyQt5.QtCore import Qt, QPointF, QPoint, QByteArray, QTextStream, QIODevice, QMimeData
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtXml import QDomDocument, QDomNode


class CTextEdit(QTextEdit):
    sig_viewMouseMove = pyqtSignal(QMouseEvent)  # 定义一个信号
    ptMousePress = QPointF()  # 鼠标单击时的坐标
    bDrag = False  # 进入拖放状态

    def __init__(self, parent=None):
        super(CTextEdit, self).__init__(parent)
        self.setMouseTracking(True)

    def paintEvent(self, evt):
        painter = QPainter()
        painter.begin(self.viewport())
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(Qt.blue)
        painter.fillRect(evt.rect(), QColor(0, 255, 255, 100))
        ft = QFont("宋体", 18)
        painter.setFont(ft)
        painter.drawText(QPointF(100, 100), "file read ok!")
        painter.end()
        QTextEdit.paintEvent(self, evt)

    def mouseMoveEvent(self, evt):
        self.sig_viewMouseMove.emit(evt)
        # 判断是否进入拖放状态
        btns = evt.buttons()
        if not (btns | Qt.NoButton):
            self.bDrag = False
        bDistance = False
        ptDistance = evt.globalPos() - self.ptMousePress
        if ptDistance.manhattanLength() > QApplication.startDragDistance():  # 超过允许的拖放距离才启动拖放操作
            bDistance = True
        if self.bDrag and bDistance and (btns & Qt.LeftButton):
            self.bDrag = False
            tc = self.textCursor()  # 获取光标下选中的文本对象
            textCharFormat = tc.charFormat()  # 获取它的格式
            bold = textCharFormat.font().bold()  # 获取字体的粗体信息
            # 开始准备拖放的数据
            mimeData = QMimeData()
            itemData = QByteArray()
            textStream = QTextStream(itemData, QIODevice.ReadWrite)
            textStream.setCodec('UTF-8')
            doc = QDomDocument()
            rootDoc = doc.createElement('root')
            doc.appendChild(rootDoc)
            eleDoc = doc.createElement('document')
            eleDoc.setAttribute('text', tc.selectedText())
            eleDoc.setAttribute('bold', bold)
            rootDoc.appendChild(eleDoc)
            doc.save(textStream, 1, QDomNode.EncodingFromTextStream)
            mimeData.setData('dnd/format', itemData)
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            if (drag.exec(Qt.DropActions(Qt.MoveAction | Qt.CopyAction),
                          Qt.CopyAction) == Qt.CopyAction):
                pass
            return
        QTextEdit.mouseMoveEvent(self, evt)  # 首先，调用基类接口

    def mousePressEvent(self, evt):
        QTextEdit.mousePressEvent(self, evt)  # 首先，调用基类接口
        self.ptMousePress = evt.globalPos()
        tc = self.textCursor()  # 获取光标下选中的文本对象
        if tc.selectedText().strip():
            self.bDrag = True
