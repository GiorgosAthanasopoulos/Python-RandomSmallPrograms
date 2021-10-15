import random
# rock paper scissors
l = ['rock','paper','scissors']
pointer = random.randint(0,2)
target = l[pointer]
user = input('rock paper or scissors\n')
print('PLAYER VS COMPUTER')
print('%s VS %s' % (user, target))
if user == 'rock':
    if target == user:
        print('tie')
    elif target == 'paper':
        print('lose')
    else:
        print('win')
elif user == 'paper':
    if target == user:
        print('tie')
    elif target == 'rock':
        print('win')
    else:
        print('lose')
elif user == 'scissors':
    if target == user:
        print('tie')
    elif target == 'paper':
        print('win')
    else:
        print('lose')
else:
    print('wrong input')
