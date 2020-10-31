from tkinter import *
from tkinter import ttk

from models.context import Context
from src.core.m_window_ctrl import CoreMainWindowController
from widgets.awakening_chooser.awk_controller import AwController
from widgets.button_chooser.btn_controller import BtnController


class MainWindow(CoreMainWindowController):

    def __init__(self):
        super().__init__()

        self.frame = ttk.Frame(self)

        # add controllers
        self.aw_ctrl = AwController(ctx=Context(self, None, self))
        self.aw_ctrl.view.pack(side=LEFT)

        self.btn_ctrl = BtnController(ctx=Context(self, None, self))
        self.btn_ctrl.view.pack(side=RIGHT)
