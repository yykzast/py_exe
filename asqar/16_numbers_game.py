import random

EMPTY_MARK = 'x'

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

def shuffle_field(): # +
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = []
    
    for x in range(1, 16):
        field.append(x)
    
    field += [EMPTY_MARK]
    random.shuffle(field)
    
    return field



def print_field(field): 
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for x in range(0, len(field), 4):
        print(*field[x:x+4])
    

def is_game_finished(field):  
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    
    a = list(range(1,16))+[EMPTY_MARK]
    return field == a

def perform_move(field, key): # - 
    
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    x_index = field.index('x')
    if key == 'w' and x_index <= 3:
        raise IndexError()
    elif key == 's' and x_index >= 12:
        raise IndexError()
    elif key == 'a' and x_index%4 == 0:
        raise IndexError()
    elif key == 'd' and x_index%4 == 3:
        raise IndexError()

    delta = MOVES[key]
    new_index = x_index+delta
    field[x_index], field[new_index] = field[new_index], field[x_index]
    return field
    
    
    
    
def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    print('Передвиньте пустую ячейку. Используйте клавиши: w s a d')
    a = input('')
    while a not in MOVES.keys():
        a = input('Неверный ввод. Попробуйте еще раз:\n')
    return a

def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    pass

if __name__ == '__main__':
    field = shuffle_field()
    while is_game_finished(field) == False:
        print_field(field)
        try:
            key = handle_user_input()
            field = perform_move(field, key)
        except IndexError:
            print('Вы на краю плитки. Измените направление')
    main()





    