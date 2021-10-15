file = open('contacts-of-contact-book.txt', 'w')

cmd = ''

while cmd != 'exit':
    cmd = input('enter cmd ').split()
    
    if cmd[0] == '':
        print('wrong input.type /help to see all available commands')
    elif cmd[0] == 'exit':
        if len(cmd)!=1:
            print('wrong input.type /help to see all available commands')
        else:
            print('cya')
            exit()
    elif cmd[0] == 'add':
        if len(cmd)!=5:
            print('wrong input.type /help to see all available commands')
        else:
            file.write(f'{cmd[1]},{cmd[2]},{cmd[3]},{cmd[4]}\n')
    elif cmd[0] == 'save':
        if len(cmd)!=1:
            print('wrong input.type /help to see all available commands')
        else:
            print('saved')
    elif cmd[0] == 'find':
        if len(cmd)!=2:
            print('wrong input.type /help to see all available commands')
        else:
            file = open('contacts-of-contact-book.txt', 'r')
            for line in file:
                if line.__contains__(cmd[1]):
                    print(line)
            file = open('contacts-of-contact-book.txt', 'w')
    elif cmd[0] == 'update':
        if len(cmd)!=6:
            print('wrong input.type /help to see all available commands')
        else:
            file = open('contacts-of-contact-book.txt', 'r')
            buffer = ''
            for line in file:
                if line.__contains__(cmd[1]):
                    buffer += f'{cmd[2]},{cmd[3]},{cmd[4]},{cmd[5]}\n'
                else:
                    buffer += line + '\n'
            file = open('contacts-of-contact-book.txt', 'w')
            file.write(buffer)
    elif cmd[0] == 'delete':
        if len(cmd)!= 2:
            print('wrong input.type /help to see all available commands')
        else:
            file = open('contacts-of-contact-book.txt', 'r')
            buffer = ''
            for line in file:
                if not line.__contains__(cmd[1]):
                    buffer += line + '\n'
            file = open('contacts-of-contact-book.txt', 'w')
            file.write(buffer)
    elif cmd[0] == 'list':
        if len(cmd)!=1:
            print('wrong input.type /help to see all available commands')
        else:
            file = open('contacts-of-contact-book.txt', 'r')
            for line in file:
                print(line)
            file = open('contacts-of-contact-book.txt', 'w')
    elif cmd[0] == '/help':
        if len(cmd)!=1:
            print('wrong input.type /help to see all available commands')
        else:
            print('\
                exit \
                add $name $address $phone $email \
                save \
                find $key \
                update $key $name $address $phone $email \
                delete $key \
                list \
                help \
            ')
    else:
        print('wrong input.type /help to see all available commands')
    file.flush()

file.close()
