# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

from data import DAO

class Controller():

    @property
    def provinces(self):
        return DAO.provinces()

    def find_patients(self, search_text):
        return DAO.find_patients(search_text)
