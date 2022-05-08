# -*- coding: utf-8 -*-
"""

"""
from PyQt5.QtCore import QEvent


class CCustomEvent(QEvent):
    def __init__(self):
        super(CCustomEvent, self).__init__(QEvent.Type(QEvent.User + 1))

    def setTeacherNumber(self, n):
        self.nTeacherNumber = n

    def getTeacherNumber(self):
        return self.nTeacherNumber

    def setStudentNumber(self, n):
        self.nStudentNumber = n

    def getStudentNumber(self):
        return self.nStudentNumber
