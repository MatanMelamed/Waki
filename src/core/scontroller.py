from core.base_controller import Controller
from models.singleton import Singleton


class SController(Controller, metaclass=Singleton):
    def __init__(self, context, events=None):
        super().__init__(context, events)
