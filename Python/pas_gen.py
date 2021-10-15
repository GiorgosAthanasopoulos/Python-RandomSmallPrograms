import string
import random
# 2 lower, 2 upper, 2 digits, 2 punctuation 
hint = input('enter hint ')

l = len(hint)
lower=0
upper=0
digits=0
punc=0

output = []
for char in hint:
    output.append(char)
for i in range(8-len(hint)):
    output.append(' ')

def check(output):
    lower = 0
    upper = 0
    digits = 0
    punc = 0
    for i in range(len(output)):
        if output[i].islower():
            lower+=1
        if output[i].isupper():
            upper+=1
        if output[i].isdigit():
            digits+=1
        if output[i] in string.punctuation:
            punc+=1
    if lower+upper+digits+punc >=8:
        return True
    else:
        return False

lower_ = 'abcdefghijklmnopqrstuvwxyz'
upper_ = lower_.upper()
digits_ = '1234567890'
punc_ = '!_-'

while  not check(output):
    if lower <2 :
        for i in range(2-lower):
            output.insert(random.randint(0,len(output)-1),lower_[random.randint(0,len(lower_)-1)])
            lower+=1
    if upper < 2:
        for i in range(2-upper):
            output.insert(random.randint(0,len(output)-1),upper_[random.randint(0,len(upper_)-1)])
            upper+=1
    if digits < 2:
        for i in range(2-digits):
            output.insert(random.randint(0,len(output)-1),digits_[random.randint(0,len(digits_)-1)])
            digits+=1
    if punc < 2:
        for i in range(2-punc):
            output.insert(random.randint(0,len(output)-1),punc_[random.randint(0,len(punc_)-1)])
            punc+=1

buffer = ''
for char in output:
    buffer += char
print(buffer.replace(" ",""))
