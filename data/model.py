import os
from datetime import date

from pony.orm import *

__author__ = 'Juan Manuel Bermúdez Cabrera'

db_path = os.path.join('../resources', 'Pacientes.sqlite')
db = Database("sqlite", db_path, create_db=True)


class Provincia(db.Entity):
    nombre = Required(str)
    pacientes = Set('Paciente')


class TipoArteria(db.Entity):
    nombre = Required(str)
    arterias = Set('Arteria')


class Arteria(db.Entity):
    tipo = Required(TipoArteria)

    lesiones = Required(int, min=0, max=150)
    volumen = Required(float, min=0)
    masa = Required(float, min=0)
    calcio = Required(float, min=0)

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
    hb = Required(float, min=0, max=20)
    glicemia = Required(float, min=0, max=20)
    colesterol = Required(float, min=0, max=20)
    trigliceridos = Required(float, min=0, max=20)
    creatinina = Required(float, min=0, max=200)
    acido_urico = Required(float, min=0, max=1000)

    paciente = Required('Paciente')


class TAC(db.Entity):
    fecha = Required(date)
    angio_ct = Optional(str)

    arterias = Set(Arteria, cascade_delete=True)
    paciente = Required('Paciente')


class Paciente(db.Entity):
    ci = Required(str, unique=True)
    edad = Required(int)
    nombre = Required(str)

    provincia = Required(Provincia)
    app = Optional(APP, cascade_delete=True)
    tac = Optional(TAC, cascade_delete=True)
    complementario = Optional(Complementario, cascade_delete=True)


db.generate_mapping(check_tables=True, create_tables=True)

with db_session:
    if not Provincia.select():
        Provincia(nombre='Villa Clara')
        Provincia(nombre='Cienfuegos')
        Provincia(nombre='Sancti Spíritus')
        Provincia(nombre='Ciego de Ávila')

    if not TipoArteria.select():
        TipoArteria(nombre='Tronco')
        TipoArteria(nombre='DA')
        TipoArteria(nombre='CX')
        TipoArteria(nombre='CD')
