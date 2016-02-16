__author__ = 'например Андрей'
# coding: utf8
import psycopg2
import os
import re
import Player
import StatPlayer
from datetime import datetime, date, time
import shutil
# Обработка информации из файла, обновление статистики по игрокам в БД


def make_personal_file(playersLine, f):
    players = playersLine[0:-2].split(" ")
    player_list = []
    # game_stat=renew_player_info.renew_player_info(f)
    game_stat = StatPlayer.renew_player_info(f)
    if game_stat != 0:
        for pre_player in players:
            mid_player = ""
            for letter in pre_player:
                if (letter != ","):
                    if (letter == "-" or letter == "/" or letter == " " or letter == "." or letter == "," or letter == "'"):
                        mid_player = mid_player + " "
                    else:
                        mid_player = mid_player + letter
            player_name = mid_player
            mid_player = ""
            try:
                cur.execute(
                    """SELECT "name","GUID","total_games", "win_rate", "svoi_podachi", "chuz_podachi", "set_rate", "game_rate", "break_point" FROM one_player WHERE "name"=%s""",
                    (player_name,))
                #print (cur.fetchone())#total_games=str(int(cur.fetchone()[0])+1)
                PInfo = cur.fetchone()
                player = Player.Player(PInfo[1], PInfo[0], str(int(PInfo[2]) + 1), PInfo[3], PInfo[4], PInfo[5],
                                       PInfo[6], PInfo[7], PInfo[8])
                connection.commit()
                #print ("Selected", player.name)
                #cur.execute("""UPDATE playerbase SET "TotalGames"=%s WHERE "Name"=%s""", (total_games,player_name,))
                #print("EXIST -> ", total_games)
            except:
                player = Player.Player("new", player_name, "1", "0/0", "0/0", "0/0", "0/0", "0/0", "0")
                cur.execute(
                    """INSERT INTO one_player ("name","GUID","total_games", "win_rate", "svoi_podachi", "chuz_podachi", "set_rate", "game_rate", "break_point") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (player.name, player.GUID, player.total_games, player.win_rate, player.svoi_podachi,
                     player.chuz_podachi, player.set_rate, player.game_rate, player.break_point))
                #print("CREATE -> ", player.name)
                connection.commit()
                #print ("Created", player.name)
            finally:
                connection.commit()
                player_list.append(player)
                #print (player)
        #Обновление геймов
        p1_sv = str(int(player_list[0].svoi_podachi.split("/")[0]) + game_stat[2][0]) + "/" + str(
            int(player_list[0].svoi_podachi.split("/")[1]) + game_stat[3][1])
        p1_ch = str(int(player_list[0].chuz_podachi.split("/")[0]) + game_stat[3][0]) + "/" + str(
            int(player_list[0].chuz_podachi.split("/")[1]) + game_stat[2][1])
        p2_sv = str(int(player_list[1].svoi_podachi.split("/")[0]) + game_stat[2][1]) + "/" + str(
            int(player_list[1].svoi_podachi.split("/")[1]) + game_stat[3][0])
        p2_ch = str(int(player_list[1].chuz_podachi.split("/")[0]) + game_stat[3][1]) + "/" + str(
            int(player_list[1].chuz_podachi.split("/")[1]) + game_stat[2][0])
        #Обновление винрейта
        if (game_stat[0] == 1):
            p1_wr = str(int(player_list[0].win_rate.split("/")[0]) + 1) + "/" + str(
                int(player_list[0].win_rate.split("/")[1]))
            p2_wr = str(int(player_list[1].win_rate.split("/")[0])) + "/" + str(
                int(player_list[1].win_rate.split("/")[1]) + 1)
        elif (game_stat[0] == 2):
            p1_wr = str(int(player_list[0].win_rate.split("/")[0])) + "/" + str(
                int(player_list[0].win_rate.split("/")[1]) + 1)
            p2_wr = str(int(player_list[1].win_rate.split("/")[0]) + 1) + "/" + str(
                int(player_list[1].win_rate.split("/")[1]))
        #Обновление сетрейта
        p1_sr = str(int(player_list[0].set_rate.split("/")[0]) + game_stat[1][0]) + "/" + str(
            int(player_list[0].set_rate.split("/")[1]) + game_stat[1][1])
        p2_sr = str(int(player_list[1].set_rate.split("/")[0]) + game_stat[1][1]) + "/" + str(
            int(player_list[1].set_rate.split("/")[1]) + game_stat[1][0])
        #Обновление Брейк Поинтов
        p1_bp = str(int(player_list[0].break_point) + game_stat[4][0])
        p2_bp = str(int(player_list[1].break_point) + game_stat[4][1])
        #elif (game_stat[10]==0): удалено так как StatPlayer теперь возвращает ошибку, если матч не окончен. (возможно, не работает при игре 2/2)
        #    p1_wr=player_list[0].win_rate
        #    p2_wr=player_list[1].win_rate

        p1 = Player.Player(player_list[0].GUID, player_list[0].name, player_list[0].total_games, p1_wr, p1_sv, p1_ch, p1_sr,
                           "0/0", p1_bp)
        p2 = Player.Player(player_list[1].GUID, player_list[1].name, player_list[1].total_games, p2_wr, p2_sv, p2_ch, p2_sr,
                           "0/0", p2_bp)
        cur.execute(
            """UPDATE one_player SET "total_games"=%s, "win_rate"=%s, "svoi_podachi"=%s, "chuz_podachi"=%s, "set_rate"=%s, "game_rate"=%s, "break_point"=%s WHERE "name"=%s""",
            (p1.total_games, p1_wr, p1.svoi_podachi, p1.chuz_podachi, p1.set_rate, p1.game_rate, p1.break_point,
             p1.name,))
        connection.commit()
        #print("Update 1")
        cur.execute(
            """UPDATE one_player SET "total_games"=%s, "win_rate"=%s, "svoi_podachi"=%s, "chuz_podachi"=%s, "set_rate"=%s, "game_rate"=%s, "break_point"=%s WHERE "name"=%s""",
            (p2.total_games, p2_wr, p2.svoi_podachi, p2.chuz_podachi, p2.set_rate, p2.game_rate, p2.break_point,
             p2.name,))
        connection.commit()
        #print("Update 2")
        #cur.execute("""SELECT """"")
    else:
        print("Game stat is not valid, game is not over may be\n", f.name)
    f.close()
        #shutil.move("path/to/current/"+f.name, "path/to/new/destination/for/"+f.name)


# Извлечение нужных файлов с играми, их открытие на чтение, считывание имен игроков(первой строки файла) и передача на детальный анализ игры в make_personal_file
def make_score_file(DirList):
    for Dir in DirList:
        for top, dir, files in os.walk(Dir):
            print(files)
            for file in files:
                #f=open(Dir+"\\"+file, 'r', encoding="utf-8")
                try:
                    f = open(Dir + "/" + file, 'r', encoding="utf-8")
                    players_line = f.readline()
                except UnicodeDecodeError:
                    f.close()
                    f = open(Dir + "/" + file, 'r', encoding="cp1251")
                    players_line = f.readline()
                print(f.name, str(players_line))
                playerList = make_personal_file(players_line, f)
        print("________________________________________________________________________________________")


#Соединение с БД
try:
    connection = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='123'  port='5432'")
    print("\nShow me the database:\n")
    connection.commit()
    cur = connection.cursor()
except:
    print("database access denied")
i = 1
while 1 > 0:
    if ((datetime.now().hour == 22) & (datetime.now().minute == 00) & (datetime.now().second == 00)) | (i == 1):
        dirList = []
        print("0")
        #Поиск папок с играми и передача на обработку в make_score_file
        print("/home/name1/tennis\ analitics")
        #for top, dirs, files in os.walk("/home/name1/tennis analitics"):
        #for top, dirs, files in os.walk("/home/programm"):
        for top, dirs, files in os.walk("E:\\tennis analitics"):
            namecheck = re.compile(r".+MSK_2015")
            if (namecheck.match(top) != None):
                #print(top)
                dirList.append(top)
        make_score_file(dirList)
        destion = "E:\\tennis analitics\\archive"
        #destion = "/home/name1/tennis analitics/archive"
        #destion="/home/programm/archive"
        for dir in dirList:
            print(dir)
            shutil.move(dir, destion)
        i = 1