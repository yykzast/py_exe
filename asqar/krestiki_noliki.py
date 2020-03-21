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
    return player1, player2

# Зкончена ли игра
def is_finished(field, player1, player2):
    for lists in WAYS_WIN:
        check_list_x = []
        check_list_o = []
        for indexes in lists:
            if field[indexes] == x:
                check_list_x.append(indexes)
                if len(check_list_x) == 3:
                    print('Выиграл первый игрок - {}.'.format(player1))
                    return True
            elif field[indexes] == o:
                check_list_o.append(indexes)
                if len(check_list_o) == 3:
                    print('Выиграл втооой игрок - {}.'.format(player2))
                    return True


# Сделать шаг 
def move1(field):
    a = int(input('Игрок 1. Прошу ввести номер поля, для ввода X:'))
    if field[a] == empty:
        field[a] = x
    elif a == str:
        raise ValueError
    else:        
        raise IndexError()

    
def move2(field):
    a = int(input('Игрок 2. Прошу ввести номер поля, для ввода O:'))
    if field[a] == empty:
        field[a] = o
    elif a == str:
        raise ValueError
    else:        
        raise IndexError()

def main():
    field = create_f()
    release_field(field)
    player1, player2 = players()

    while True:
        try:
            move1(field)
            release_field(field)
            if is_finished(field, player1, player2) == True:
                break
            if empty not in field:
                print('Ничья!')
                break
        except IndexError:
            print("Неверный ход. Ход передается следующему игроку")
            release_field(field)
        except ValueError:
            print("Неверный ход. Ход передается следующему игроку")
            release_field(field)          
        try:
            move2(field)
            release_field(field)
            if is_finished(field, player1, player2) == True:
                break
            if empty not in field:
                print('Ничья!')
                break
        except IndexError:
            print("Неверный ход. Ход передается следуюему игроку")
            release_field(field)
        except ValueError:
            print("Неверный ход. Ход передается следующему игроку")
            release_field(field)   



if __name__ == '__main__':
    main()

