from windows.awakening_window.awk_events import AwakeningEvents
from core.observable import Observable


class AwModel(Observable):

    def __init__(self):
        super().__init__(AwakeningEvents)
        self.stats_list = []
        self.is_running = False

    def start_processing(self):
        if self.is_running: return
        # process
        self.is_running = True
        self.notify_event(AwakeningEvents.IMAGE_PROCESS_FINISHED)
