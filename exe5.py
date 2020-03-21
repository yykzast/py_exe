
# find XO in the field and returns their index
def find_XO(f,xo):
    f_index = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    p = []
    k = 0
    for a in f:
        i = 0
        for b in a:
            if b == xo:
                p.append(f_index[k][i])
            i = i + 1
        k = k + 1
    return p

# decide whether draw or not
def DRAW(f):
    i = 0
    for a in f:
        for b in a:
            if b in ['[X]','[O]']:
                i = i + 1
    if i == 9: return True
    else: return False

x = '[X]'
o = '[O]'
WIN = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
PACE = {0:(0,0),1:(0,1),2:(0,2),3:(1,0),4:(1,1),5:(1,2),6:(2,0),7:(2,1),8:(2,2)}
field_numbers = [['[0]','[1]','[2]'],['[3]','[4]','[5]'],['[6]','[7]','[8]']]
for i in field_numbers: print(''.join(i))

field = [['[ ]','[ ]','[ ]'],['[ ]','[ ]','[ ]'],['[ ]','[ ]','[ ]']]
IF_WIN = False

while True:

    playerX = None
    while playerX not in range(9) or field[PACE[playerX][0]][PACE[playerX][1]] in [x,o]:
        try: playerX = int(input("(X): "))
        except: print("Введите числовое значение!")
    field[PACE[playerX][0]][PACE[playerX][1]] = x
    for i in field: print(''.join(i))
    for item in WIN:
        if all(e in find_XO(field,x) for e in item):
            IF_WIN = True
            print("(X) выиграл!")
            break
    if IF_WIN == True: break
    elif DRAW(field):
        print("Ничья!")
        break

    playerO = None
    while playerO not in range(9) or field[PACE[playerO][0]][PACE[playerO][1]] in [x,o]:
        try: playerO = int(input("(O): "))
        except: print("Введите числовое значение!")
    field[PACE[playerO][0]][PACE[playerO][1]] = o
    for i in field: print(''.join(i))
    for item in WIN:
        if all(e in find_XO(field,o) for e in item):
            IF_WIN = True
            print("(O) выиграл!")
            break
    if IF_WIN == True: break
    elif DRAW(field):
        print("Ничья!")
        break