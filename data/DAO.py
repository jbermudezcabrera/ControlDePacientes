# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
import sqlite3 as sql

from data.model import *

@db_session
def provinces():
    return Provincia.select().order_by(Provincia.nombre)[:]


@db_session
def get_patient(patient_id):
    result = select(p for p in Paciente if p.id == patient_id)
    result = result.prefetch(Provincia, APP, Complementario, TAC)
    return result.first()


@db_session
def find_patients(query):
    if len(query) == 0:
        return Paciente.select().prefetch(Provincia, APP, Complementario, TAC)[:]

    if query.isalpha():
        lquery = query.lower()
        result = select(p for p in Paciente if lquery in p.nombre.lower())
        return result.prefetch(Provincia, APP, Complementario, TAC)[:]

    if query.isdigit():
        result = select(p for p in Paciente if query in p.ci)
        return result.prefetch(Provincia, APP, Complementario, TAC)[:]

    return []


def insert_patient(ci, name, age, province_id):
    with db_session:
        p = Paciente(ci=ci, nombre=name, edad=age,
                     provincia=Provincia[province_id])
    return p.id


@db_session
def update_patient(patient_id, ci, name, age, province_id):
    p = Paciente[patient_id]
    p.set(ci=ci, nombre=name, edad=age, provincia=Provincia[province_id])


@db_session
def delete_patient(patient_id):
    patient = Paciente[patient_id]

    # since cascade_delete raises an error, i worked around by deleting manually
    if exists(app for app in APP if app.paciente == patient):
        APP.get(paciente=patient).delete()

    if exists(ac for ac in Complementario if ac.paciente == patient):
        Complementario.get(paciente=patient).delete()

    patient.delete()


@db_session
def set_patient_app(patient_id, hta, ci, hc, ht, dm, smoker, other, idiag):
    APP(paciente=Paciente[patient_id], hta=hta, ci=ci, hc=hc, ht=ht, dm=dm,
        fumador=smoker, otro=other, idiagnostico=idiag)


@db_session
def update_app(app_id, hta, ci, hc, ht, dm, smoker, other, idiag):
    app = APP[app_id]
    app.set(hta=hta, ci=ci, hc=hc, ht=ht, dm=dm, fumador=smoker,
            otro=other, idiagnostico=idiag)


@db_session
def set_patient_ac(patient_id, hb, gli, crea, col, trig, au):
    Complementario(paciente=Paciente[patient_id], hb=hb, glicemia=gli,
                   creatinina=crea, colesterol=col, trigliceridos=trig,
                   acido_urico=au)


@db_session
def update_ac(ac_id, hb, gli, crea, col, trig, au):
    ac = Complementario[ac_id]
    ac.set(hb=hb, glicemia=gli, creatinina=crea, colesterol=col,
           trigliceridos=trig, acido_urico=au)
