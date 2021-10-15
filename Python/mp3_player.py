import os
import time
import tkinter as tk
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('250x150')
        self.title('mp3player')
        Application.title_label = tk.Label(self, font = 10, text = "mp3player")
        Application.title_label.pack(padx = 2, pady = 2)
        text = tk.StringVar()
        Application.entry = tk.Entry(self, width = 20, textvariable = text)
        Application.entry.pack(padx = 2, pady = 4)
        Application.button = tk.Button(self, text = "submit", command = submit)
        Application.button.pack(padx = 2, pady = 6)
def submit():
    text = Application.entry.get()
    time.sleep(1)
    os.system("winamp " + text)
app = Application()
app.mainloop()
