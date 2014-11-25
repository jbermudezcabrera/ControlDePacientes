# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
from datetime import date

from pony.orm import *

db_path = os.path.join('../resources', 'Pacientes.sqlite')
db = Database("sqlite", db_path, create_db=True)


class Provincia(db.Entity):
    nombre = Required(str)
    pacientes = Set('Paciente')


class Arteria(db.Entity):
    nombre = Required(str)

    masa = Required(float)
    calcio = Required(float)
    volumen = Required(float)
    lesiones = Required(int, min=0)

    tac = Required('TAC')


class APP(db.Entity):
    ci = Required(bool)
    hc = Required(bool)
    ht = Required(bool)
    hta = Required(bool)

    dm = Required(int, min=0, max=2)
    fumador = Required(int, min=0, max=2)

    otro = Optional(str)
    idiagnostico = Optional(str)

    paciente = Required('Paciente')


class Complementario(db.Entity):
    hb = Required(float)
    creatinina = Required(float)
    colesterol = Required(float)
    acido_urico = Required(float)
    trigliceridos = Required(float)
    glicemia = Required(float, min=0)

    paciente = Required('Paciente')


class TAC(db.Entity):
    fecha = Required(date)
    angio_ct = Required(str)

    arterias = Set(Arteria, cascade_delete=True)
    paciente = Required('Paciente')


class Paciente(db.Entity):
    ci = Required(str)
    edad = Required(int)
    nombre = Required(str)

    provincia = Required(Provincia)
    app = Optional(APP, cascade_delete=True)
    tac = Optional(TAC, cascade_delete=True)
    complementario = Optional(Complementario, cascade_delete=True)


db.generate_mapping(check_tables=True, create_tables=True)

with db_session:
    if len(Provincia.select()) == 0:
        Provincia(nombre='Villa Clara')
        Provincia(nombre='Cienfuegos')
        Provincia(nombre='Sancti Spíritus')
