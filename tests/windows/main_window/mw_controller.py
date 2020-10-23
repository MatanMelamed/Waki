from tkinter import Tk

from tests.models.base_controller import BaseController
from tests.windows.main_window.mw_view import MainView


class MainWindow(BaseController):

    def __init__(self):
        super().__init__(BaseController.GeneralEvents, Tk())
        self.view = MainView(self.root)


    def run(self):
        self.root.mainloop()
