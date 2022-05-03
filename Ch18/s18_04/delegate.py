# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSpinBox, QStyledItemDelegate, QComboBox
from PyQt5.QtCore import Qt, QMetaType, QVariant
from Ch18.s18_04.editor import CEditor
from Ch18.s18_04.tablemodel import CTableModel


class CDelegate(QStyledItemDelegate):
    strListYesNo = ['yes', 'no']  # 0:yes, 1:no
    strListSpeed = ['慢速', '中速', '快速']

    def __init__(self, parent=None):
        super(CDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        # 只有第1列允许编辑
        if 1 != index.column():
            return QStyledItemDelegate.createEditor(self, parent, option, index)
        print(index.row())
        if CTableModel.EAttrIndex.EAttr_Id == CTableModel.EAttrIndex(index.row()):
            editor = QSpinBox(parent)
            editor.setFrame(False)
            editor.setMinimum(0)
            editor.setMaximum(100)
        elif CTableModel.EAttrIndex.EAttr_Checked == CTableModel.EAttrIndex(index.row()):
            editor = QComboBox(parent)
            editor.addItems(self.strListYesNo)
            editor.setItemData(0, 0)  # 0:yes,索引=0，对应的值=0
            editor.setItemData(1, 1)  # 1:no,索引=1，对应的值=1
        elif CTableModel.EAttrIndex.EAttr_LastOneFlag == CTableModel.EAttrIndex(index.row()):
            editor = CEditor(parent)
            editor.sig_editFinished.connect(self.slot_commitAndCloseEditor)

        elif CTableModel.EAttrIndex.Eattr_AnimateSpeed == CTableModel.EAttrIndex(index.row()):
            editor = QComboBox(parent)
            editor.addItems(self.strListSpeed)
            editor.setItemData(0, CTableModel.EAnimateSpeed.EAnimateSpeed_Slow)
            editor.setItemData(1, CTableModel.EAnimateSpeed.EAnimateSpeed_Normal)
            editor.setItemData(2, CTableModel.EAnimateSpeed.EAnimateSpeed_Fast)
        else:
            editor = QStyledItemDelegate.createEditor(self, parent, option, index)

        return editor

    def setEditorData(self, editor, index):
        if 1 != index.column():
            return QStyledItemDelegate.setEditorData(self, editor, index)
        if CTableModel.EAttrIndex.EAttr_Id == CTableModel.EAttrIndex(index.row()):
            value = index.model().data(index, Qt.EditRole)
            editor.setValue(value)
        elif CTableModel.EAttrIndex.EAttr_Checked == CTableModel.EAttrIndex(index.row()):
            #   item 	index  value(data())
            #   yes  	0        		0
            # 	no   	1       	 	1
            idx = (index.model().data(index, Qt.EditRole) and 1 or 0)
            editor.setCurrentIndex(idx)
        elif CTableModel.EAttrIndex.EAttr_LastOneFlag == CTableModel.EAttrIndex(index.row()):
            var = index.model().data(index, Qt.EditRole)
            checkState = Qt.CheckState(var)
            if checkState:
                editor.setText('是')
            else:
                editor.setText('否')
        elif CTableModel.EAttrIndex.Eattr_AnimateSpeed == CTableModel.EAttrIndex(index.row()):
            aSpeed = index.model().data(index, Qt.EditRole)
            aSpeed = CTableModel.EAnimateSpeed(aSpeed)
            idx = 0
            if aSpeed == CTableModel.EAnimateSpeed.EAnimateSpeed_Slow:
                idx = 0
            elif aSpeed == CTableModel.EAnimateSpeed.EAnimateSpeed_Normal:
                idx = 1
            elif aSpeed == CTableModel.EAnimateSpeed.EAnimateSpeed_Fast:
                idx = 2
            editor.setCurrentIndex(idx)
        else:
            QStyledItemDelegate.setEditorData(self, editor, index)

    def setModelData(self, editor, model, index):
        if 1 != index.column():
            return QStyledItemDelegate.setModelData(self, editor, model, index)
        if CTableModel.EAttrIndex.EAttr_Id == CTableModel.EAttrIndex(index.row()):
            editor.interpretText()  # 确保取得最新的数值
            model.setData(index, editor.value(), Qt.EditRole)
        elif CTableModel.EAttrIndex.EAttr_Checked == CTableModel.EAttrIndex(index.row()):
            var = editor.currentData()  # 0:yes, 1:no
            model.setData(index, var, Qt.EditRole)
        elif CTableModel.EAttrIndex.EAttr_LastOneFlag == CTableModel.EAttrIndex(index.row()):
            var = (editor.text() == '是' and True or False)
            model.setData(index, var, Qt.EditRole)
        elif CTableModel.EAttrIndex.Eattr_AnimateSpeed == CTableModel.EAttrIndex(index.row()):
            var = editor.currentData()
            model.setData(index, var, Qt.EditRole)
        else:
            QStyledItemDelegate.setModelData(self, editor, model, index)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def slot_commitAndCloseEditor(self):
        editor = self.sender()
        self.commitData.emit(editor)  # 提交数据
        self.closeEditor.emit(editor)  # 关闭编辑器控件

    def displayText(self, value, locale):
        var = QVariant(value)
        if QMetaType.Bool == var.userType():
            strs = (value and '是' or '否')
            return strs
        else:
            return QStyledItemDelegate.displayText(self, value, locale)
