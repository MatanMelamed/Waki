import tkinter
from tkinter import *
from tkinter import ttk

from core.context import Context
from core.main_win_ctrl import CoreMainWindowController
from definitions import APP_TITLE
from models.style_manager import StyleManager
from widgets.awakening_chooser.awk_controller import AwController
from widgets.button_chooser.ok_controller import OkController
from widgets.condition_maker.cm_controller import CMController
from widgets.controls.controls_controller import ControlsController


class MainWindow(CoreMainWindowController):

    def __init__(self):
        super().__init__()

        StyleManager()

        ttk.Label(self, text=APP_TITLE, font=('Times', '24', 'bold')).grid(row=0, column=0, columnspan=2, pady=50)

        # awakening window frame
        self.awk_frame = ttk.LabelFrame(self, text='Awakening Window')
        self.awk_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nw')  # , fill=tkinter.BOTH, expand=True

        # button window frame
        self.button_frame = ttk.LabelFrame(self, text='Ok Button Window')
        self.button_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nw')

        # condition maker frame
        self.condition_maker_frame = ttk.LabelFrame(self, text='Condition Maker')
        self.condition_maker_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nw')

        # controls frame
        self.controls_frame = ttk.LabelFrame(self, text='Control')
        self.controls_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nwse')

        # Controllers
        self.aw_ctrl = AwController(ctx=Context(self, None, self.awk_frame))
        self.aw_ctrl.view.pack(padx=10, pady=10)

        self.btn_ctrl = OkController(ctx=Context(self, None, self.button_frame))
        self.btn_ctrl.view.pack(padx=10, pady=10)

        self.cm_ctrl = CMController(context=Context(self, None, self.condition_maker_frame))
        self.cm_ctrl.view.pack(padx=10, pady=10)

        self.controls = ControlsController(Context(self, None, self.controls_frame),
                                           self.aw_ctrl,
                                           self.btn_ctrl,
                                           self.cm_ctrl)

        self.controls.view.place(relx=0.5, rely=0.5, anchor=CENTER)
