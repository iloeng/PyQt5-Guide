# -*- coding: utf-8 -*-
""" 
CTableModel 类定义文件
"""

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt, QVariant, QModelIndex
from enum import IntEnum, Enum


class CTableModel(QStandardItemModel):
    # 各属性项枚举
    class EAttrIndex(IntEnum):
        EAttr_Id = 0  # id
        EAttr_Descrition = 1  # 描述
        EAttr_Checked = 2  # 是否已验证
        EAttr_LastOneFlag = 3  # 是否最后一个
        Eattr_Animate = 4  # 动画
        Eattr_Max = 5

    # 动画的子属性项枚举
    class EAttrIndexAnimate(IntEnum):
        EattrAnimate_AnimateType = 0  # 动画类型
        EattrAnimate_AnimateSpeed = 1  # 动画速度
        EattrAnimate_Max = 2

    # 速度枚举值
    class EAnimateSpeed(IntEnum):
        EAnimateSpeed_Slow = 0  # 慢速
        EAnimateSpeed_Normal = 1  # 中速
        EAnimateSpeed_Fast = 2  # 快速
        EAnimateSpeed_Max = 3

    def __init__(self, rows, columns, parent=None):
        super(CTableModel, self).__init__(rows, columns, parent)

    def flags(self, dataIndex):
        itemFlags = Qt.ItemFlags(0)
        # 只有第1列允许被编辑
        if 1 != dataIndex.column():
            return itemFlags
        if dataIndex.parent().isValid():  # 是子数据项
            itemFlags = Qt.ItemFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
            if dataIndex.row() == 4 and dataIndex.column() == 1:
                print(dataIndex.row(), dataIndex.column(), "aa")
            return itemFlags
        else:  # 是根数据项
            if self.hasChildren(
                    self.index(dataIndex.row(), 0, dataIndex.parent())):  # 有子数据项，则父项本身不允许编辑
                itemFlags = Qt.ItemFlags(0)  # itemFlags &= ~Qt.ItemIsEnabled
            else:  # 无子数据项，则本身允许编辑
                itemFlags = Qt.ItemFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
        return itemFlags

    def data(self, index, role):
        idxParent = (index.parent().isValid() and index.parent() or index)

        if 0 == index.column():
            return QStandardItemModel.data(self, index, role)
        if Qt.EditRole == role:
            return QStandardItemModel.data(self, index, role)
        elif Qt.DisplayRole != role:
            return QStandardItemModel.data(self, index, role)
        var = self.data(index, Qt.EditRole)
        var = QVariant(var)
        if CTableModel.EAttrIndex.EAttr_Checked == CTableModel.EAttrIndex(idxParent.row()):
            var = (var.value() and 'no' or 'yes')  # 0:yes, 1:no
        elif CTableModel.EAttrIndex.EAttr_LastOneFlag == CTableModel.EAttrIndex(idxParent.row()):
            var = (var.value() and True or False)  # 0:False, other:True
        elif CTableModel.EAttrIndex.Eattr_Animate == CTableModel.EAttrIndex(idxParent.row()):
            if idxParent != index:  # 有父项，说明是子属性项
                if CTableModel.EAttrIndexAnimate.EattrAnimate_AnimateSpeed == \
                        CTableModel.EAttrIndexAnimate(index.row()):  # 如果是【动画速度】属性项
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
        if (Qt.EditRole == role):
            return QStandardItemModel.setData(self, index, value, role)
        else:
            return False
