found = False
data = []

temp = 0
for i in range(50):
    data.append(temp)
    temp += 2

key = ''
while not data.__contains__(key):
    key = int(input('enter key'))

found = False
start = 0
end = len(data)
counter = 1

while start <= end and found == False:
    mid = int((start + end) / 2)

    if data[mid]==key:
        found = True
    elif data[mid]>key:
        end = mid - 1
        counter += 1
    else:
        start = mid + 1
        counter += 1 

if found:
    print(f'found in {counter} attempt/s')
