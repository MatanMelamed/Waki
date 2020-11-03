from abc import ABCMeta, abstractmethod
from threading import Thread, Event


class PauseableThread(Thread, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self._running = Event()
        self._running.clear()

    def is_running(self):
        return self._running.is_set()

    def pause(self):
        print('paused')
        self._running.clear()

    def resume(self):
        print('resume')
        self._running.set()

    def run(self):
        print('run')

        while True:
            self._running.wait()
            self.routine()

    @abstractmethod
    def routine(self):
        pass
