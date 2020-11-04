from tkinter import ttk
from tkinter import *

from core.view import View


class ControlsView(View):

    def __init__(self, context, **kw):
        super().__init__(context, **kw)
        # self.configure(bg='red')

        self.start_button = ttk.Button(self, text='Stat')
        self.start_button.grid(pady=10)

        self.stop_button = ttk.Button(self, text='Stop')
        self.stop_button.grid(pady=10)

        size = 10
        pady = 5

        status_frame = Frame(self)
        status_frame.grid(pady=pady * 2, padx=10, sticky='e')

        ttk.Label(status_frame, text='Status', font=('Ariel', size, 'bold')).grid(row=2, column=0, pady=pady)
        self.lbl_status = ttk.Label(status_frame, text='Idle', font=('Ariel', size - 1))
        self.lbl_status.grid(row=2, column=1)

        ttk.Label(status_frame, text='Timer', font=('Ariel', size, 'bold')).grid(row=3, column=0, padx=10, pady=pady,
                                                                                 sticky='e')
        self.lbl_timer = ttk.Label(status_frame, text='00:00:00', font=('Ariel', size - 1))
        self.lbl_timer.grid(row=3, column=1)

        ttk.Label(status_frame, text='Step', font=('Ariel', size, 'bold')).grid(row=4, column=0, pady=pady)
        self.lbl_steps = ttk.Label(status_frame, text='0', font=('Ariel', size - 1))
        self.lbl_steps.grid(row=4, column=1)

        self.test_btn = ttk.Button(self, text='next')
        self.test_btn.grid()

    def set_status_label(self, status):
        self.lbl_status.configure(text=status)

    def set_timer(self, timer):
        self.lbl_timer.configure(text=timer)

    def set_step_counter(self, steps):
        self.lbl_steps.configure(text=steps)
