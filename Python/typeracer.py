#timer 
import time
# api-imports
import requests
import json
import random
# gui-imports
import tkinter as tk
from tkinter import messagebox
 
# api - required fields are: (subject, verb, object): e.g. (cat, chew, gum)
def get_sentence()->str:
    subjects = [
        'cat',
        'dog',
        'bird',
        'human',
        'alien'
    ]
    verbs = [
        'eat',
        'drink',
        'play',
        'do',
        'fly'    
    ]
    objects = [
        'ball',
        'food',
        'tools',
        'mouse and keyboard',
        'computer'    
    ]
    rand1 = random.randint(0, len(subjects)-1)
    rand2 = random.randint(0, len(verbs)-1)
    rand3 = random.randint(0, len(objects)-1)
    response_api = requests.get('https://lt-nlgservice.herokuapp.com/rest/english/realise?subject=%s&verb=%s&object=%s' % (subjects[rand1],verbs[rand2],objects[rand3]))
    data = response_api.text
    parse_json = json.loads(data)
    active_case = parse_json['sentence']
    return active_case

# gui
class Application(tk.Tk):    
    def __init__(self):
        #spawning window
        tk.Tk.__init__(self)
        #size
        self.geometry('600x200')
        #title of window
        self.title('typeracer.py')
        #typeracer label
        title_label = tk.Label(self, text = 'Typeracer', font = 10)
        title_label.pack(padx = 3, pady = 3)
        #typeracer button
        start_button = tk.Button(self, text = "press me to start", command = start)
        start_button.pack(padx = 7, pady = 7)
        #entries
        entryText = tk.StringVar()
        Application.sentence_entry = tk.Entry(self, textvariable = entryText, width = 100)
        Application.input_entry = tk.Entry(self, width = 100)
        #score label
        Application.score_label = tk.Entry(self, width = 1)
        Application.score_label.pack(padx = 12, pady = 2 )
        Application.score_label.insert(0, Player.score)
      
# start game  
def start():
    if not Player.playing:
        Player.t0 = time.time()
        Player.pos += 1
        print('starting typeracer game')
        print('press enter to submit you try:')
        sentence = get_sentence() + get_sentence()
        Player.l.append(sentence)
        Player.playing = True
        Application.sentence_entry.pack(padx = 7, pady = 7)
        Application.input_entry.pack(padx = 7, pady = 9)
        Application.sentence_entry.delete(0, "end")
        Application.sentence_entry.insert(0 , str(sentence))
        Application.input_entry.bind('<Return>',Return_key_pressed)
        Application.score_label.insert(0, Player.score)
    else:
        print('already playing')

def Return_key_pressed(event):
    t1 = time.time()
    text = str(Application.input_entry.get())
    word_count = int(len(Player.l[Player.pos-1].split(' '))+1)
    Player.avg.append(int(word_count/(t1-Player.t0)))
    if text == Player.l[Player.pos-1]:
        correct = True
        Application.sentence_entry.delete(0, "end")
        Application.input_entry.delete(0, "end")
        Application.sentence_entry.pack_forget()
        Application.input_entry.pack_forget()
        Player.playing = False
        Player.score += 1
        messagebox.showinfo("Results", "You won")
        Application.score_label.insert(0, Player.score)
    else:
        correct = False
        Application.sentence_entry.delete(0, "end")
        Application.input_entry.delete(0, "end")
        Application.sentence_entry.pack_forget()
        Application.input_entry.pack_forget()
        Player.playing = False
        messagebox.showinfo("Results", "You lost")
        print(text,Player.l[Player.pos-1])
        Application.score_label.insert(0, Player.score)
    
#player class
class Player():
    playing = False
    pos = 0
    l = []
    score = 0
    avg = []
    t0 = time.time()

# entry point-main
app = Application()
app.mainloop()
