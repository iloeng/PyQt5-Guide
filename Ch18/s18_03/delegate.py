# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSpinBox, QStyledItemDelegate
from PyQt5.QtCore import Qt
from enum import IntEnum


# 各属性项枚举
class EAttrIndex(IntEnum):
    EAttr_Id = 0  # id
    EAttr_Descrition = 1  # 描述
    Eattr_Max = 2


class CDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(CDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        # 只有第1列允许编辑
        if 1 != index.column():
            return None
        print(index.row())
        if EAttrIndex.EAttr_Id == EAttrIndex(index.row()):
            editor = QSpinBox(parent)
            editor.setFrame(False)
            editor.setMinimum(0)
            editor.setMaximum(100)
        else:
            editor = QStyledItemDelegate.createEditor(self, parent, option, index)

        return editor

    def setEditorData(self, editor, index):
        if 1 != index.column():
            return QStyledItemDelegate.setEditorData(self, editor, index)
        if EAttrIndex.EAttr_Id == EAttrIndex(index.row()):
            value = index.model().data(index, Qt.EditRole)
            print(value)
            editor.setValue(value)
        else:
            QStyledItemDelegate.setEditorData(self, editor, index)

    def setModelData(self, editor, model, index):
        if 1 != index.column():
            return QStyledItemDelegate.setModelData(self, editor, model, index)
        if EAttrIndex.EAttr_Id == EAttrIndex(index.row()):
            editor.interpretText()  # 确保取得最新的数值
            model.setData(index, editor.value(), Qt.EditRole)
        else:
            QStyledItemDelegate.setModelData(self, editor, model, index)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
