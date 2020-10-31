from tkinter import ttk


class View(ttk.Frame):

    def __init__(self, context, **kw):
        super().__init__(context.master, **kw)
        self.context = context
