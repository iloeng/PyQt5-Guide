#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.09   21:09
-------------------------------------------------------------------------------
   @Change:   2022.05.09
-------------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from PyQt5.QtCore import QDir
import os


def queryTable():
    sql_query = QSqlQuery()
    # sql_query.exec("select * from people")
    if not sql_query.exec("select * from people"):
        print(sql_query.lastError())
    else:
        id = 0
        name = str()
        weight = 0
        while sql_query.next():
            id = sql_query.value(0)
            name = sql_query.value(1)
            weight = sql_query.value(2)
            print("id:{0}    name:{1}    weight:{2}".format(id, name, weight))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建并打开数据库
    database = QSqlDatabase.addDatabase("QSQLITE")
    strFile = "data.dbfile"
    database.setDatabaseName(strFile)
    database.setUserName("admin")  # 数据库用户名
    database.setPassword("admin1235")  # 数据库密码
    if not database.open():
        print("Error: Failed to add database." + database.lastError().text())
    else:
        print("Info: Succeed to add database.")

    # 创建表
    sql_query = QSqlQuery()
    if not sql_query.exec("create table if not exists people(id int primary key, name text, weight int)"):
        print("Error: Fail to create table." + sql_query.lastError().text())
    else:
        print("Info: Table created!")
    # 插入数据
    if not sql_query.exec("insert into people values(1, \"kangxi\", 80)"):
        print("Error: " + sql_query.lastError().text())
    else:
        print("Info: inserted Alex!")
    if not sql_query.exec("insert into people values(2, \"libai\", 77)"):
        print("Error: " + sql_query.lastError().text())
    else:
        print("Info: inserted Paul!")
    # 查询数据
    queryTable()

    # 批量插入数据
    names = ["zhao", "qian", "sun", "li"]
    # 为每一列标题添加绑定值
    sql_query.prepare("insert into people (id, name, weight) "
                      "values (:id, :name, :weight)")
    id = 3
    # 从names表里获取每个名字
    for name in names:
        sql_query.bindValue(":id", id)  # id
        sql_query.bindValue(":name", name)  # 名字
        sql_query.bindValue(":weight", 80)  # weiht，使用默认值
        sql_query.exec_()  # 插入记录
        id = id + 1
    # 更新数据
    if not sql_query.exec("update people set name = \"Ben\" where id = 1"):
        print(sql_query.lastError().text())
    else:
        print("Info: updated!")
    # 再次查询数据
    queryTable()
    # 删除数据
    if not sql_query.exec("delete from people where id = 1"):
        print(sql_query.lastError().text())
    else:
        print("Info: people deleted!")
    # 删除表
    if not sql_query.exec("drop table people"):
        print(sql_query.lastError().text())
    else:
        print("table cleared")
    # 关闭数据库
    database.close()

# sys.exit(app.exec_())
