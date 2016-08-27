from data import dao

__author__ = 'Juan Manuel Bermúdez Cabrera'


def provinces():
    return dao.provinces()


def arteries():
    return dao.arteries()


def find_patients(search_text):
    return dao.find_patients(search_text)


def add_patient(ci, name, age, province_id):
    return dao.insert_patient(ci, name, age, province_id)


def update_patient(patient_id, ci, name, age, province_id):
    dao.update_patient(patient_id, ci, name, age, province_id)


def delete_patient(patient_id):
    dao.delete_patient(patient_id)


def set_patient_app(patient_id, hta, ci, hc, ht, dm, smoker, other, idiag):
    dao.set_patient_app(patient_id, hta, ci, hc, ht, dm, smoker, other, idiag)


def update_tac(tac_id, date, angio, arteries):
    dao.update_tac(tac_id, date, angio, arteries)


def set_patient_tac(patient_id, date, angio, arteries):
    dao.set_patient_tac(patient_id, date, angio, arteries)


def update_ac(ac_id, hb, gli, crea, col, trig, au):
    dao.update_ac(ac_id, hb, gli, crea, col, trig, au)


def set_patient_ac(patient_id, hb, gli, crea, col, trig, au):
    dao.set_patient_ac(patient_id, hb, gli, crea, col, trig, au)


def update_app(app_id, hta, ci, hc, ht, dm, smoker, other, idiag):
    dao.update_app(app_id, hta, ci, hc, ht, dm, smoker, other, idiag)


def patient(patient_id):
    return dao.get_patient(patient_id)
