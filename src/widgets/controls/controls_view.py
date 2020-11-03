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

        self.state = ttk.Label(self, text='', font=('Ariel', 14))
        self.state.pack(padx=10, pady=10)

        self.run_counter = ttk.Label(self, text='', font=('Ariel', 14))
        self.run_counter.pack(padx=10, pady=10)

        self.test_btn = ttk.Button(self, text='next')
        self.test_btn.pack(padx=10, pady=10)

    def set_state_label(self, state):
        self.state.configure(text=state)

    def set_run_counter(self, count):
        self.run_counter.configure(text=count)
