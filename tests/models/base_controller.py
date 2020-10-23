from enum import Enum

from core.observable import Observable


class BaseController(Observable):
    class GeneralEvents(Enum):
        ANY = 0

    def __init__(self, events, root):
        super().__init__(events)
        self.root = root
