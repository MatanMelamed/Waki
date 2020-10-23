from tkinter import ttk

from tests.models.base_view import BaseView


class SnipperView(BaseView):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.label = ttk.Label(self, text='new window', width=20)
