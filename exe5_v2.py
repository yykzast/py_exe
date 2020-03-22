
# this function make a move in the field according to [X] or [O]. returns new field and result of WIN, DRAW
def MOVE(p,f):
    move = None
    f_index = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    xy = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (1, 0), 4: (1, 1), 5: (1, 2), 6: (2, 0), 7: (2, 1), 8: (2, 2)}
    if_win = False
    if_draw = False

    while move not in range(9) or f[xy[move][0]][xy[move][1]] in ['[X]','[O]']:
        try: move = int(input(p + "вставьте: "))
        except: print("Введите числовое значение!")
    f[xy[move][0]][xy[move][1]] = p
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
    if k == 9:
        if_draw = True
        print("Ничья!")

    return f, if_win, if_draw

x = '[X]'
o = '[O]'
field_numbers = [['[0]','[1]','[2]'],['[3]','[4]','[5]'],['[6]','[7]','[8]']]
for i in field_numbers: print(''.join(i))

field = [['[ ]','[ ]','[ ]'],['[ ]','[ ]','[ ]'],['[ ]','[ ]','[ ]']]

while True:

    field = MOVE(x,field)[0]
    if MOVE(x,field)[1] or MOVE(x,field)[2]:
        break

    field = MOVE(o,field)[0]
    if MOVE(o,field)[1] or MOVE(o,field)[2]:
        break