import datetime
import time

from models.threads.pauseable_thread import PausableThread


class TimerThread(PausableThread):

    def __init__(self, time_step, function):
        super().__init__()
        self.time_step = time_step
        self.function = function
        self.accumulated_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
        self.resume_time = datetime.time(0, 0, 0)

    def _delta_since_last_resume(self):
        now = datetime.datetime.now().time()

        return datetime.timedelta(hours=now.hour - self.resume_time.hour,
                                  minutes=now.minute - self.resume_time.minute,
                                  seconds=now.second - self.resume_time.second)

    def resume(self):
        super().resume()
        self.resume_time = datetime.datetime.now().time()

    def pause(self):
        super().pause()
        self.accumulated_time += self._delta_since_last_resume()

    def routine(self):
        self.function(self._delta_since_last_resume() + self.accumulated_time)
        time.sleep(self.time_step)
