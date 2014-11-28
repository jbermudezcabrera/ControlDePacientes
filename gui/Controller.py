# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

from data import DAO


class Controller():

    @property
    def provinces(self):
        return DAO.provinces()

    @property
    def arteries(self):
        return DAO.arteries()

    @staticmethod
    def patient(patient_id):
        return DAO.get_patient(patient_id)

    @staticmethod
    def find_patients(search_text):
        return DAO.find_patients(search_text)

    @staticmethod
    def add_patient(ci, name, age, province_id):
        return DAO.insert_patient(ci, name, age, province_id)

    @staticmethod
    def update_patient(patient_id, ci, name, age, province_id):
        DAO.update_patient(patient_id, ci, name, age, province_id)

    @staticmethod
    def delete_patient(patient_id):
        DAO.delete_patient(patient_id)

    @staticmethod
    def set_patient_app(patient_id, hta, ci, hc, ht, dm, smoker, other, idiag):
        DAO.set_patient_app(patient_id, hta, ci, hc, ht, dm, smoker, other, idiag)

    @staticmethod
    def update_app(app_id, hta, ci, hc, ht, dm, smoker, other, idiag):
        DAO.update_app(app_id, hta, ci, hc, ht, dm, smoker, other, idiag)

    @staticmethod
    def set_patient_ac(patient_id, hb, gli, crea, col, trig, au):
        DAO.set_patient_ac(patient_id, hb, gli, crea, col, trig, au)

    @staticmethod
    def update_ac(ac_id, hb, gli, crea, col, trig, au):
        DAO.update_ac(ac_id, hb, gli, crea, col, trig, au)

    @staticmethod
    def set_patient_tac(patient_id, date, angio, arteries):
        DAO.set_patient_tac(patient_id, date, angio, arteries)

    @staticmethod
    def update_tac(tac_id, date, angio, arteries):
        DAO.update_tac(tac_id, date, angio, arteries)
