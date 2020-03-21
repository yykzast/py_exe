WAYS_WIN = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

# Две глобальные переменны X и O

x = 'X'
o = 'O'
empty = '_'
error_ = "\nНеверный ход. Ход передается следующему игроку."

# Создать поле

def create_f():
    field = []
    for i in range(1,10):
        field.append(empty)
    return field

# Выводить поле

def release_field(field):
    print("_ _ _")
    for x in range(0, len(field), 3):
        print(*field[x:x+3], sep = '|')
    

# Определить игроков 

def players():
    player1 = input('Вы первый игрок. Введите ваше имя: ')
    player2 = input('Вы второй игрок. Введите ваше имя: ')
    print('Первый игрок - {}. Второй игрок - {}. Начинает {} с {}.'.format(player1,player2, player1, x))
    key = {player1:x, player2:o}
    return player1, player2, key

# Закончена ли игра
def is_finished(field, player1, player2):
    for lists in WAYS_WIN:
        check_list_x = []
        check_list_o = []
        for indexes in lists:
            if field[indexes] == x:
                check_list_x.append(indexes)
                if len(check_list_x) == 3:
                    print('Выиграл {}.'.format(player1))
                    return True
            elif field[indexes] == o:
                check_list_o.append(indexes)
                if len(check_list_o) == 3:
                    print('Выиграл {}.'.format(player2))
                    return True


# Сделать шаг 
def move(field, player, key):
    a = int(input('{}. Прошу ввести номер поля, для ввода {}:'.format(player, key[player])))
    if field[a] == empty:
        field[a] = key[player]
    elif a == str:
        raise ValueError
    else:        
        raise IndexError()

def main():
    field = create_f()
    player1, player2, key = players()
    release_field(field)
    while True:
        try:
            move(field, player1, key)
            release_field(field)
            if is_finished(field, player1, player2) == True:
                break
            if empty not in field:
                print('Ничья!')
                break
        except:
            print(error_)
            release_field(field)
        try: 
            move(field, player2, key)
            release_field(field)
            if is_finished(field, player1, player2) == True:
                break
            if empty not in field:
                print('Ничья!')
                break
        except:
            print(error_)
            release_field(field)

if __name__ == '__main__':
    main()

