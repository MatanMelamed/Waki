from abc import ABCMeta, abstractmethod
from threading import Thread, Event


class PausableThread(Thread, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self._running = Event()
        self._running.clear()

    def is_running(self):
        return self._running.is_set()

    def pause(self):
        self._running.clear()

    def resume(self):
        self._running.set()

    def run(self):
        self.setup()
        while True:
            self._running.wait()
            self.routine()

    def setup(self):
        pass

    @abstractmethod
    def routine(self):
        pass
