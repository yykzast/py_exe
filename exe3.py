import random

word_list = ['cisco','huawei','zte','nokia']

print("Hey, friend! \nDo you want to play the game 'Find the word'?")
entrance = input("Please enter 'yes' or 'no': ")

if entrance == 'yes':
    print("Lets go!")
    word = random.choice(word_list)
    print('Find the word with ' + str(len(word)) + ' letters!')
    w = [] # list of secret letters
    for i in word:
        w.append('-')
    sw = ''.join(w) # secret word
    a = 3 # number of attempts

    while True:
        if sw == word:
            print("Secret word: " + sw)
            print("You found word!")
            break

        print("Secret word: " + sw)
        x = input("Input any letter: ")

        if x not in word:
            a = a - 1
            print("Incorrect!")
            print("You have left "+str(a)+ " attempts!")
            if a == 0:
                print("Sorry...")
                break
        else:
            p = 0 # position in unknown list
            for i in word:
                if i == x:
                    w[p] = x
                    sw = ''.join(w)
                p = p + 1

else:
    print('Goodbye, my friend!!!')
