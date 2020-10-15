import win32ui
from PyQt5.uic.properties import QtGui
import win32gui

from Model.hook import screen_selection
from Model.screen_snipper import run_screen_snipper


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.initialize_view()

    def run(self):
        self.view.run_ui()


    def initialize_view(self):
        self.view.ui.btn_awk_set.clicked.connect(lambda: self.button())

    def button(self):
        # grab a handle to the main desktop window
        # hdesktop = win32gui.GetDesktopWindow()

        # create a device context
        # desktop_dc = win32gui.GetWindowDC(hdesktop)
        # win32gui.DrawFocusRect(desktop_dc, (0, 0, 100, 100))
        # d = run_screen_snipper()
        # print(f'is back with {d}')
        self.view.r()
