import random
import time
import webbrowser

times = input('enter time for timer(format:MMM,DD,HH,MM,SS)')
times = times.split(',')

file = open('yt-links.txt','r')
links = []
for line in file:
    links.append(line)
url = links[random.randint(0,len(links)-1)]

found = False

while found == False:
    llocaltime = time.localtime()
    llocaltime = time.asctime(llocaltime)
    llocaltime = llocaltime.split()
    month = llocaltime[1]
    day = llocaltime[2]
    llocaltime = llocaltime[3].split(':')
    hour = llocaltime[0]
    minute = llocaltime[1]
    second = llocaltime[2]

    print(month,day,hour,minute,second)

    if times[0]==month:
        if times[1]==day:
            if times[2]==hour:
                if times[3]==minute:
                    if times[4]==second:
                        found=True
                        webbrowser.open(f'{url}')

