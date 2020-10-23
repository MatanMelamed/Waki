from tkinter import Toplevel

from core.observable import Observable


class BaseSideController(Toplevel, Observable):

    def __init__(self, events, master=None):
        Toplevel.__init__(self, master=master)
        Observable.__init__(self, events)
