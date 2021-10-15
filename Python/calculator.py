from tkinter import *
import time
from threading import *
import locale
from tkinter.messagebox import askyesno

answer = askyesno('config', 'wanna change calculator colors?')

bgc = ''
fgi = ''
bgi = ''

if answer:
    colors = Tk()


    def enter():
        colors.destroy()
        pass


    bgc = StringVar()
    fgi = StringVar()
    bgi = StringVar()
    colors.title('config')
    colors.geometry('300x300')
    colors['bg'] = 'black'
    colors.resizable(False, False)
    temp_0 = Label(colors, text='enter colors for calculator:', font=('Fira Code', 12)).place(x=1, y=1)
    temp_1 = Label(colors, text='background', font=('Fira Code', 10)).place(x=25, y=50)
    temp_2 = Label(colors, text='bg', font=('Fira Code', 10)).place(x=25, y=100)
    temp_3 = Label(colors, text='fg', font=('Fira Code', 10)).place(x=25, y=150)
    temp4 = Entry(colors, textvariable=bgc).place(x=150, y=50)
    temp5 = Entry(colors, textvariable=bgi).place(x=150, y=100)
    temp6 = Entry(colors, textvariable=fgi).place(x=150, y=150)
    exit_b = Button(colors, text='Submit', font=('Fira Code', 20), command=enter).place(x=150, y=200)
    colors.mainloop()

if type(fgi) == str:
    if fgi == '':
        fgi = 'white'
    if bgi == '':
        bgi = 'cyan'
    if bgc == '':
        bgc = 'black'
else:
    fgi = fgi.get()
    bgi = bgi.get()
    bgc = bgc.get()

root = Tk()


def press_one():
    root.buffer += '1'
    pass


def press_two():
    root.buffer += '2'
    pass


def press_three():
    root.buffer += '3'
    pass


def press_four():
    root.buffer += '4'
    pass


def press_five():
    root.buffer += '5'
    pass


def press_six():
    root.buffer += '6'
    pass


def press_seven():
    root.buffer += '7'
    pass


def press_eight():
    root.buffer += '8'
    pass


def press_nine():
    root.buffer += '9'
    pass


def press_zero():
    root.buffer += '0'
    pass


def press_add():
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.buffer += '+'
    pass


def press_substract():
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.buffer += '-'
    pass


def press_multiply():
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.buffer += '*'
    pass


def format_():
    if not root.buffer.__contains__(',') and not (
            root.buffer.__contains__('+') or root.buffer.__contains__('-') or root.buffer.__contains__('*') or root.buffer.__contains__('/')):
        temp = list(str(root.buffer))
        count = 0
        for i in range(len(temp) - 1, -1, -1):
            count += 1
            if count == 3:
                count = 0
                temp.insert(i, ',')
        output = ''
        for i in range(len(temp)):
            output += temp[i]
        root.buffer = output
        if root.buffer[0] == ',':
            temp = list(str(root.buffer))
            temp[0] = ''
            output = ''
            for i in range(len(temp)):
                output += temp[i]
            root.buffer = output
    pass


def press_equals():
    if root.buffer.__contains__('+'):
        buf1, buf2 = root.buffer.split('+')
        buf1 = int(buf1)
        buf2 = int(buf2)

        root.buffer = str(buf1 + buf2)
        format_()
        pass
    elif root.buffer.__contains__('-'):
        buf1, buf2 = root.buffer.split('-')
        buf1 = int(buf1)
        buf2 = int(buf2)

        root.buffer = str(buf1 - buf2)
        format_()
        pass
    elif root.buffer.__contains__('*'):
        buf1, buf2 = root.buffer.split('*')
        buf1 = int(buf1)
        buf2 = int(buf2)

        root.buffer = str(buf1 * buf2)
        format_()
        pass
    elif root.buffer.__contains__('/'):
        buf1, buf2 = root.buffer.split('/')
        buf1 = int(buf1)
        buf2 = int(buf2)

        root.buffer = str(buf1 / buf2)
        format_()
        pass
    else:
        pass
    pass


def press_dot():
    root.buffer += '.'
    pass


def press_divide():
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.buffer += '/'
    pass


def buffer_flush():
    t1 = Thread(target=work)
    t1.start()
    pass


def work():
    try:
        while True:
            time.sleep(0.1)
            root.io_var.set(str(root.buffer))
    except:
        error = 'runtime error'
    pass


def press_backspace():
    length = len(root.buffer)
    root.buffer = root.buffer[:length - 1]
    pass


def press_mc():
    root.memory = []
    root.index = -1
    pass


def press_mplus():
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.memory.append(root.buffer)
        root.index += 1
    pass


def press_mr():
    if len(root.memory) >= 1 and 0 <= root.index < len(root.memory):
        root.buffer = root.memory[root.index]
        if root.index > 0:
            root.index -= 1
        else:
            root.index = len(root.memory) - 1
    pass


def press_clear():
    root.buffer = ''
    pass


def press_about():
    about = Tk()
    about.title('about')
    about.geometry('250x200')
    about['bg'] = bgc
    about.resizable(False, False)
    text = Text(about, width=30, height=25)
    text.insert(END,
                'Hello there!My name is George!\nI made this project for fun as part of my little project \nsolving streak for github!Hope you enjoy!(if you want to \ncontact me do it here:)\nathanassopoulosg@gmail.com')
    text['state'] = 'disabled'
    text.place(x=0, y=0)
    about.mainloop()
    pass

###
### TODO
### 

def press_one_(random_parameter):
    root.buffer += '1'
    pass


def press_two_(random_parameter):
    root.buffer += '2'
    pass


def press_three_(random_parameter):
    root.buffer += '3'
    pass


def press_four_(random_parameter):
    root.buffer += '4'
    pass


def press_five_(random_parameter):
    root.buffer += '5'
    pass


def press_six_(random_parameter):
    root.buffer += '6'
    pass


def press_seven_(random_parameter):
    root.buffer += '7'
    pass


def press_eight_(random_parameter):
    root.buffer += '8'
    pass


def press_nine_(random_parameter):
    root.buffer += '9'
    pass


def press_zero_(random_parameter):
    root.buffer += '0'
    pass


def press_add_(random_parameter):
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.buffer += '+'
    pass


def press_substract_(random_parameter):
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.buffer += '-'
    pass


def press_multiply_(random_parameter):
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.buffer += '*'
    pass

def press_equals_(random_parameter):
    if root.buffer.__contains__('+'):
        buf1, buf2 = root.buffer.split('+')
        buf1 = int(buf1)
        buf2 = int(buf2)

        root.buffer = str(buf1 + buf2)
        format_()
        pass
    elif root.buffer.__contains__('-'):
        buf1, buf2 = root.buffer.split('-')
        buf1 = int(buf1)
        buf2 = int(buf2)

        root.buffer = str(buf1 - buf2)
        format_()
        pass
    elif root.buffer.__contains__('*'):
        buf1, buf2 = root.buffer.split('*')
        buf1 = int(buf1)
        buf2 = int(buf2)

        root.buffer = str(buf1 * buf2)
        format_()
        pass
    elif root.buffer.__contains__('/'):
        buf1, buf2 = root.buffer.split('/')
        buf1 = int(buf1)
        buf2 = int(buf2)

        root.buffer = str(buf1 / buf2)
        format_()
        pass
    else:
        pass
    pass


def press_dot_(random_parameter):
    root.buffer += '.'
    pass


def press_divide_(random_parameter):
    if not root.buffer.__contains__('+') and not root.buffer.__contains__('-') and not root.buffer.__contains__(
            '*') and not root.buffer.__contains__('/'):
        root.buffer += '/'
    pass

def press_backspace_(random_parameter):
    length = len(root.buffer)
    root.buffer = root.buffer[:length - 1]
    pass

root.title('calculator')
root.geometry('500x560')
root['bg'] = bgc
root.resizable(False, False)

root.io_var = StringVar()
root.io_entry = Entry(root, textvariable=root.io_var, width=30, font=('Fira Code', 18), state='disabled').place(x=10,y=50)

root.buffer = ''
buffer_flush()
root.memory = []
root.index = -1

# components
one = Button(root, text='1', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_one, width=3).place(x=100, y=150)
two = Button(root, text='2', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_two, width=3).place(x=200, y=150)
three = Button(root, text='3', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_three, width=3).place(x=300, y=150)
four = Button(root, text='4', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_four, width=3).place(x=100, y=250)
five = Button(root, text='5', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_five, width=3).place(x=200, y=250)
six = Button(root, text='6', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_six, width=3).place(x=300, y=250)
seven = Button(root, text='7', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_seven, width=3).place(x=100, y=350)
eight = Button(root, text='8', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_eight, width=3).place(x=200, y=350)
nine = Button(root, text='9', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_nine, width=3).place(x=300, y=350)
zero = Button(root, text='0', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_zero, width=3).place(x=200, y=450)
add = Button(root, text='+', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_add, width=3).place(x=400, y=150)
substract = Button(root, text='-', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_substract, width=3).place(x=400, y=250)
multiply = Button(root, text='*', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_multiply, width=3).place(x=400,y=350)
divide = Button(root, text='/', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_divide, width=3).place(x=100,y=450)
dot = Button(root, text='.', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_dot, width=3).place(x=300, y=450)
backspace = Button(text='<=', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_backspace).place(x=25, y=150)
mc = Button(root, text='MC', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_mc).place(x=25, y=250)
mplus = Button(root, text='M+', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_mplus).place(x=25, y=350)
mr = Button(root, text='MR', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_mr).place(x=25, y=450)
equals = Button(root, text='=', bg=bgi, fg=fgi, font=('Fira Code', 20), command=press_equals, width=3).place(x=400,y=450)
clear = Button(root, text='C', bg=bgi, fg=fgi, font=('Fira Code', 12), command=press_clear, width=3, height=1).place(x=450, y=50)
about_B = Button(root, text='About', bg=bgi, fg=fgi, font=('Fira Code', 10), command=press_about, width=4).place(x=450, y=10)

# keyboard bindings
root.bind('1', press_one_)
root.bind('2', press_two_)
root.bind('3', press_three_)
root.bind('4', press_four_)
root.bind('5', press_five_)
root.bind('6', press_six_)
root.bind('7', press_seven_)
root.bind('8', press_eight_)
root.bind('9', press_nine_)
root.bind('0', press_zero_)
root.bind('+', press_add_)
root.bind('-', press_substract_)
root.bind('*', press_multiply_)
root.bind('/', press_divide_)
root.bind('<Key-Return>', press_equals_)
root.bind('.', press_dot_)
root.bind('<Key-BackSpace>',press_backspace_)

# run app
root.mainloop()
root.lift()
