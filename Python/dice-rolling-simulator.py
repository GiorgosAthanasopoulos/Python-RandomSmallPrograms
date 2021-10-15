import random
 
def roll():
    choice = input('wanna roll?(y or n)')
    if choice == 'y':
        return True
    return False

def get_number():
    print(int(random.randint(1, 6)))

while roll():
    dice = random.randint(1,6)
    print(f'dice says {dice}')

print('cya')
