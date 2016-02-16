import Game

__author__ = 'например Андрей'
# coding: utf8
import psycopg2
import os
import re
import Player
import StatPlayer
from datetime import datetime, date, time
import random
import shutil
# Обработка информации из файла, обновление статистики по игрокам в БД


def player_name_improvement(raw_player):
    '''
    Обработка имени игрока.
    '''
    mid_player = ""
    for letter in raw_player:
        if (letter != ","):
            if (letter == "-" or letter == "/" or letter == " " or letter == "." or letter == "," or letter == "'"):
                mid_player = mid_player + " "
            else:
                mid_player = mid_player + letter
    player_name = mid_player
    return player_name


def player_to_database(playersLine, f):
    '''
    Добавление/обноление игрока в БД

    Передает имена игроков на обработку в player_name_improvement;
    Передает запись игры на обработку игровой статистики в StatPlayer.renew_player_info(f);
    Добавляет нового или обновляет существующего игрока в БД.
    (Тест) Передает имена игроков и результат игры в  GameMaker.----
    '''
    players = playersLine[0:-2].split(" ")
    player_list = []
    game_stat = StatPlayer.renew_player_info(f)
    if game_stat != 0:
        for raw_player in players:
            player_name = player_name_improvement(raw_player)   #Изменяет имя игрока на более читаемое.
            try:
                cur.execute(
                    """SELECT "name","GUID","total_games", "win_rate", "svoi_podachi", "chuz_podachi", "set_rate", "game_rate", "break_point" FROM one_player WHERE "name"=%s""",
                    (player_name,))
                #print (cur.fetchone())#total_games=str(int(cur.fetchone()[0])+1)
                p_info = cur.fetchone()
                player = Player.Player(p_info[1], p_info[0], str(int(p_info[2]) + 1), p_info[3], p_info[4], p_info[5], p_info[6], p_info[7], p_info[8])
                connection.commit()
                #print ("Selected", player.name)
                #cur.execute("""UPDATE playerbase SET "TotalGames"=%s WHERE "Name"=%s""", (total_games,player_name,))
                #print("EXIST -> ", total_games)
            except:
                connection.commit()
                player = Player.Player("new", player_name, "1", "0/0", "0/0", "0/0", "0/0", "0/0", "0")
                guid = player.guid()
                #print (guid)
                cur.execute(
                    """INSERT INTO one_player ("name","GUID","total_games", "win_rate", "svoi_podachi", "chuz_podachi", "set_rate", "game_rate", "break_point") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (player.name, guid, player.total_games, player.win_rate, player.svoi_podachi,
                     player.chuz_podachi, player.set_rate, player.game_rate, player.break_point))
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


        p1 = Player.Player(player_list[0]._GUID, player_list[0].name, player_list[0].total_games, p1_wr, p1_sv, p1_ch, p1_sr,
                           "0/0", p1_bp)
        p2 = Player.Player(player_list[1]._GUID, player_list[1].name, player_list[1].total_games, p2_wr, p2_sv, p2_ch, p2_sr,
                           "0/0", p2_bp)
        cur.execute(
            """UPDATE one_player SET "total_games"=%s, "win_rate"=%s, "svoi_podachi"=%s, "chuz_podachi"=%s, "set_rate"=%s, "game_rate"=%s, "break_point"=%s WHERE "name"=%s""",
            (p1.total_games, p1_wr, p1.svoi_podachi, p1.chuz_podachi, p1.set_rate, p1.game_rate, p1.break_point, p1.name,))
        connection.commit()
        #print("Update 1")
        cur.execute(
            """UPDATE one_player SET "total_games"=%s, "win_rate"=%s, "svoi_podachi"=%s, "chuz_podachi"=%s, "set_rate"=%s, "game_rate"=%s, "break_point"=%s WHERE "name"=%s""",
            (p2.total_games, p2_wr, p2.svoi_podachi, p2.chuz_podachi, p2.set_rate, p2.game_rate, p2.break_point, p2.name,))
        connection.commit()
    else:
        print("Game stat is not valid, game is not over may be\n", f.name)
    f.close()
        #shutil.move("path/to/current/"+f.name, "path/to/new/destination/for/"+f.name)


def make_test_games():
    '''Создает тестовые записи в БД для работы сайта.'''
    i = 1
    number_of_games = 30
    games = []
    while i < number_of_games:
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
            (game._GUID, game.tournament, game.time, game.players, game.coeff[1:-1], game.result))
        connection.commit()

# Извлечение нужных файлов с играми, их открытие на чтение, считывание имен игроков(первой строки файла) и передача на детальный анализ игры в player_to_database
def make_score_file(DirList):
    '''
    Чтение файлов с играми. Передача данных в player_to_database.
    '''
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
                player_to_database(players_line, f)     #Функция добавления/обновления игрока
        print("________________________________________________________________________________________")


#Соединение с БД
try:
    connection = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='123'  port='5432'")
    print("\nShow me the database:\n")
    connection.commit()
    cur = connection.cursor()
except:
    print("database access denied")
i = 1
while i > 0:
    if ((datetime.now().hour == 22) & (datetime.now().minute == 00) & (datetime.now().second == 00)) | (i == 1):
        dirList = []
        print("0")
        #Поиск папок с играми и передача на обработку в make_score_file
        #print("/home/name1/tennis\ analitics")
        #for top, dirs, files in os.walk("/home/name1/tennis analitics"):
        #for top, dirs, files in os.walk("/home/programm"):
        for top, dirs, files in os.walk("E:\\tennis analitics"):
            name_check = re.compile(r".+MSK_2015")
            if (name_check.match(top) is not None):
                #print(top)
                dirList.append(top)
        make_score_file(dirList)
        make_test_games()
        destion = "E:\\tennis analitics\\archive"
        #destion = "/home/name1/tennis analitics/archive"
        #destion="/home/programm/archive"
        for dir in dirList:
            print(dir)
            shutil.move(dir, destion)
        i = 0