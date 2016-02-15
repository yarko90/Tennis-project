__author__ = 'например Андрей'
import psycopg2
import re
import Player


def MakePersonalFile(tableName):
    processline = "SELECT player1,player2 FROM " + tableName
    print("pl check", processline)
    try:
        cur.execute(processline)
        print("ex check")
    except psycopg2.Error as error:
        print(error.pgerror)
    players = cur.fetchone()
    print("fetch check")
    for player in players:
        print(player)
        try:
            rown = "SELECT score FROM " + player.lower()
            print(rown)
            cur.execute(rown)
            NumberOfGames = cur.fetchone()[0]
            NewNumberOfGames = int(NumberOfGames) + 1
            rown = "UPDATE " + player.lower() + " SET score='" + str(NewNumberOfGames) + "' WHERE score ='" + str(
                NumberOfGames) + "'"
            cur.execute(rown)
            print("   ", rown)
        except psycopg2.Error as error:
            connection.commit()
            print("fail: ", error)
            rown = "CREATE TABLE " + player.lower() + " (score character varying(10));"
            print(rown)
            cur.execute(rown)
            connection.commit()
            rown = "INSERT INTO " + player.lower() + " (score) VALUES (1);"
            cur.execute(rown)
            print("   ", rown)
            connection.commit()
        finally:
            connection.commit()


try:
    connection = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='123'  port='5432'")
    print("\nShow me the database:\n")
except:
    print("Fuckeduppa")
connection.commit()
cur = connection.cursor()
try:
    cur.execute("SELECT * FROM information_schema.tables WHERE table_schema = 'public'")
    tables = cur.fetchall()
    for table in tables:
        tablename = table[2]
        namecheck = re.compile(r"score\d+")
        if (namecheck.match(tablename) != None):
            print("gomakefile for ", tablename)
            MakePersonalFile(tablename)
        else:
            print(namecheck.match(tablename))
except psycopg2.Error as error:
    print("execute table fail", error)
connection.close()