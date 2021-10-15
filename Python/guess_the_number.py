import random

def play():
    range = int(input('enter range'))
    to_guess_number = random.randint(1, range)
    guess = 0

    while guess != to_guess_number:
        guess = int(input(f'guess number between 1 and {range}'))

        if guess > to_guess_number:
            print('too high.')
        elif guess < to_guess_number:
            print('too low.')

    print(f'congrats you guessed the correct number!({to_guess_number})')            

if __name__ == "__main__":
    play()
