# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
import sqlite3 as sql


def __connect():
    return sql.connect(os.path.join('resources', 'Pacientes.sqlite'))


def provinces():
    query = 'SELECT ID, nombre FROM Provincias ORDER BY nombre'

    con = __connect()
    id_to_name = dict(con.execute(query))
    con.close()

    return id_to_name


def find_patients(query):
    con = __connect()

    if len(query) == 0:
        sql_query = 'SELECT * FROM Pacientes'
        result = dict(con.execute(sql_query))
    elif query.isalpha():
        sql_query = 'SELECT * FROM Pacientes WHERE nombre LIKE ?'
        result = dict(con.execute(sql_query, ('%' + query + '%', )))
    elif query.isdigit():
        sql_query = 'SELECT * FROM Pacientes WHERE CI LIKE ?'
        result = dict(con.execute(sql_query, ('%' + query + '%', )))
    else:
        result = {}

    con.close()
    return result
