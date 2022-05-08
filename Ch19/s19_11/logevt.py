# -*- coding: utf-8 -*-
from PyQt5.QtCore import QTime, QEvent
from enum import Enum


# 日志级别枚举
class ELogLevel(Enum):
    ELogLevel_Error = 1  # 错误
    ELogLevel_Warning = 2  # 警告
    ELogLevel_Normal = 3  # 一般


# 日志结构
class SLog:
    level = ELogLevel.ELogLevel_Normal  # 日志级别
    msg = str()  # 日志内容
    time = QTime()  # 接收日志时间

    @staticmethod
    def translateLevel(level):
        if ELogLevel.ELogLevel_Error == level:
            return "Error"
        if ELogLevel.ELogLevel_Warning == level:
            return "Warning"
        if ELogLevel.ELogLevel_Normal == level:
            return "Normal"
        else:
            return ''


# CLogEvt
class CLogEvt(QEvent):
    ELogEvt_LogOut = QEvent.User + 1
    log = SLog()

    def __init__(self, nType=ELogEvt_LogOut):
        super(CLogEvt, self).__init__(QEvent.Type(nType))

    def __del__(self):
        pass

    def getLog(self):
        return self.log

    def setLog(self, log):
        self.log = log
