from core.observable import Observable
from windows.snipping.snp_controller import SnipperEvents


class SnipperModel(Observable):

    def __init__(self):
        super().__init__(SnipperEvents)
        self.start_x = 0
        self.start_y = 0
        self.cur_x = 0
        self.cur_y = 0

    def start_snipping(self, x, y):
        self.start_x, self.cur_x = x, x
        self.start_y, self.cur_y = y, y

        self.notify_event(SnipperEvents.STARTED_CROPPING)

    def update_snipping(self, event):
        self.cur_x, self.cur_y = (event.x, event.y)

    def finish_snipping(self, event):
        self.recPosition()

        if self.start_x <= self.cur_x and self.start_y <= self.cur_y:
            print("right down")
            self.update_coords(self.start_x, self.start_y, self.cur_x - self.start_x, self.cur_y - self.start_y)

        elif self.start_x >= self.cur_x and self.start_y <= self.cur_y:
            print("left down")
            self.update_coords(self.cur_x, self.start_y, self.start_x - self.cur_x, self.cur_y - self.start_y)

        elif self.start_x <= self.cur_x and self.start_y >= self.cur_y:
            print("right up")
            self.update_coords(self.start_x, self.start_y, self.cur_x - self.start_x, self.start_y - self.cur_y)

        elif self.start_x >= self.cur_x and self.start_y >= self.cur_y:
            print("left up")
            self.update_coords(self.cur_x, self.cur_y, self.start_x - self.cur_x, self.start_y - self.cur_y)

        self.notify_event(SnipperEvents.FINISHED_CROPPING)

    def update_coords(self, x, y, z, w):
        self.start_x, self.start_y = x, y
        self.cur_x, self.cur_y = z, w

    def clear(self):
        self.start_x, self.start_y = 0, 0
        self.cur_x, self.cur_y = 0, 0

    def recPosition(self):
        print(self.start_x)
        print(self.start_y)
        print(self.cur_x)
        print(self.cur_y)