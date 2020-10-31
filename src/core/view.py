import tkinter as tk


class View(tk.Frame):

    def __init__(self, context, **kw):
        super().__init__(context.master, **kw)
        self.context = context
