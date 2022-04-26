#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.26   23:37
-------------------------------------------------------------------------------
   @Change:   2022.04.26
-------------------------------------------------------------------------------
"""

# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QObject, pyqtSignal


class CObjectA(QObject):
    # 对象A
    # 定义一个信号
    sig_message = pyqtSignal()

    def __init__(self):
        super(CObjectA, self).__init__()

    def emission_simulate(self):
        # 模拟发射信号
        print("emit signal sig_message")
        # 发射信号
        self.sig_message.emit()


class CObjectB(QObject):
    # 对象B

    def __init__(self):
        super(CObjectB, self).__init__()

    def slot_receive(self):
        # 槽函数
        self.test = 'slot_receive'
        print(self.test + "receive signal sig_message and slot_receive called")


if __name__ == "__main__":
    print("\nstart working...")
    objectA = CObjectA()
    objectB = CObjectB()

    # 将信号关联到槽函数
    objectA.sig_message.connect(objectB.slot_receive)

    # 模拟信号发射
    objectA.emission_simulate()

    print("exit.")


