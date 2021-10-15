import random

def play(range):
    feedback = ''
    low = 1
    high = int(range)
    guess = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # or high
        feedback = input(f'is {guess} too high(h), too low(l), or corrrect(c)?')
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess -1            
    
    print('yay! the computer guessed your number')

if __name__ == "__main__":
    play(int(input('enter range')))
