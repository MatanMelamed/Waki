from tkinter import ttk


class BaseView(ttk.Frame):

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        if self.master:
            self.pack()
