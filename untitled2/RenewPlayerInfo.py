__author__ = 'например Андрей'


def RenewPlayerInfo(f):
    i = 0
    P1MemScore = []
    P1MemScore.append("0:0")
    P2MemScore = []
    P2MemScore.append("0:0")
    P1SvoiWin = 0
    P1SvoiLoo = 0
    P1ChuzWin = 0
    P1ChuzLoo = 0
    P2SvoiWin = 0
    P2SvoiLoo = 0
    P2ChuzWin = 0
    P2ChuzLoo = 0
    winPoint = 0
    P1set = 0
    P2set = 0
    for line in f.readlines():
        Line = line.split(" ")
        # Подготовка статистики по геймам.
        if (Line[-2] != "-"):
            if (Line[-3] == "<-"):
                P1MemScore.append(Line[-4][1:-1])
            if (Line[-3] == "->"):
                P2MemScore.append(Line[-4][1:-1])
            #Анализ последней строки на наличие итогов матча. Если есть, определение победителя, очки по сетам.
        if (Line[-2] == "-") & (Line[0] != "0:0"):
            if (int(Line[0].split(":")[0]) + int(Line[0].split(":")[1]) >= 2) & (
                        int(Line[0].split(":")[0]) != int(Line[0].split(":")[1])):
                #print (Line)
                if int(Line[0].split(":")[0]) > int(Line[0].split(":")[1]):
                    winPoint = 1
                else:
                    winPoint = 2
            else:
                winPoint = 0
            for setRes in Line[2].split(", "):
                if setRes.split(":")[0] > setRes.split(":")[1]:
                    P1set = P1set + 1
                else:
                    P2set = P2set + 1
                    #print ("Sets results: ", P1set,":", P2set, "Winner is: ",winPoint)
    # print (f.name)
    i = 1
    #print (P1MemScore)
    #Статистика по геймам
    if (len(P1MemScore) > 1) & (len(P2MemScore) > 1):
        for P in P1MemScore:
            if i < len(P1MemScore):
                if P1MemScore[i] != P1MemScore[i - 1]:
                    if P1MemScore[i].find("A") == -1 & P1MemScore[i - 1].find("A") == -1:
                        if (int(str(P1MemScore[i]).split(":")[0]) > int(str(P1MemScore[i - 1]).split(":")[0])):
                            #print (i, P1MemScore[i])
                            P1SvoiWin = P1SvoiWin + 1
                            P2ChuzLoo = P2ChuzLoo + 1
                        if (int(str(P1MemScore[i]).split(":")[1]) > int(str(P1MemScore[i - 1]).split(":")[1])):
                            P1SvoiLoo = P1SvoiLoo + 1
                            P2ChuzWin = P2ChuzWin + 1
                    else:
                        if (P1MemScore[i].split(":")[0] == "A") & (P1MemScore[i - 1].split(":")[0] != "A"):
                            P1SvoiWin = P1SvoiWin + 1
                            P2ChuzLoo = P2ChuzLoo + 1
                        if (P1MemScore[i].split(":")[1] == "A") & (P1MemScore[i - 1].split(":")[1] != "A"):
                            P1SvoiLoo = P1SvoiLoo + 1
                            P2ChuzWin = P2ChuzWin + 1

                        if (P1MemScore[i].split(":")[0] != 0) & (P1MemScore[i - 1].split(":")[0] == "A"):
                            P1SvoiLoo = P1SvoiLoo + 1
                            P2ChuzWin = P2ChuzWin + 1
                        if (P1MemScore[i].split(":")[1] != 0) & (P1MemScore[i - 1].split(":")[1] == "A"):
                            P1SvoiWin = P1SvoiWin + 1
                            P2ChuzLoo = P2ChuzLoo + 1

                        if (P1MemScore[i].split(":")[0] == 0) & (P1MemScore[i - 1].split(":")[0] == "A"):
                            P1SvoiWin = P1SvoiWin + 1
                            P2ChuzLoo = P2ChuzLoo + 1
                        if (P1MemScore[i].split(":")[1] == 0) & (P1MemScore[i - 1].split(":")[1] == "A"):
                            P1SvoiLoo = P1SvoiLoo + 1
                            P2ChuzWin = P2ChuzWin + 1
                i = i + 1
        i = 1
        #print (P2MemScore)
        for P in P2MemScore:
            if i < len(P2MemScore):
                if (P2MemScore[i] != P2MemScore[i - 1]):
                    if P2MemScore[i].find("A") == -1 & P2MemScore[i - 1].find("A") == -1:
                        if (int(str(P2MemScore[i]).split(":")[0]) > int(str(P2MemScore[i - 1]).split(":")[0])):
                            P2SvoiLoo = P2SvoiLoo + 1
                            P1ChuzWin = P1ChuzWin + 1
                        if (int(str(P2MemScore[i]).split(":")[1]) > int(str(P2MemScore[i - 1]).split(":")[1])):
                            P2SvoiWin = P2SvoiWin + 1
                            P1ChuzLoo = P1ChuzLoo + 1
                    else:
                        if (P2MemScore[i].split(":")[0] == "A") & (P2MemScore[i - 1].split(":")[0] != "A"):
                            P2SvoiWin = P2SvoiWin + 1
                            P1ChuzLoo = P1ChuzLoo + 1
                        if (P2MemScore[i].split(":")[1] == "A") & (P2MemScore[i - 1].split(":")[1] != "A"):
                            P2SvoiLoo = P2SvoiLoo + 1
                            P1ChuzWin = P1ChuzWin + 1

                        if (P2MemScore[i].split(":")[0] != 0) & (P2MemScore[i - 1].split(":")[0] == "A"):
                            P2SvoiLoo = P2SvoiLoo + 1
                            P1ChuzWin = P1ChuzWin + 1
                        if (P2MemScore[i].split(":")[1] != 0) & (P2MemScore[i - 1].split(":")[1] == "A"):
                            P2SvoiWin = P2SvoiWin + 1
                            P1ChuzLoo = P1ChuzLoo + 1

                        if (P2MemScore[i].split(":")[0] == 0) & (P2MemScore[i - 1].split(":")[0] == "A"):
                            P2SvoiWin = P2SvoiWin + 1
                            P1ChuzLoo = P1ChuzLoo + 1
                        if (P2MemScore[i].split(":")[1] == 0) & (P2MemScore[i - 1].split(":")[1] == "A"):
                            P2SvoiLoo = P2SvoiLoo + 1
                            P1ChuzWin = P1ChuzWin + 1
                i = i + 1
    #print ("Svoi Podachi P1W/L | P2W/L: ", P1SvoiWin,"/",P2SvoiLoo,"  |  ",P2SvoiWin,"/",P2SvoiLoo)
    #print ("Chuz Podachi P1W/L | P2W/L: ", P1ChuzWin,"/",P2ChuzLoo,"  |  ",P2ChuzWin,"/",P2ChuzLoo)
    #print ("P1 Svoi Win / P2 Chuz Loose", P1SvoiWin,"/",P2ChuzLoo)
    #print ("P1 Svoi Loose / P2 Chuz Win", P1SvoiLoo,"/",P2ChuzWin)
    #print ("P2 Svoi Win / P1 Chuz Loose", P2SvoiWin,"/",P1ChuzLoo)
    #print ("P2 Svoi Loose / P1 Chuz Win", P2SvoiLoo,"/",P1ChuzWin)
    return [P1SvoiWin, P1SvoiLoo, P1ChuzWin, P1ChuzLoo, P2SvoiWin, P2SvoiLoo, P2ChuzWin, P2ChuzLoo, P1set, P2set,
            winPoint]