import random

# global variables
xy = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
f_index = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

# Menu for opponent selection
def MENU():
    print('''
Выберите с кем играть:
(1) - Второй игрок;
(2) - CPU1;
(3) - CPU2;''')
    select = None
    while not select in range(1,4):
        try:
            select = int(input("Ваш выбор: "))
        except:
            print("Введите числовое значение!")
    return select

# this function make the movement in the field and returns new field with results of WIN, DRAW
def PLAY(p,m,f):
    global f_index
    global win
    if_win = False
    if_draw = False

    f[m[0]][m[1]] = p
    for i in f: print(''.join(i))

    place = []
    i1 = 0
    for a1 in f:
        i2 = 0
        for b1 in a1:
            if b1 == p:
                place.append(f_index[i1][i2])
            i2 = i2 + 1
        i1 = i1 + 1

    for item in win:
        if all(e in place for e in item):
            if_win = True
            print(p + " выиграл!")
            break

    k = 0
    for a2 in f:
        for b2 in a2:
            if b2 in ['[X]','[O]']:
                k = k + 1
    if k == 9 and not if_win:
        if_draw = True
        print("Ничья!")

    return f, if_win, if_draw

# this function asks player to move and if valid movement then returns move result
def ASK_MOVE(f,p):
    global xy
    move = None
    while move not in range(1,10) or f[xy[move][0]][xy[move][1]] in ['[X]','[O]']:
        try:
            move = int(input("Ваш ход {}: ".format(p)))
        except:
            print("Введите числовое значение!")
    return xy[move][0],xy[move][1]

# this function make CPU Level_1 move then returns move result
def CPU1_MOVE(f):
    global xy
    available_moves = []
    for key in xy:
        if not f[xy[key][0]][xy[key][1]] in ['[X]','[O]']:
            available_moves.append(key)
    move = random.choice(available_moves)
    print("CPU1 ход:")
    return xy[move][0],xy[move][1]

def CPU2_MOVE(f):
    global xy
    global f_index
    global win

    available_moves = []
    for key in xy:
        if not f[xy[key][0]][xy[key][1]] in ['[X]','[O]']:
            available_moves.append(key)

    win_moves = []
    for i in available_moves:
        f[xy[i][0]][xy[i][1]] = '[O]'

        place = []
        i1 = 0
        for a1 in field:
            i2 = 0
            for b1 in a1:
                if b1 == '[O]':
                    place.append(f_index[i1][i2])
                i2 = i2 + 1
            i1 = i1 + 1
        f[xy[i][0]][xy[i][1]] = '[ ]'

        for item in win:
            if all(e in place for e in item):
                win_moves.append(i)

    save_moves = []
    for i in available_moves:
        f[xy[i][0]][xy[i][1]] = '[X]'

        place = []
        i1 = 0
        for a1 in field:
            i2 = 0
            for b1 in a1:
                if b1 == '[X]':
                    place.append(f_index[i1][i2])
                i2 = i2 + 1
            i1 = i1 + 1
        f[xy[i][0]][xy[i][1]] = '[ ]'

        for item in win:
            if all(e in place for e in item):
                save_moves.append(i)

    rec_moves = []
    for i in [1,3,7,9]:
        if i in available_moves:
            rec_moves.append(i)

    best_moves = []
    if len(win_moves) > 0:
        for i in win_moves:
            if i in available_moves:
                best_moves.append(i)
    elif len(save_moves) > 0:
        for i in save_moves:
            if i in available_moves:
                best_moves.append(i)
    elif len(rec_moves) > 0:
        best_moves = rec_moves
    else:
        best_moves = available_moves

    move = random.choice(best_moves)

    print("CPU2 ход:")
    return xy[move][0],xy[move][1]

# main body of the GAME starts from here
x = '[X]'
o = '[O]'
field = [['[ ]','[ ]','[ ]'],['[ ]','[ ]','[ ]'],['[ ]','[ ]','[ ]']]

select = MENU()

# instruction how to make movement
print("Инструкция:")
field_numbers = [['[1]','[2]','[3]'],['[4]','[5]','[6]'],['[7]','[8]','[9]']]
for i in field_numbers: print(''.join(i))

while True:

    player_move = ASK_MOVE(field,x)
    field, WIN, DRAW = PLAY(x,player_move,field)
    if WIN or DRAW:
        break

    if select == 1:
        player_move = ASK_MOVE(field,o)
    elif select == 2:
        player_move = CPU1_MOVE(field)
    elif select == 3:
        player_move = CPU2_MOVE(field)
    field, WIN, DRAW = PLAY(o,player_move,field)
    if WIN or DRAW:
        break