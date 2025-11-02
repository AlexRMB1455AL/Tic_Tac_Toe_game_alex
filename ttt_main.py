#-------------------------------------------------------------------------------
"""
1. Нам нужно отобразить доску (игровое поле).
2. Получить ввод от игрока.
3. Поместить этот ввод на доске.
4. Проверить, получился ли в игре выигрыш, проигрыш, ничья, или игра продолжается.
5. Повторить шаги 3 и 4 до тех пор, пока не получим выигрыш или ничью.
6. Спросить, хотят ли игроки играть снова."""

#Нам нужно отобразить доску (игровое поле)
#-------------------------------------------------------------------------------
#map_go*************************************************************************
result = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'} #const
result_play = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '} #const
result_players = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '} #change_inplay
win_results = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
#map_end************************************************************************
#-------------------------------------------------------------------------------
#description_go*****************************************************
start_des = 'Описание ячеек ввода такое же как на клавиатуре справа'
play_des =  'Игровая площадка с номерами ячеек в диапазоне 1-9'
play_des1 = 'Игрок 1 использует "Х", а игрок 2 использует "0"'
play_des2 = 'Для установки элемента игры введите номер ячейки'
play_des3 = 'Вне области значений ячеек, повторите ввод'
play_des4 = 'Ячейка занята, выберите другую ячейку'
play_des5 = 'Выберите "Y" для старта или "E" для выхода:'
play_des6 = 'Выход из игры'
play_des7 = 'Ввод отменён, выход из игры'
play_des8 = 'Игрок 1'
play_des9 = 'Игрок 2'
play_des10 = 'Введите номер ячейки для'
play_des11 = 'Символ не верный, повторите ввод'
#indent
ind10 =' '*10
ind4 = ' '*4
ind0 = ''
#description_end******************************************************
#-------------------------------------------------------------------------------
#Function
#start_board_go*****************************************************************
def board_place(run, indent='',description1='', description2='',description3=''):
    A0=A6='-'*7
    A1='|'+run[7]+'|'+run[8]+ '|' +run[9]+ '|'+ indent + '* ' + description1
    A3='|'+run[4]+'|'+run[5]+ '|' +run[6]+ '|'+ indent + '* ' + description2
    A5='|'+run[1]+'|'+run[2]+ '|' +run[3]+ '|'+ indent + '* ' + description3
    A2=A4='|'+'-'*5 +'|'
    print(ind0)
    for place_num in [A0,A1,A2,A3,A4,A5,A6]:
        print(ind10,place_num)
#start_board_end****************************************************************
#-------------------------------------------------------------------------------
#clear_terminal_go**********************************
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#clear_terminal_end*********************************
#input_go***********************************************************
def check_input(marker):
    number_int = input(f'{ind10}{play_des8},{play_des10} {marker}:')
    return number_int
#input_end**********************************************************
#update_board_go*********************************************
def board_up(result_board):
    clear()
    board_place(result_board,ind4,play_des,play_des1,play_des2)
#update_board_end*********************************************
#Function_end
#-------------------------------------------------------------------------------
#start_play_go*************************
board_place(result,ind4,ind0,start_des)
board_place(result_play,ind4,ind0,play_des)
#start_play_end************************
#-------------------------------------------------------------------------------
#start_game_go***************************************************
flag = 1
while flag == 1:
    try:
        start_checkin = input(f'{ind10} {play_des5}')
        print(ind0)
        if start_checkin == 'Y' or start_checkin == 'y':
            board_up(result_play)
            flag = 0
        elif start_checkin == 'E' or start_checkin == 'e':
            print(ind10, play_des6)
            break
        else:
            print(ind10, play_des11)
    except KeyboardInterrupt:
        print(ind10, play_des7)
        break

#start_game_end*****************************************************
#-------------------------------------------------------------------------------
#players_move_go******************************************
def players_move_X_0(literal_tic_toc):
    flag = 0
    while flag == 0:

        try:
            play1 = check_input(literal_tic_toc)
        except KeyboardInterrupt:
            print(f"{ind10}{play_des6}")
            flag = 1
            break
        if play1 in result.values():
            play2 = int(play1)
            if  result_players[play2] == ' ':
                result_players[play2] = literal_tic_toc
                board_up(result_players)
                break
            else:
                print(ind10,play_des4)
        else:
            print(ind10,play_des3)
            continue

        for win_check in win_results():
            if (result_players[win_check[0]] == literal_tic_toc and
                result_players[win_check[1]] == literal_tic_toc and
                result_players[win_check[2]] == literal_tic_toc):
                print(f'{ind10} {literal_tic_toc} - Победил!')
                flag = 1
                break
            if flag == 1:
                break
            if ' ' not in result_players.values():
                print(f'{ind10} Ничья!')
                flag = 1
                break
#players_move_end*****************************************
while True:
    players_move_X_0('X')
    players_move_X_0('0')
