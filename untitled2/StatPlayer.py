__author__ = 'например Андрей'
import re


def game_score(line):
    if re.search(r"A", line):
        line = re.sub(r"A", "41", line)
    if re.search(r"\(\d+\:\d+\)", line):
        score = re.search(r"\(\d+\:\d+\)", line).group(0)[1:-1].split(":")
        # if re.search(r"A",line):
        #    score[0]=re.sub(r"A","41",score[0])
        #    score[1]=re.sub(r"A","41",score[1])
        #    print (line)
        if line.split(" ")[-3] == "<-":
            score.append("1")
        elif line.split(" ")[-3] == "->":
            score.append("2")
        else:
            score = "fail"
    else:
        score = "fail"
    return score


def renew_player_info(f):
    # print (f.name)
    i = 0
    #p1_mem_score = ["0:0"]     #lkz расширеной статистики.
    #p2_mem_score = ["0:0"]
    #p1_game_coef = 0
    #p2_game_coef = 0
    svoi_win = [0, 0]
    chuz_win = [0, 0]
    score = 0
    win_point = 0
    set_win = [0, 0]
    game_win = [0, 0]
    break_point_count = [0, 0]
    lines = f.readlines()
    file_len = len(lines)  # Это нужно для правильной работы. Повторный вызов len() выводит результат = 0.
    if file_len > 0:
        end_line = lines[-1]
        #определение победителя win_point
        if (end_line[-2] == "-") & (end_line[0] != "0:0"):
            if (int(end_line[0:3].split(":")[0]) == int(end_line[0:3].split(":")[1])) | (
                        (int(end_line[0:3].split(":")[0]) + int(end_line[0:3].split(":")[1])) < 2):
                win_point = 0  # в случае неоконченного матча
            elif (int(end_line[0:3].split(":")[0]) > int(end_line[0:3].split(":")[1])):
                win_point = 1
            elif (int(end_line[0:3].split(":")[0]) < int(end_line[0:3].split(":")[1])):
                win_point = 2
                #print(end_line," ", win_point)
            #определение счета по сетам P1setWin, P2setWin и по геймам P1GameWin P2GameWin
        if win_point != 0:
            sets = end_line[5:-6].split(", ")
            if len(sets) > 1:
                for set in sets:
                    if (int(set.split(":")[0]) > int(set.split(":")[1])):
                        set_win[0] = set_win[0] + 1
                    if (int(set.split(":")[0]) < int(set.split(":")[1])):
                        set_win[1] = set_win[0] + 1
                    game_win[0] = game_win[0] + int(set.split(":")[0])
                    game_win[1] = game_win[1] + int(set.split(":")[1])
                    #print(end_line," ", win_point, " ",set_win[0],"/",set_win[1]," ",game_win[0],"/",game_win[1])
                #Процент побед в геймах на своей подаче, на чужой подаче (Брейк) и Брейк-поинтов.
            for line in lines:
                if i > 1:
                    #print("i=",i," line: ",lines[i-1])
                    score = game_score(line)
                    past_score = game_score(lines[i - 1])
                    if (score != "fail") & (past_score != "fail") & (past_score != score):
                        #print (past_score)
                        #print(score," ",past_score)
                        if (int(past_score[0]) > int(past_score[1])) & (int(score[2]) > int(past_score[2])):
                            svoi_win[0] = svoi_win[0] + 1
                        elif (int(past_score[0]) > int(past_score[1])) & (int(score[2]) < int(past_score[2])):
                            chuz_win[0] = chuz_win[0] + 1
                        elif (int(past_score[0]) < int(past_score[1])) & (int(score[2]) < int(past_score[2])):
                            svoi_win[1] = svoi_win[1] + 1
                        elif (int(past_score[0]) < int(past_score[1])) & (int(score[2]) > int(past_score[2])):
                            chuz_win[1] = chuz_win[1] + 1
                        #if  (int(past_score[0])!=int(score[0])) & (int(past_score[1])!=int(score[1])) & ((past_score[2]!=score[2])):
                        if (int(past_score[2]) == 1) & (((int(past_score[1]) == 40) & (int(past_score[0]) < 40)) | int(past_score[1]) == 41):
                            break_point_count[1] = break_point_count[1] + 1
                            print(past_score, "\n", score, "\n")
                        if (int(past_score[2]) == 2) & (((int(past_score[0]) == 40) & (int(past_score[1]) < 40)) | int(past_score[0]) == 41):
                            break_point_count[0] = break_point_count[0] + 1
                            print(past_score, "\n", score, "\n")
                i = i + 1
            #print ("Player 1: ",game_win[0]," (",svoi_win[0],"+",chuz_win[0],")\n", "Player 2: ",game_win[1]," (",svoi_win[1],"+",chuz_win[1],")\n")
            print("Player 1: ", break_point_count[0], " Player 2: ", break_point_count[1])
            return [win_point, set_win, svoi_win, chuz_win, break_point_count]
        else:
            print("Can't read last line")
            return 0
    else:
        print("Empty file")
        return 0
