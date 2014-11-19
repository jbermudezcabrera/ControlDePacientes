# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
import sqlite3 as sql

def __connect():
    return sql.connect(os.path.join('resources', 'Pacientes.sqlite'))

def provinces():
    query = 'SELECT ID, nombre FROM Provincias'

    con = __connect()
    id_to_name = dict(con.execute(query))
    con.close()

    return id_to_name
