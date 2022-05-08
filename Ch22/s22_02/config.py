# -*- coding: utf-8 -*-

import types


class CSingleton(type):
    _instance = None

    def __call__(self, *args, **kw):
        if self._instance is None:
            self._instance = super().__call__(*args, **kw)
        return self._instance


def singleton(cls, *args, **kwargs):
    instances = {}

    def wrapper():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class CConfig:
    nTeacherNumber = 0
    nStudentNumber = 0

    def __init__(self):
        pass

    def setTeacherNumber(self, n):
        self.nTeacherNumber = n

    def getTeacherNumber(self):
        return self.nTeacherNumber

    def setStudentNumber(self, n):
        self.nStudentNumber = n

    def getStudentNumber(self):
        return self.nStudentNumber
