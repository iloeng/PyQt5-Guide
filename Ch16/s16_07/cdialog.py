# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QStackedLayout
from Ch16.s16_07.ks16_07_rc import *
from Ch16.s16_07.ui_dialog import *
from Ch16.s16_07.cstep1 import CStep1
from Ch16.s16_07.cstep2 import CStep2
from Ch16.s16_07.cstep3 import CStep3


class CDialog(QDialog, Ui_CDialog):
    def __init__(self, parent=None):
        super(CDialog, self).__init__(parent)
        self.setupUi(self)
        # 构建QStackedLayout布局对象、3个子向导界面对象
        stackedLayout = QStackedLayout(self.horizontalLayout)
        widgetStep1 = CStep1(self)
        widgetStep2 = CStep2(self)
        widgetStep3 = CStep3(self)

        # 将3个子向导界面对象添加到堆栈布局
        stackedLayout.addWidget(widgetStep1)
        stackedLayout.addWidget(widgetStep2)
        stackedLayout.addWidget(widgetStep3)

        # 设置默认页
        stackedLayout.setCurrentIndex(0)

        # 将堆栈布局添加到父窗口的布局对象中
        # self.horizontalLayout.addLayout(stackedLayout)

        # 绑定信号槽:将子向导界面的信号绑定到堆栈布局对象的槽函数
        widgetStep1.sig_showPage.connect(stackedLayout.setCurrentIndex)
        widgetStep2.sig_showPage.connect(stackedLayout.setCurrentIndex)
        widgetStep3.sig_showPage.connect(stackedLayout.setCurrentIndex)
        widgetStep3.sig_closeWindow.connect(self.close)
