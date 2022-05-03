# -*- coding: utf-8 -*-
""" 
CTableModel类定义文件
"""

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt, QVariant
from enum import IntEnum, Enum


class CTableModel(QStandardItemModel):
    # 各属性项枚举
    class EAttrIndex(IntEnum):
        EAttr_Id = 0  # id
        EAttr_Descrition = 1  # 描述
        EAttr_Checked = 2  # 是否已验证
        EAttr_LastOneFlag = 3  # 是否最后一个
        Eattr_AnimateSpeed = 4  # 动画速度
        Eattr_Max = 5

    # 速度枚举值
    class EAnimateSpeed(Enum):
        EAnimateSpeed_Slow = 0  # 慢速
        EAnimateSpeed_Normal = 1  # 中速
        EAnimateSpeed_Fast = 2  # 快速
        EAnimateSpeed_Max = 3

    def __init__(self, rows, columns, parent=None):
        super(CTableModel, self).__init__(rows, columns, parent)

    def flags(self, index):
        # 只有第1列允许被编辑
        itemFlags = Qt.ItemFlags(0)
        if 1 != index.column():
            itemFlags &= (
                ~Qt.ItemIsEditable)  # Qt.ItemIsEditable表示可编辑，~Qt.ItemIsEditable表示取反，即不可编辑。
            return itemFlags
        else:
            return QStandardItemModel.flags(self, index)

    def data(self, index, role):
        if Qt.EditRole == role:
            return QStandardItemModel.data(self, index, role)
        elif Qt.DisplayRole != role:
            return QStandardItemModel.data(self, index, role)
        var = self.data(index, Qt.EditRole)
        var = QVariant(var)
        if 0 == index.column():
            return var
        if CTableModel.EAttrIndex.EAttr_Checked == CTableModel.EAttrIndex(index.row()):
            var = (var.value() and 'no' or 'yes')  # 0:yes, 1:no
        elif CTableModel.EAttrIndex.EAttr_LastOneFlag == CTableModel.EAttrIndex(index.row()):
            var = (var.value() and True or False)  # 0:False, other:True
        elif CTableModel.EAttrIndex.Eattr_AnimateSpeed == CTableModel.EAttrIndex(index.row()):
            eSpeed = CTableModel.EAnimateSpeed(var.value())
            if eSpeed == CTableModel.EAnimateSpeed.EAnimateSpeed_Slow:
                var = '慢速'
            elif eSpeed == CTableModel.EAnimateSpeed.EAnimateSpeed_Normal:
                var = '中速'
            elif eSpeed == CTableModel.EAnimateSpeed.EAnimateSpeed_Fast:
                var = '快速'
            else:
                var = ''
        return var

    def setData(self, index, value, role):
        if Qt.EditRole == role:
            return QStandardItemModel.setData(self, index, value, role)
        else:
            return False
