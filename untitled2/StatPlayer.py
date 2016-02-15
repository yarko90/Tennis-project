__author__ = 'например Андрей'
import re


def GameScore(line):
    if re.search(r"A", line):
        line = re.sub(r"A", "41", line)
    if re.search(r"\(\d+\:\d+\)", line):
        game_score = re.search(r"\(\d+\:\d+\)", line).group(0)[1:-1].split(":")
        # if re.search(r"A",line):
        #    game_score[0]=re.sub(r"A","41",game_score[0])
        #    game_score[1]=re.sub(r"A","41",game_score[1])
        #    print (line)
        if line.split(" ")[-3] == "<-":
            game_score.append("1")
        elif line.split(" ")[-3] == "->":
            game_score.append("2")
        else:
            game_score = "fail"
    else:
        game_score = "fail"
    return game_score


def RenewPlayerInfo(f):
    # print (f.name)
    i = 0
    P1MemScore = []
    P1MemScore.append("0:0")
    P2MemScore = []
    P2MemScore.append("0:0")
    svoiWin = [0, 0]
    chuzWin = [0, 0]
    gameScore = 0
    winPoint = 0
    setWin = [0, 0]
    gameWin = [0, 0]
    P1GameCoef = 0
    P2GameCoef = 0
    breakPointCount = [0, 0]
    Lines = f.readlines()
    FileLen = len(Lines)  # Это нужно для правильной работы. Повторный вызов len() выводит результат = 0.
    if FileLen > 0:
        EndLine = Lines[-1]
        #определение победителя winPoint
        if (EndLine[-2] == "-") & (EndLine[0] != "0:0"):
            if (int(EndLine[0:3].split(":")[0]) == int(EndLine[0:3].split(":")[1])) | (
                        (int(EndLine[0:3].split(":")[0]) + int(EndLine[0:3].split(":")[1])) < 2):
                winPoint = 0  # в случае неоконченного матча
            elif (int(EndLine[0:3].split(":")[0]) > int(EndLine[0:3].split(":")[1])):
                winPoint = 1
            elif (int(EndLine[0:3].split(":")[0]) < int(EndLine[0:3].split(":")[1])):
                winPoint = 2
                #print(EndLine," ", winPoint)
            #определение счета по сетам P1setWin, P2setWin и по геймам P1GameWin P2GameWin
        if winPoint != 0:
            sets = EndLine[5:-6].split(", ")
            if len(sets) > 1:
                for set in sets:
                    if (int(set.split(":")[0]) > int(set.split(":")[1])):
                        setWin[0] = setWin[0] + 1
                    if (int(set.split(":")[0]) < int(set.split(":")[1])):
                        setWin[1] = setWin[0] + 1
                    gameWin[0] = gameWin[0] + int(set.split(":")[0])
                    gameWin[1] = gameWin[1] + int(set.split(":")[1])
                    #print(EndLine," ", winPoint, " ",setWin[0],"/",setWin[1]," ",gameWin[0],"/",gameWin[1])
                #Процент побед в геймах на своей подаче, на чужой подаче (Брейк) и Брейк-поинтов.
            for Line in Lines:
                if i > 1:
                    #print("i=",i," Line: ",Lines[i-1])
                    gameScore = GameScore(Line)
                    past_gameScore = GameScore(Lines[i - 1])
                    if (gameScore != "fail") & (past_gameScore != "fail") & (past_gameScore != gameScore):
                        #print (past_gameScore)
                        #print(gameScore," ",past_gameScore)
                        if (int(past_gameScore[0]) > int(past_gameScore[1])) & (
                                    int(gameScore[2]) > int(past_gameScore[2])):
                            svoiWin[0] = svoiWin[0] + 1
                        elif (int(past_gameScore[0]) > int(past_gameScore[1])) & (
                                    int(gameScore[2]) < int(past_gameScore[2])):
                            chuzWin[0] = chuzWin[0] + 1
                        elif (int(past_gameScore[0]) < int(past_gameScore[1])) & (
                                    int(gameScore[2]) < int(past_gameScore[2])):
                            svoiWin[1] = svoiWin[1] + 1
                        elif (int(past_gameScore[0]) < int(past_gameScore[1])) & (
                                    int(gameScore[2]) > int(past_gameScore[2])):
                            chuzWin[1] = chuzWin[1] + 1
                        #if  (int(past_gameScore[0])!=int(gameScore[0])) & (int(past_gameScore[1])!=int(gameScore[1])) & ((past_gameScore[2]!=gameScore[2])):
                        if (int(past_gameScore[2]) == 1) & (
                                        ((int(past_gameScore[1]) == 40) & (int(past_gameScore[0]) < 40)) | int(
                                            past_gameScore[1]) == 41):
                            breakPointCount[1] = breakPointCount[1] + 1
                            print(past_gameScore, "\n", gameScore, "\n")
                        if (int(past_gameScore[2]) == 2) & (
                                        ((int(past_gameScore[0]) == 40) & (int(past_gameScore[1]) < 40)) | int(
                                            past_gameScore[0]) == 41):
                            breakPointCount[0] = breakPointCount[0] + 1
                            print(past_gameScore, "\n", gameScore, "\n")
                i = i + 1
            #print ("Player 1: ",gameWin[0]," (",svoiWin[0],"+",chuzWin[0],")\n", "Player 2: ",gameWin[1]," (",svoiWin[1],"+",chuzWin[1],")\n")
            print("Player 1: ", breakPointCount[0], " Player 2: ", breakPointCount[1])
            return [winPoint, setWin, svoiWin, chuzWin, breakPointCount]
        else:
            print("Can't read last line")
            return 0
    else:
        return 0
