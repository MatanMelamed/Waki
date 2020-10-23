from enum import Enum
from tkinter import Toplevel

from tests.models.base_controller import BaseController
from tests.windows.snipper.snp_view import SnipperView


class SnipperController(BaseController):
    class SnipperEvents(Enum):
        SNIPPER_START = 0
        SNIPPER_FINISHED = 1

    def __init__(self):
        super().__init__(SnipperController.SnipperEvents, Toplevel())
        self.view = SnipperView(self.root)
        self.caller = None

    def snipper_finished(self):
        print('finisehd')

    def run(self, caller):
        self.caller = caller
