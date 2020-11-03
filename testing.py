import time
from tkinter import *
from tkinter import ttk

def click(l):
    print(l.curselection()[0])
    pass


app = Tk()
app.geometry('400x400+200+200')

l = Listbox(app)
l.pack()

for i in range(5):
    l.insert(END, f'text is {i}')

l.delete(0)

b = ttk.Button(app, text='click', command=lambda: click(l))
b.pack()

app.mainloop()

