__author__ = 'например Андрей'
import psycopg2
import os
import re
import uuid


class Game:
    GUID = ""
    tournament = ""
    time = ""
    players = ""
    coeff = ""
    result = ""

    def __init__(self, GUID, tournament, time, players, coeff, result):
        if (GUID == "new"):
            self.GUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, tournament))
        else:
            self.__GUID = GUID
        self.tournament = tournament
        self.time = time
        self.players = players
        self.coeff = coeff
        self.result = result