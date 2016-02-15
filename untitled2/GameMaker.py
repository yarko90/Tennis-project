__author__ = 'например Андрей'
# coding: utf8
import psycopg2
import os
import re
import Game
import StatPlayer
import RenewPlayerInfo
import random
from datetime import datetime, date, time
import shutil
# Обработка информации из файла, обновление статистики по игрокам в БД
#def MakeGameFile (playersLine, f):
#    players=playersLine[0:-2].split(" ")
#    playerList=[]
#    #
#    #gameStat=RenewPlayerInfo.RenewPlayerInfo(f)
#    gameStat=StatPlayer.RenewPlayerInfo(f)
#    if gameStat!=0:
#        for prePlayer in players:
#            midPlayer=""
#            for letter in prePlayer:
#                if (letter!=","):
#                    if (letter=="-" or letter=="/" or letter==" " or letter=="." or letter=="," or letter=="'"):
#                        midPlayer = midPlayer+" "
#                    else:
#                        midPlayer = midPlayer+letter
#            playerName=midPlayer
#            midPlayer=""
#            try:
#                cur.execute("""SELECT "name","GUID","total_games", "win_rate", "svoi_podachi", "chuz_podachi", "set_rate", "game_rate", "break_point" FROM one_player WHERE "name"=%s""", (playerName,))
#                #print (cur.fetchone())#total_games=str(int(cur.fetchone()[0])+1)
#                PInfo=cur.fetchone()
#                player = Player.Player(PInfo[1],PInfo[0],str(int(PInfo[2])+1),PInfo[3],PInfo[4],PInfo[5],PInfo[6],PInfo[7],PInfo[8])
#                connection.commit()
#                #print ("Selected", player.name)
#                #cur.execute("""UPDATE playerbase SET "TotalGames"=%s WHERE "Name"=%s""", (total_games,playerName,))
#                #print("EXIST -> ", total_games)
#            except:
#                player=Player.Player("new",playerName,"1","0/0","0/0","0/0","0/0","0/0","0")
#                cur.execute("""INSERT INTO one_player ("name","GUID","total_games", "win_rate", "svoi_podachi", "chuz_podachi", "set_rate", "game_rate", "break_point") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(player.name,player.GUID,player.total_games,player.win_rate,player.svoi_podachi,player.chuz_podachi, player.set_rate,player.game_rate,player.break_point))
#                #print("CREATE -> ", player.name)
#                connection.commit()
#                #print ("Created", player.name)
#            finally:
#                connection.commit()
#                playerList.append(player)
#                #print (player)
#        #Обновление геймов
#        P1Sv=str(int(playerList[0].svoi_podachi.split("/")[0])+gameStat[2][0])+"/"+str(int(playerList[0].svoi_podachi.split("/")[1])+gameStat[3][1])
#        P1Ch=str(int(playerList[0].chuz_podachi.split("/")[0])+gameStat[3][0])+"/"+str(int(playerList[0].chuz_podachi.split("/")[1])+gameStat[2][1])
#        P2Sv=str(int(playerList[1].svoi_podachi.split("/")[0])+gameStat[2][1])+"/"+str(int(playerList[1].svoi_podachi.split("/")[1])+gameStat[3][0])
#        P2Ch=str(int(playerList[1].chuz_podachi.split("/")[0])+gameStat[3][1])+"/"+str(int(playerList[1].chuz_podachi.split("/")[1])+gameStat[2][0])
#        #Обновление винрейта
#        if (gameStat[0]==1):
#            P1WR=str(int(playerList[0].win_rate.split("/")[0])+1)+"/"+str(int(playerList[0].win_rate.split("/")[1]))
#            P2WR=str(int(playerList[1].win_rate.split("/")[0]))+"/"+str(int(playerList[1].win_rate.split("/")[1])+1)
#        elif (gameStat[0]==2):
#            P1WR=str(int(playerList[0].win_rate.split("/")[0]))+"/"+str(int(playerList[0].win_rate.split("/")[1])+1)
#            P2WR=str(int(playerList[1].win_rate.split("/")[0])+1)+"/"+str(int(playerList[1].win_rate.split("/")[1]))
#        #Обновление сетрейта
#        P1Se=str(int(playerList[0].set_rate.split("/")[0])+gameStat[1][0])+"/"+str(int(playerList[0].set_rate.split("/")[1])+gameStat[1][1])
#        P2Se=str(int(playerList[1].set_rate.split("/")[0])+gameStat[1][1])+"/"+str(int(playerList[1].set_rate.split("/")[1])+gameStat[1][0])
#        #Обновление Брейк Поинтов
#        P1BP=str(int(playerList[0].break_point)+gameStat[4][0])
#        P2BP=str(int(playerList[1].break_point)+gameStat[4][1])
#        #elif (gameStat[10]==0): удалено так как StatPlayer теперь возвращает ошибку, если матч не окончен. (возможно, не работает при игре 2/2)
#        #    P1WR=playerList[0].win_rate
#        #    P2WR=playerList[1].win_rate
#
#        P1=Player.Player(playerList[0].GUID, playerList[0].name,playerList[0].total_games,P1WR,P1Sv, P1Ch,P1Se,"0/0",P1BP)
#        P2=Player.Player(playerList[1].GUID, playerList[1].name,playerList[1].total_games,P2WR,P2Sv, P2Ch,P2Se,"0/0",P2BP)
#        cur.execute("""UPDATE one_player SET "total_games"=%s, "win_rate"=%s, "svoi_podachi"=%s, "chuz_podachi"=%s, "set_rate"=%s, "game_rate"=%s, "break_point"=%s WHERE "name"=%s""", (P1.total_games,P1WR,P1.svoi_podachi, P1.chuz_podachi,P1.set_rate,P1.game_rate,P1.break_point,P1.name,))
#        connection.commit()
#        #print("Update 1")
#        cur.execute("""UPDATE one_player SET "total_games"=%s, "win_rate"=%s, "svoi_podachi"=%s, "chuz_podachi"=%s, "set_rate"=%s, "game_rate"=%s, "break_point"=%s WHERE "name"=%s""", (P2.total_games,P2WR,P2.svoi_podachi, P2.chuz_podachi,P2.set_rate,P2.game_rate,P2.break_point,P2.name,))
#        connection.commit()
#        #print("Update 2")
#        #cur.execute("""SELECT """"")
#        f.close()
#    else:
#        print ("Game stat is not valid, game is not over may be\n", f.name)
#        f.close()
#    #shutil.move("path/to/current/"+f.name, "path/to/new/destination/for/"+f.name)


def TestMakeGameFile():
    i = 1
    numberOfGames = 30
    games = []
    while i < numberOfGames:
        GUID = 'new'
        tournament = 'test'
        time = str(datetime.now().date())
        players = 'player 1, player 2'
        coeff = [round(random.uniform(1, 3), 3), round(random.uniform(1, 3), 3)]
        if coeff[0] > coeff[1]:
            result = 1
        else:
            result = 2
        try:
            game = Game.Game(GUID, tournament, time, players, str(coeff), result)
            games.append(game)
        except:
            print("game error")
        print(coeff)
        i += 1
        connection.commit()
    for game in games:
        print(game)
        cur.execute(
            """INSERT INTO one_game ("GUID","tournament", "time", "players", "coeff", "result") VALUES (%s,%s,%s,%s,%s,%s)""",
            (game.GUID, game.tournament, game.time, game.players, game.coeff[1:-1], game.result))
        connection.commit()


#Извлечение нужных файлов с играми, их открытие на чтение, считывание имен игроков(первой строки файла) и передача на детальный анализ игры в MakePersonalFile
#def MakeScoreFile (DirList):
#    for Dir in DirList:
#        for top, dir, files in os.walk(Dir):
#            print (files)
#            for file in files:
#                #f=open(Dir+"\\"+file, 'r', encoding="utf-8")
#                try:
#                    f=open(Dir+"/"+file, 'r', encoding="utf-8")
#                    playersLine=f.readline()
#                except UnicodeDecodeError:
#                    f.close()
#                    f=open(Dir+"/"+file, 'r', encoding="cp1251")
#                    playersLine=f.readline()
#                print (f.name,str(playersLine))
#                playerList=MakePersonalFile(playersLine,f)
#        print("________________________________________________________________________________________")



#Соединение с БД
try:
    connection = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='123'  port='5432'")
    print("\nShow me the database:\n")
    connection.commit()
    cur = connection.cursor()
except:
    print("database access denied")
i = 1
TestMakeGameFile()
#while 1>0:
#if ((datetime.now().hour==22) & (datetime.now().minute==00) & (datetime.now().second==00)) | (i==1):
dirList = []
#print ("0")
#Поиск папок с играми и передача на обработку в MakeScoreFile
#print ("/home/name1/tennis\ analitics")
#for top, dirs, files in os.walk("/home/name1/tennis analitics"):
##for top, dirs, files in os.walk("/home/programm"):
#	namecheck=re.compile(r".+MSK_2015")
#    if (namecheck.match(top)!=None):
#        #print(top)
#		dirList.append(top)
#MakeScoreFile(dirList)
#destion="/home/name1/tennis analitics/archive"
##destion="/home/programm/archive"
#for dir in dirList:
#    print (dir)
#    shutil.move(dir,destion)
#i=1

