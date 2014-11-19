# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

from core import DAO

class Controller():

    @property
    def provinces(self):
        return DAO.provinces()
