from data.model import *

__author__ = 'Juan Manuel Bermúdez Cabrera'


@db_session
def provinces():
    return Provincia.select().order_by(Provincia.nombre)[:]


@db_session
def arteries():
    return TipoArteria.select().order_by(TipoArteria.nombre)[:]


@db_session
def get_patient(patient_id):
    result = select(p for p in Paciente if p.id == patient_id)
    result = result.prefetch(Provincia, APP, Complementario, TAC, TAC.arterias)
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

    if exists(tac for tac in TAC if tac.paciente == patient):
        TAC.get(paciente=patient).delete()

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


@db_session
def set_patient_tac(patient_id, tac_date, angio, art_data):
    tac = TAC(paciente=Paciente[patient_id], fecha=tac_date, angio_ct=angio)
    commit()

    for artery, data in art_data.items():
        Arteria(tipo=TipoArteria[artery], lesiones=data[0], volumen=data[1],
                masa=data[2], calcio=data[3], tac=tac)


@db_session
def update_tac(tac_id, tac_date, angio, art_data):
    tac = TAC[tac_id]
    tac.set(fecha=tac_date, angio_ct=angio)

    for artery, data in art_data.items():
        at = TipoArteria[artery]
        art = select(a for a in Arteria if a.tipo == at and a.tac == tac).first()
        art.set(lesiones=data[0], volumen=data[1], masa=data[2], calcio=data[3])
