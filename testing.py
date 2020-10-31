from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry('400x400+200+200')

s = ttk.Style()
s.configure('My.TFrame', background='red')

frame1 = ttk.Frame(master=app, style='My.TFrame',)

frame1.config()
frame1.pack()

label = ttk.Label(frame1, text='text')
label.grid(row=0, column=0, padx=10)

app.mainloop()
