__author__ = 'например Андрей'
import uuid


class Player:
    name = ""
    GUID = ""
    total_games = ""
    win_rate = ""
    svoi_podachi = ""
    chuz_podachi = ""
    set_rate = ""
    game_rate = ""
    break_point = ""

    def __init__(self, GUID, name, totalGames, winRate, svoiPodachi, chuzPodachi, setRate, gameRate, breakePoint):
        if (GUID == "new"):
            self.__GUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, name))
        else:
            self.__GUID = GUID
        self.name = name
        self.total_games = totalGames
        self.win_rate = winRate
        self.svoi_podachi = svoiPodachi
        self.chuz_podachi = chuzPodachi
        self.set_rate = setRate
        self.game_rate = gameRate
        self.break_point = breakePoint
