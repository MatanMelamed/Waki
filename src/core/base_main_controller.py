from tkinter import Tk

from core.observable import Observable, GenericEvents


class BaseMainController(Tk, Observable):

    def __init__(self, event=GenericEvents):
        Tk.__init__(self)
        Observable.__init__(self, event)
