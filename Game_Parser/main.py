__author__ = 'например Андрей'
import urllib.request as url
import itertools
import re
import requests
from bs4 import BeautifulSoup

class Game_parser():
    URL = "http://www.gotennis.ru/players/live/yesterday/"

    def get_soup(self):
        request=url.Request(self.URL)
        data=url.urlopen(request)
        table_of_games=BeautifulSoup(data.read(),"html.parser")
        #print (table_of_games.find_all('div', id='liveContent'))
        players1 = self.get_info(table_of_games.find_all('tr', class_='first'))
        players2 = self.get_info(table_of_games.find_all('tr', class_='second'))
        i = 0
        print (len(players1), len(players2))
        for player1, player2 in zip(players1, players2):
            i += 1
            print (i,player1,"\n",player2)

    #def get_players (selfsoup):
    #    playerlist = {}
    #    i = 0
    #    for player in soup:
    #        if player.find('span') is not None:
    #            playerlist[i] = player.find('span').get_text()
    #        else:
    #            playerlist[i] = player.find('a').get_text()
    #        i+=1
    #    return playerlist


    def get_info(self,soup):
        infolist=[]
        for soup_line in soup:
            #line = soup_line.get_text().replace('\n','')
            line = re.split(r'\n',soup_line.get_text())
            #print (sorted(line))
            for element in sorted(line):
                g = str(element).find('\xa0')
                if g != -1:
                #    element = str(element)[:g]
                    element = element.replace(u'\xa0',' ')
            for element in sorted(line):
                if (element == '')|(element ==' '):
                    line.remove(element)
                    continue
            infolist.append(line)
        return infolist


parser = Game_parser()
parser.get_soup()