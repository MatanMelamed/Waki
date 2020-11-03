from tkinter import ttk
from tkinter import *

from core.view import View
from models.stat import Stat


class CMView(View):

    def __init__(self, context, **kw):
        super().__init__(context, **kw)

        # row 0
        ttk.Label(self, text='Choose a stat:').grid(row=0, column=0)
        ttk.Label(self, text='Insert min value:').grid(row=0, column=1)

        # row 1
        self.stat_chooser = ttk.Combobox(self, justify='center', state='readonly', width=10)
        self.stat_chooser.grid(row=1, column=0, padx=10)

        self.stat_value = ttk.Entry(self, width=7, justify='center')
        self.stat_value.grid(row=1, column=1, padx=10)

        self.add_btn = ttk.Button(self, text='Add', command=self.context.controller.add_condition)
        self.add_btn.grid(row=1, column=2, padx=10)

        # row 2
        style = ttk.Style()
        style.configure("Red.TLabel", foreground="red")
        self.error_label = ttk.Label(self, text='Value must be number.', style='Red.TLabel')
        self.error_label.grid(row=2, column=0, columnspan=2, pady=5)

        # row 3
        ttk.Label(self, text='Conditions:').grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='ws')

        # row 4
        self.remove_btn = ttk.Button(self, text='Remove', command=self.context.controller.remove_condition)
        self.remove_btn.grid(row=4, column=2, padx=25, pady=12, sticky='n')

        self.conditions = Listbox(self, width=26)
        self.conditions.grid(row=4, column=0, padx=10, columnspan=2, sticky='w')

        self.clear_btn = ttk.Button(self, text='Clear', command=self.context.controller.clear_all_stat_conditions)
        self.clear_btn.grid(row=4, column=2, pady=15, sticky='s')

        self.stat_chooser['values'] = list(Stat.NAMES.values())
        self.clear_error_value()

    def set_error_value(self):
        self.error_label.grid()

    def clear_error_value(self):
        self.error_label.grid_remove()

    def get_input(self):
        return self.stat_chooser.get(), self.stat_value.get()

    def clear_condition_maker(self):
        self.stat_chooser.set('')
        self.stat_value.delete(0, 'end')

    def add_condition(self, condition):
        self.conditions.insert(END, condition)

    def remove_condition(self, value=None):
        print(f'cm view :: remove_condition {value}')
        if value is None:
            value = self.conditions.get(ANCHOR)
            self.conditions.delete(ANCHOR)
        else:
            for i, item in enumerate(self.conditions.get(0, END)):
                if item == value:
                    self.conditions.delete(i)

        return value

    def clear_all_conditions(self):
        self.conditions.delete(0, END)

    def update_conditions(self, conditions_stats):
        self.conditions.delete(0, END)

        for i, stat in enumerate(conditions_stats):
            self.conditions.insert(i + 1, f'{stat.name} > {stat.value}')
