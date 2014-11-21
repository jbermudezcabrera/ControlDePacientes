# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
import sqlite3 as sql

import pony.orm as pony

from data.model import *

@pony.db_session
def provinces():
    return Provincia.select()[:]

@pony.db_session
def find_patients(query):
    if len(query) == 0:
        return Paciente.select()[:]

    if query.isalpha():
        lquery = query.lower()
        return pony.select(p for p in Paciente if lquery in p.nombre.lower())[:]

    if query.isdigit():
        return pony.select(p for p in Paciente if query in p.ci)[:]

    return []

@pony.db_session
def save_patient(ci, name, age, province_id):
    Paciente(ci=ci, nombre=name, edad=age, provincia=Provincia[province_id])
