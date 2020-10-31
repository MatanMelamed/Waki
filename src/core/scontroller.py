from core.controller import Controller
from core.singleton import Singleton


class SController(Controller, metaclass=Singleton):
    def __init__(self, context, events=None):
        super().__init__(context, events)
