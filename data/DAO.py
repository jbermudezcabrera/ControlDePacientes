# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
import sqlite3 as sql

import pony.orm as pony

from data.model import *

@pony.db_session
def provinces():
    return Provincia.select().order_by(Provincia.nombre)[:]

@pony.db_session
def find_patients(query):
    if len(query) == 0:
        return Paciente.select()[:]

    if query.isalpha():
        lquery = query.lower()
        result = pony.select(p for p in Paciente if lquery in p.nombre.lower())
        return result.order_by(Paciente.nombre)[:]

    if query.isdigit():
        result = pony.select(p for p in Paciente if query in p.ci)
        return result.order_by(Paciente.nombre)[:]

    return []

@pony.db_session
def save_patient(ci, name, age, province_id):
    Paciente(ci=ci, nombre=name, edad=age, provincia=Provincia[province_id])

@pony.db_session
def get_patient(id):
    return Paciente[id]
