from tkinter import ttk

from core.view import View


class ControlsView(View):

    def __init__(self, context, **kw):
        super().__init__(context, **kw)
        # self.configure(bg='red')
        self.start_button = ttk.Button(self, text='Stat')
        self.start_button.pack(padx=10, pady=10)

        self.stop_button = ttk.Button(self, text='Stop')
        self.stop_button.pack(padx=10, pady=10)
