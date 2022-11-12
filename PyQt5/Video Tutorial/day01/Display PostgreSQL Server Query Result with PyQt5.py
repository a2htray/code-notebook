# -*- coding=utf-8 -*-
r"""
展示数据库查询结果
"""

import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView, QApplication

conn = None


def createConnection():
    """创建数据库连接"""
    # @link: https://doc.qt.io/qtforpython/overviews/sql-driver.html
    global conn
    conn = QSqlDatabase('QPSQL')
    conn.setHostName('127.0.0.1')
    conn.setPort(5432)
    conn.setDatabaseName('')  # 数据名
    conn.setUserName('postgres')
    conn.setPassword('')  # 密码

    if not conn.open():
        print(f'error: {conn.lastError().text()}')
        return False
    return True


def displayData(sqlStatement):
    qry = QSqlQuery(conn)
    qry.prepare(sqlStatement)
    qry.exec()

    model = QSqlQueryModel()
    model.setQuery(qry)

    view = QTableView()
    view.setModel(model)

    return view


if __name__ == '__main__':
    app = QApplication(sys.argv)

    if createConnection():
        SQL_STATEMENT = 'SELECT * FROM django_content_type;'
        dataView = displayData(SQL_STATEMENT)
        dataView.show()

    app.exit()
    sys.exit(app.exec_())
