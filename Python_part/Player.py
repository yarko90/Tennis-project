__author__ = 'например Андрей'
import uuid


class Player:

    def __init__(self, GUID, name, totalGames, winRate, svoiPodachi, chuzPodachi, setRate, gameRate, breakePoint):
        self.name = name
        self.total_games = totalGames
        self.win_rate = winRate
        self.svoi_podachi = svoiPodachi
        self.chuz_podachi = chuzPodachi
        self.set_rate = setRate
        self.game_rate = gameRate
        self.break_point = breakePoint
        self.guid = GUID

    @property
    def guid(self):
        return self.__GUID

    @guid.setter
    def guid(self, GUID):
        if (GUID == "new"):
            self.__GUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, self.name))
        else:
            self.__GUID = GUID

    #def guid(self):
    #    return self.__GUID