__author__ = 'например Андрей'
import uuid


class Game:

    def __init__(self, GUID, tournament, time, players, coeff, result):
        if (GUID == "new"):
            self._GUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, tournament))
        else:
            self._GUID = GUID
        self.tournament = tournament
        self.time = time
        self.players = players
        self.coeff = coeff
        self.result = result


    def guid(self):
        return self.__GUID