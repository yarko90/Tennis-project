__author__ = 'например Андрей'
# coding: utf8
import unicodedata
import urllib.request as url
import itertools
import re
import requests
from bs4 import BeautifulSoup
from Game import Game


class Game_parser():
    URL = "http://www.gotennis.ru/players/live/yesterday/"

    def get_soup(self):
        games = []
        request = url.Request(self.URL)
        data = url.urlopen(request)
        table_of_games = BeautifulSoup(data.read(), "html.parser")
        # print (table_of_games.find_all('div', id='liveContent'))
        players1 = self.get_info(table_of_games.find_all('tr', class_='first'))
        players2 = self.get_info(table_of_games.find_all('tr', class_='second'))
        i = 0
        #print(len(players1), len(players2))
        for player1, player2 in zip(players1, players2):
            i += 1
            print(i, player1, "\n", player2)
            tournament = player1[2]
            players = '{} против {}'.format(player1[0], player2[0])
            time = str(player1[3])
            GUID = 'new'
            coeff = str(player1[1]+'/'+player2[1])
            result = player1[3]
            game = Game(GUID, tournament, time, players, coeff, result)
            games.append(game)
        return games

    def get_info(self, soup):
        infolist = []
        for soup_line in soup:
            line = re.split(r'\n', soup_line.get_text())
            i = []
            for element in sorted(line):
                g = element.find('\xa0')
                if g != -1:
                    line.append(element.replace('\xa0', ' '))
                    line.remove(element)
            for element in sorted(line):
                if (element == '') | (element == ' '):
                    line.remove(element)
            infolist.append(line)
        return infolist


parser = Game_parser()
parser.get_soup()