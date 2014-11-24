# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
from datetime import date

import pony.orm as pony

db_path = os.path.join('../resources', 'Pacientes.sqlite')
db = pony.Database("sqlite", db_path, create_db=True)

class Provincia(db.Entity):
    nombre = pony.Required(str)
    paciente = pony.Set('Paciente')

class APP(db.Entity):
    hta = pony.Required(bool)
    dm = pony.Required(int)
    ci = pony.Required(bool)
    fumador = pony.Required(int)
    hc = pony.Required(bool)
    ht = pony.Required(bool)
    otro = pony.Required(str)
    idiagnostico = pony.Required(str)
    paciente = pony.Required('Paciente')

class Complementario(db.Entity):
    hb = pony.Required(float)
    glicemia = pony.Required(float)
    creatinina = pony.Required(float)
    colesterol = pony.Required(float)
    trigliceridos = pony.Required(float)
    acido_urico = pony.Required(float)
    paciente = pony.Required('Paciente')

class Arteria(db.Entity):
    nombre = pony.Required(str)
    lesiones = pony.Required(int)
    volumen = pony.Required(float)
    masa = pony.Required(float)
    calcio = pony.Required(float)

    tac = pony.Required('TAC')

class TAC(db.Entity):
    angio_ct = pony.Required(int)
    fecha = pony.Required(date)

    paciente = pony.Required('Paciente')
    arterias = pony.Set(Arteria)

class Paciente(db.Entity):
    ci = pony.Required(str)
    nombre = pony.Required(str)
    edad = pony.Required(int)

    provincia = pony.Required(Provincia)
    app = pony.Optional(APP)
    complementario = pony.Optional(Complementario)
    tac = pony.Optional(TAC)

db.generate_mapping(check_tables=True, create_tables=True)

with pony.db_session:
    Provincia(nombre='Villa Clara')
    Provincia(nombre='Cienfuegos')
    Provincia(nombre='Sancti Spíritus')
