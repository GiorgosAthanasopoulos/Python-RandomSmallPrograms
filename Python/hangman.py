import random
from typing import Counter

words = [
    'abyss',
    'bubbly',
    'buzz',
    'buff',
    'cozy',
    'fluff',
    'fluffy',
    'fizz',
    'fizzy',
    'fox',
    'jinx',
    'lucky',
    'puff',
    'jazz',
    'puffy',
    'puzzle',
    'quiz',
    'shabby',
    'zippy'
]

def winner(guess):
    counter = 0
    for i in range(len(guess)):
        if guess[i] != '' and guess[i] != '_':
            counter += 1
    if counter == len(guess):
        return True
    return False

def play():
    guess_word = words[random.randint(1, len(words)-1)]
    guess = []
    for i in range(len(guess_word)):
        guess.append('')
    temp = ''
    for i in range(1,len(guess_word)):
        if guess_word[0] ==  guess_word[i]:
            guess[i] = guess_word[0]
        else:
            guess[i] = '_'
    guess[0] = guess_word[0]
    tries = 10

    print(guess)

    while guess != guess_word and tries > 0:
        temp = input('enter guess')
        if len(temp)>1:
            if temp == guess_word:
                print('you found the word')
                break
            else:
                print('you tried to find the whole word and your try was incorrect so you lost')
                tries = 0
                break
        else:
            if guess_word.__contains__(temp):
                for i in range(len(guess_word)):
                    if guess_word[i] == temp:
                        guess[i] = temp
                print(guess)
                if winner(guess):
                    break
                continue
            else:
                tries -= 1
                print(guess)
                continue

    if tries > 0:
        print('congrats you won!')
    else:
        print('you lost...')


if __name__ == "__main__":
    play()
