# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSpinBox, QStyledItemDelegate, QComboBox
from PyQt5.QtCore import Qt, QMetaType, QVariant
from Ch18.s18_05.editor import CEditor
from Ch18.s18_05.tablemodel import CTableModel


class CDelegate(QStyledItemDelegate):
    strListYesNo = ['yes', 'no']  # 0:yes, 1:no
    strListSpeed = ['慢速', '中速', '快速']

    def __init__(self, parent=None):
        super(CDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        # 只有第1列允许编辑
        if 1 != index.column():
            return QStyledItemDelegate.createEditor(self, parent, option, index)
        idxParent = (index.parent().isValid() and index.parent() or index)
        if CTableModel.EAttrIndex.EAttr_Id == CTableModel.EAttrIndex(idxParent.row()):
            editor = QSpinBox(parent)
            editor.setFrame(False)
            editor.setMinimum(0)
            editor.setMaximum(100)
            return editor
        elif CTableModel.EAttrIndex.EAttr_Checked == CTableModel.EAttrIndex(idxParent.row()):
            editor = QComboBox(parent)
            editor.addItems(self.strListYesNo)
            editor.setItemData(0, 0)  # 0:yes,索引=0，对应的值=0
            editor.setItemData(1, 1)  # 1:no,索引=1，对应的值=1
            return editor
        elif CTableModel.EAttrIndex.EAttr_LastOneFlag == CTableModel.EAttrIndex(idxParent.row()):
            editor = CEditor(parent)
            editor.sig_editFinished.connect(self.slot_commitAndCloseEditor)
            return editor
        elif CTableModel.EAttrIndex.Eattr_Animate == CTableModel.EAttrIndex(idxParent.row()):
            if idxParent != index and idxParent.isValid():  # 有父项，说明是子属性项
                if CTableModel.EAttrIndexAnimate.EattrAnimate_AnimateSpeed == \
                        CTableModel.EAttrIndexAnimate(index.row()):  # 如果是【动画速度】属性项
                    editor = QComboBox(parent)
                    editor.addItems(self.strListSpeed)
                    editor.setItemData(0, CTableModel.EAnimateSpeed.EAnimateSpeed_Slow)
                    editor.setItemData(1, CTableModel.EAnimateSpeed.EAnimateSpeed_Normal)
                    editor.setItemData(2, CTableModel.EAnimateSpeed.EAnimateSpeed_Fast)
                    return editor
        editor = QStyledItemDelegate.createEditor(self, parent, option, index)
        return editor

    def setEditorData(self, editor, index):
        if 1 != index.column():
            return QStyledItemDelegate.setEditorData(self, editor, index)
        idxParent = (index.parent().isValid() and index.parent() or index)
        if CTableModel.EAttrIndex.EAttr_Id == CTableModel.EAttrIndex(idxParent.row()):
            value = index.model().data(index, Qt.EditRole)
            editor.setValue(value)
            return
        elif CTableModel.EAttrIndex.EAttr_Checked == CTableModel.EAttrIndex(idxParent.row()):
            #   item 	 index  value(data())
            #   yes  	0        		0
            # 	no   	1       	 	1
            idx = (index.model().data(index, Qt.EditRole) and 1 or 0)
            editor.setCurrentIndex(idx)
            return
        elif CTableModel.EAttrIndex.EAttr_LastOneFlag == CTableModel.EAttrIndex(idxParent.row()):
            var = index.model().data(index, Qt.EditRole)
            checkState = Qt.CheckState(var)
            if checkState:
                editor.setText('是')
            else:
                editor.setText('否')
            return
        elif CTableModel.EAttrIndex.Eattr_Animate == CTableModel.EAttrIndex(idxParent.row()):
            # 有父项（说明是子属性项），并且是【动画速度】属性项
            if idxParent != index and idxParent.isValid():  # 有父项，说明是子属性项
                if CTableModel.EAttrIndexAnimate.EattrAnimate_AnimateSpeed == \
                        CTableModel.EAttrIndexAnimate(index.row()):  # 如果是【动画速度】属性项
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
        QStyledItemDelegate.setEditorData(self, editor, index)

    def setModelData(self, editor, model, index):
        if 1 != index.column():
            return QStyledItemDelegate.setModelData(self, editor, model, index)
        idxParent = (index.parent().isValid() and index.parent() or index)
        if CTableModel.EAttrIndex.EAttr_Id == CTableModel.EAttrIndex(idxParent.row()):
            editor.interpretText()  # 确保取得最新的数值
            model.setData(index, editor.value(), Qt.EditRole)
            return
        elif CTableModel.EAttrIndex.EAttr_Checked == CTableModel.EAttrIndex(idxParent.row()):
            var = editor.currentData()  # 0:yes, 1:no
            model.setData(index, var, Qt.EditRole)
            return
        elif CTableModel.EAttrIndex.EAttr_LastOneFlag == CTableModel.EAttrIndex(idxParent.row()):
            var = (editor.text() == '是' and True or False)
            model.setData(index, var, Qt.EditRole)
            return
        elif CTableModel.EAttrIndex.Eattr_Animate == CTableModel.EAttrIndex(idxParent.row()):
            # 有父项（说明是子属性项），并且是【动画速度】属性项
            if idxParent != index:  # 有父项，说明是子属性项
                if CTableModel.EAttrIndexAnimate.EattrAnimate_AnimateSpeed == CTableModel.EAttrIndexAnimate(
                        index.row()):  # 如果是【动画速度】属性项
                    var = editor.currentData()
                    model.setData(index, var, Qt.EditRole)
                    return
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
