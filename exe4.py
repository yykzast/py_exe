import random

# function make 'n' dimension ordered square
def ordered_sq(n):
    sq = []
    i = 0
    for x in range(n):
        row = []
        for y in range(n):
            i = i + 1
            row.append(i)
        sq.append(row)
    sq[n-1][n-1] = 'x'
    return sq

# function make 'n' dimension unordered square
def unordered_sq(n):
    lst = []
    sq = []
    for i in range(n*n-1):
        lst.append(i+1)
    lst.append('x')
    for x in range(n):
        row = []
        for y in range(n):
            c = random.choice(lst)
            row.append(c)
            lst.remove(c)
        sq.append(row)
    return sq

# function to find position of 'x' in the square
def position(sq):
    i = 0
    for row in sq:
        if 'x' in row:
            x = i
            y = sq[x].index('x')
        i = i+1
    return x,y

# functions to move 'x' to up, down, right, left
def up(sq,p):
    sq[p[0]][p[1]] = sq[p[0]-1][p[1]]
    sq[p[0]-1][p[1]] = 'x'
    return sq

def down(sq,p):
    sq[p[0]][p[1]] = sq[p[0]+1][p[1]]
    sq[p[0]+1][p[1]] = 'x'
    return sq

def right(sq,p):
    sq[p[0]][p[1]] = sq[p[0]][p[1]+1]
    sq[p[0]][p[1]+1] = 'x'
    return sq

def left(sq,p):
    sq[p[0]][p[1]] = sq[p[0]][p[1]-1]
    sq[p[0]][p[1]-1] = 'x'
    return sq


# from here starts GAME main body

s = None
while s not in range(2,10):
    try:
        s = int(input("Введите размер 's' квадрата (10>s>1): "))
    except:
        print("Введите числовое значение!")
        continue

print("\nВаша задача двигать 'x' кнопками w,s,a,d и собрать квадрат как ниже:")
tsq = ordered_sq(s)
for i in range(s):
    print(tsq[i])

print("\nНачинаем игру:")
sq = unordered_sq(s)
p = position(sq)
# print initial square
for i in range(s):
    print(sq[i])

while True:
    # if sq equals to tsq then target achieved and stop the GAME
    if sq == tsq:
        print("Вы собрали квадрат!")
        break
    # ask player to move 'x' by buttons w,s,a,d
    move = input("Введите w,s,a,d: ")
    # when player input other buttons then ask again
    if move not in ['w','a','s','d']:
        continue
    # when player move 'x' out of range then ask again
    if (move == 'w' and p[0] == 0) or (move == 's' and p[0] == s-1) or (move == 'a' and p[1] == 0) or (move == 'd' and p[1] == s-1):
        print("Неверный ход!")
        continue
    # in other case move 'x' according to direction
    if move == 'w':
        sq = up(sq,p)
        p = position(sq)
    elif move == 's':
        sq = down(sq,p)
        p = position(sq)
    elif move == 'a':
        sq = left(sq,p)
        p = position(sq)
    elif move == 'd':
        sq = right(sq,p)
        p = position(sq)
    # print new square after player move 'x'
    for i in range(s):
        print(sq[i])
