from enum import Enum


class GenericEvents(Enum):
    DEFAULT = 0


class Observable:

    def __init__(self, events):
        self._observers = {}
        self._initialize_events(events)

    def _initialize_events(self, events):
        for event_type in events:
            self._observers[event_type] = []

    def add_observer(self, event_type, callback):
        if event_type in self._observers.keys():
            self._observers[event_type].append(callback)

    def remove_observer(self, event_type, callback):
        if event_type in self._observers.keys():
            self._observers[event_type].remove(callback)

    def notify_event(self, event_type):
        for callback in self._observers[event_type]:
            callback()
