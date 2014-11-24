# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

from data import DAO


class Controller():

    @property
    def provinces(self):
        return DAO.provinces()

    @staticmethod
    def find_patients(search_text):
        return DAO.find_patients(search_text)

    @staticmethod
    def add_patient(ci, name, age, province_id):
        DAO.save_patient(ci, name, age, province_id)

    @staticmethod
    def update_patient(patient_id, ci, name, age, province_id):
        DAO.update_patient(patient_id, ci, name, age, province_id)

    @staticmethod
    def delete_patient(patient_id):
        DAO.delete_patient(patient_id)

    @staticmethod
    def patient(patient_id):
        return DAO.get_patient(patient_id)
