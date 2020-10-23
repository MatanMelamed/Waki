from tkinter import ttk


class MainView(ttk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.master = master
        self.pack()

        self.label = ttk.Label(self, text='initial text', width=10)
        self.label.pack()
