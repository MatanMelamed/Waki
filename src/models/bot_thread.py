import time
from enum import Enum

from core.observable import Observable
from definitions import AWK_IMAGE
from models.aw_image_processor import AwkImageProcessor
from models.pauseable_thread import PauseableThread
from models.utils.tools import takeBoundedScreenShot, mouse_click, are_stats_satisfy


class BotThread(PauseableThread, Observable):
    class BotEvents(Enum):
        BOT_STARTED = 0
        BOT_LOOP_STATED = 1
        BOT_STOPPED = 2

    def __init__(self):
        PauseableThread.__init__(self)
        Observable.__init__(self, [BotThread.BotEvents])

        self.loop_count = 0
        self.aw_coords = []
        self.ok_coords = []
        self.conditions = []
        self.stats_image_processor = AwkImageProcessor()
        self.pause()

    def configure(self, aw_coords, ok_coords, conditions):
        self.aw_coords = aw_coords
        self.ok_coords = [ok_coords[0] + ok_coords[2] / 2, ok_coords[1] + ok_coords[3] / 2]
        self.conditions = conditions

    def routine(self):
        print('bot starting routine')
        self.notify_event(BotThread.BotEvents.BOT_LOOP_STATED)

        # screenshot
        print('bot screen shot')
        takeBoundedScreenShot(*self.aw_coords, AWK_IMAGE)

        # process data
        print('process data')
        self.stats_image_processor.process_image(AWK_IMAGE)
        current_stats = self.stats_image_processor.get_stats()
        print('result', current_stats)

        # check data
        if are_stats_satisfy(current_stats, self.conditions):
            print(current_stats, 'satisfying ', self.conditions)
            # done
            return

        # click
        print('clicking')
        mouse_click(*self.ok_coords)
        self.loop_count += 1
        time.sleep(2)
