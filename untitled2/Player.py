__author__ = 'например Андрей'
import psycopg2
import os
import re
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

    # def __init__(self, name):
    #    self.name=name
    #    self.GUID=str(uuid.uuid5(uuid.NAMESPACE_DNS, name))
    #    self.total_games=1
    #    self.win_rate="0/0"
    #    self.svoi_podachi="0/0"
    #    self.chuz_podachi="0/0"
    def __init__(self, GUID, name, totalGames, winRate, svoiPodachi, chuzPodachi, setRate, gameRate, breakePoint):
        if (GUID == "new"):
            self.GUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, name))
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
