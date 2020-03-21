import random

list_ = ['мама', 'дом', 'машина']
word = random.choice(list_)
attemp = 3

list_ = []

for i in word:
    list_.append('-')

is_play = input('Сыграем в игру? Введите \'Да\'\n')

if is_play.upper() == 'ДА':
    print('Поехали.')
    while ''.join(list_) != word and attemp > 0:
        print('Угадай слово: ' + ''.join(list_))
        ans = input('Введите букву: ').lower()
        flag = False
        for i in range(len(word)):
            if word[i] == ans:
                list_[i] = ans
                flag = True
        if flag == False:
            attemp-=1
            print('Неверно. Осталось {} попыток'.format(attemp))
        if ''.join(list_) == word:
            print('Ура! Вы угадали! Слово: ', end = '')
            print(''.join(list_))
         
            
else:
    print('В следующий раз поиграем.')
