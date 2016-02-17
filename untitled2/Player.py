__author__ = 'например Андрей'
import uuid


class Player:

    def __init__(self, GUID, name, totalGames, winRate, svoiPodachi, chuzPodachi, setRate, gameRate, breakePoint):
        if (GUID == "new"):
            self._GUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, name))
        else:
            self._GUID = GUID
        self.name = name
        self.total_games = totalGames
        self.win_rate = winRate
        self.svoi_podachi = svoiPodachi
        self.chuz_podachi = chuzPodachi
        self.set_rate = setRate
        self.game_rate = gameRate
        self.break_point = breakePoint

    #def guid(self):
    #    return self.__GUID