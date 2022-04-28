#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.28   23:51
-------------------------------------------------------------------------------
   @Change:   2022.04.28
-------------------------------------------------------------------------------
"""

import sys
from PyQt5.QtCore import QObject, pyqtSignal


class CObjectA(QObject):
    # 对象A
    # 不带参数的信号
    sig_no_parameter = pyqtSignal()
    # 带1个float参数的信号
    sig_float_parameter = pyqtSignal(float)
    # 带1个int或str参数的重载信号
    sig_in_or_str_parameter = pyqtSignal([int], [str])
    # 带2参数(int,int)的信号
    sig_two_parameter = pyqtSignal(int, int)
    # 带2参数([int,str]或[int, float])的重载信号
    sig_two_parameter_overload = pyqtSignal([int, str], [int, float])

    def __init__(self):
        super(CObjectA, self).__init__()

    # 模拟发射信号
    def emission_simulate_no_parameter(self):
        print("emit signal sig_no_parameter.")
        # 发射信号
        self.sig_no_parameter.emit()

    # 模拟发射信号
    def emission_simulate_one_parameter(self, fValue):
        print("emit signal sig_float_parameter.")
        # 发射信号
        self.sig_float_parameter.emit(fValue)

    # 模拟发射信号
    def emission_simulate_one_parameter_overload_int(self, value):
        print("emit signal sig_in_or_str_parameter_int.")
        # 发射信号
        self.sig_in_or_str_parameter[int].emit(value)

    # 模拟发射信号
    def emission_simulate_one_parameter_overload_str(self, strValue):
        print("emit signal sig_in_or_str_parameter_str.")
        # 发射信号
        self.sig_in_or_str_parameter[str].emit(strValue)

    # 模拟发射信号
    def emission_simulate_two_parameter(self, iValue1, iValue2):
        print("emit signal sig_two_parameter.")
        # 发射信号
        self.sig_two_parameter.emit(iValue1, iValue2)

    # 模拟发射信号
    def emission_simulate_two_parameter_int_str(self, iValue, strValue):
        print("emit signal sig_two_parameter_overload_int_str.")
        # 发射信号
        self.sig_two_parameter_overload[int, str].emit(iValue, strValue)

    # 模拟发射信号
    def emission_simulate_two_parameter_int_float(self, iValue, fValue):
        print("emit signal sig_two_parameter_overload_int_float.")
        # 发射信号
        self.sig_two_parameter_overload[int, float].emit(iValue, fValue)


class CObjectB(QObject):
    # 对象B

    def __init__(self):
        super(CObjectB, self).__init__()

    # 槽函数
    def slot_no_parameter(self):
        print("slot__no_parameter called.")

    # 槽函数
    def slot_one_parameter(self, fValue):
        print("slot_one_parameter called.")

    # 槽函数
    def slot_one_parameter_int(self, iValue):
        print("slot_one_parameter_int called.")

    # 槽函数
    def slot_one_parameter_str(self, strValue):
        print("slot_one_parameter_str called.")

    # 槽函数
    def slot_two_parameter(self, iValue1, iValue2):
        print("slot_two_parameter called.")

    # 槽函数
    def slot_two_parameter_int_str(self, iValue, strValue):
        print("slot_two_parameter_int_str called.")

    # 槽函数
    def slot_two_parameter_int_float(self, iValue, fValue):
        print("slot_two_parameter_int_float called.")


if __name__ == "__main__":
    print("\nstart working...")
    objectA = CObjectA()
    objectB = CObjectB()
    # 将信号关联到槽函数
    objectA.sig_no_parameter.connect(objectB.slot_no_parameter)
    objectA.sig_float_parameter.connect(objectB.slot_one_parameter)
    objectA.sig_in_or_str_parameter[int].connect(objectB.slot_one_parameter_int)
    objectA.sig_in_or_str_parameter[str].connect(objectB.slot_one_parameter_str)
    objectA.sig_two_parameter.connect(objectB.slot_two_parameter)
    objectA.sig_two_parameter_overload[int, str].connect(objectB.slot_two_parameter_int_str)
    objectA.sig_two_parameter_overload[int, float].connect(objectB.slot_two_parameter_int_float)
    # 模拟信号发射
    objectA.emission_simulate_no_parameter()
    objectA.emission_simulate_one_parameter(15.6)
    objectA.emission_simulate_one_parameter_overload_int(100)
    objectA.emission_simulate_one_parameter_overload_str('iDev')
    objectA.emission_simulate_two_parameter(20, 30)
    objectA.emission_simulate_two_parameter_int_str(50, 'iDev')
    objectA.emission_simulate_two_parameter_int_float(60, 89.3)
    print("exit.")
