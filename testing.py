import time
from tkinter import *
from tkinter import ttk

# app = Tk()
# app.geometry('400x400+200+200')
#
# s = ttk.Style()
# s.configure('My.TFrame', background='red')
#
# frame1 = ttk.Frame(master=app, style='My.TFrame',)
#
# frame1.config()
# frame1.pack()
#
# label = ttk.Label(frame1, text='text')
# label.grid(row=0, column=0, padx=10)
#
# app.mainloop()
from models.pauseable_thread import PauseableThread


class ConcreteThread(PauseableThread):

    def routine(self):
        print('doing some work!')
        time.sleep(1)


t = ConcreteThread()
t.start()
time.sleep(2)
t.pause()
time.sleep(2)
t.resume()
time.sleep(4)
print('finished')

