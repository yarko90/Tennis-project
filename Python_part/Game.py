__author__ = 'например Андрей'
import uuid


class Game:

    def __init__(self, GUID, tournament, time, players, coeff, result):
        self.tournament = tournament
        self.time = time
        self.players = players
        self.coeff = coeff
        self.result = result
        self.guid = GUID

    @property
    def guid(self):
        return self.__GUID

    @guid.setter
    def guid(self, GUID):
        if (GUID == "new"):
            self.__GUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, self.tournament))
        else:
            self.__GUID = GUID

    #def guid(self):
    #    return self.__GUID