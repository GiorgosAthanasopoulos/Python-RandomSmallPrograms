questions = [
            'Which fictional city is the home of Batman?',
            'Which crime-fighting cartoon dog has the initals “S.D.” on his collar?',
            'What’s the total number of dots on a pair of dice?',
            'Traditionally, how many Wonders of the World are there?',
            'Which planet is the closest to Earth?',
            'According to the old proverb, to which European capital city do all roads lead?',
            'On which mountain did Moses receive the Ten Commandments?',
            'Which is the tallest mammal?',
            'Which sign of the zodiac is represented by the ram?',
            'Mount Everest is found in which mountain range?'
            ]
answers = [
            'Gotham',
            'Scooby Doo',
            '42',
            '7',
            'Venus',
            'Rome',
            'Sinai',
            'Giraffe',
            'Aires',
            'Himalayas'
          ]
score = 0
for i in range(0, len(questions)):
    correct = False
    print(questions[i] + '\n')
    answer = input('enter answer:\n')
    if answer.lower() == answers[i].lower():
        correct = True
    if correct:
        print('correct\n')
        score +=1
    else:
        print('wrong\n')
print('end,total score:%d\n' % (score))
