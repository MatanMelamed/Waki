from enum import Enum

from core.controller import Controller
from core.context import Context
from models.utils.tools import takeBoundedScreenShot
from widgets.snipping_tool.snp_model import SnipperModel
from widgets.snipping_tool.snp_view import SnipperView


class SnippingController(Controller):
    class SnippingEvents(Enum):
        STARTED_SNIPPING = 0
        UPDATING_SNIPPING = 1
        FINISHED_SNIPPING = 2

    def __init__(self):
        super().__init__(Context(None, self, None), [SnippingController.SnippingEvents])

        self.file_name = ''
        self.caller = None

        self._model = SnipperModel()
        self.view = SnipperView(self.context)

    def start_snipping(self, x, y):
        self._model.start_snipping(x, y)
        self.view.create_rectangle(x, y)

        self.notify_event(SnippingController.SnippingEvents.STARTED_SNIPPING)

    def update_snipping(self, x, y):
        self._model.update_snipping(x, y)
        self.view.update_rectangle(*self._model.get_rectangle())

        self.notify_event(SnippingController.SnippingEvents.UPDATING_SNIPPING)

    def finish_snipping(self, x, y):
        self._model.finish_snipping(x, y)

        takeBoundedScreenShot(*self._model.get_rectangle(), self.file_name)

        self.caller.deiconify()
        self.view.disable()

        self.notify_event(SnippingController.SnippingEvents.FINISHED_SNIPPING)

    def get_rectangle(self):
        return self._model.get_rectangle()

    def run(self, caller_window, new_file_name):
        self.caller = caller_window
        self.caller.withdraw()
        self.file_name = new_file_name
        self.view.enable()
