import tkinter
from tkinter import *
from tkinter import ttk

from core.context import Context
from core.main_win_ctrl import CoreMainWindowController
from definitions import APP_TITLE
from widgets.awakening_chooser.awk_controller import AwController
from widgets.button_chooser.btn_controller import BtnController


class MainWindow(CoreMainWindowController):

    def __init__(self):
        super().__init__()

        # self.frame = ttk.Frame(self)
        ttk.Label(self, text=APP_TITLE, font=('Times', '24', 'bold')).pack(pady=50)

        # add controllers
        self.frame1 = ttk.LabelFrame(self, text='Awakening Window')
        self.frame1.pack(side=LEFT, padx=25, pady=10, ipadx=10, fill=tkinter.BOTH, expand=True)

        self.aw_ctrl = AwController(ctx=Context(self, None, self.frame1))
        self.aw_ctrl.view.pack(side=TOP, pady=10)

        self.frame2 = ttk.LabelFrame(self, text='Ok Button Window')
        self.frame2.pack(side=TOP, padx=25, pady=10, ipadx=10)

        self.btn_ctrl = BtnController(ctx=Context(self, None, self.frame2))
        self.btn_ctrl.view.pack(side=TOP, pady=10)
