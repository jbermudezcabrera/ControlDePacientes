# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
import sqlite3 as sql

from data.model import *

@db_session
def provinces():
    return Provincia.select().order_by(Provincia.nombre)[:]

@db_session
def find_patients(query):
    if len(query) == 0:
        return Paciente.select()[:]

    if query.isalpha():
        lquery = query.lower()
        result = select(p for p in Paciente if lquery in p.nombre.lower())
        return result.order_by(Paciente.nombre)[:]

    if query.isdigit():
        result = select(p for p in Paciente if query in p.ci)
        return result.order_by(Paciente.nombre)[:]

    return []

def insert_patient(ci, name, age, province_id):
    with db_session:
        p = Paciente(ci=ci, nombre=name, edad=age,
                     provincia=Provincia[province_id])
    return p.id

@db_session
def set_patient_app(patient_id, hta, ci, hc, ht, dm, smoker, other, idiag):
    APP(paciente=Paciente[patient_id], hta=hta, ci=ci, hc=hc, ht=ht, dm=dm,
        fumador=smoker, otro=other, idiagnostico=idiag)

@db_session
def update_patient(patient_id, ci, name, age, province_id, app=None,
                   ac=None, tac=None):
    p = Paciente[patient_id]
    p.set(ci=ci, nombre=name, edad=age, provincia=Provincia[province_id],
          app=app, ac=ac, tac=tac)

@db_session
def delete_patient(patient_id):
    Paciente[patient_id].delete()

@db_session
def get_patient(patient_id):
    return Paciente[patient_id]
