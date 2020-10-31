from core.observable import Observable


class SnipperModel(Observable):

    def __init__(self):
        Observable.__init__(self)
        self.start_x = 0
        self.start_y = 0
        self.cur_x = 0
        self.cur_y = 0

    def _update_coords(self, x, y, z, w):
        self.start_x, self.start_y = x, y
        self.cur_x, self.cur_y = z, w

    def get_coords(self):
        return [self.start_x, self.start_y, self.cur_x, self.cur_y]

    def start_snipping(self, x, y):
        ''' this method should be called when the snipping start'''
        self.start_x = self.cur_x = x
        self.start_y = self.cur_y = y

    def update_snipping(self, x, y):
        ''' this method should be called to update the mouse position'''
        self.cur_x, self.cur_y = (x, y)

    def finish_snipping(self, x, y):
        ''' this method should be called to end the snipping'''
        self.cur_x, self.cur_y = x, y

        if self.start_x <= self.cur_x and self.start_y <= self.cur_y:
            print("right down")
            self._update_coords(self.start_x, self.start_y, self.cur_x - self.start_x, self.cur_y - self.start_y)

        elif self.start_x >= self.cur_x and self.start_y <= self.cur_y:
            print("left down")
            self._update_coords(self.cur_x, self.start_y, self.start_x - self.cur_x, self.cur_y - self.start_y)

        elif self.start_x <= self.cur_x and self.start_y >= self.cur_y:
            print("right up")
            self._update_coords(self.start_x, self.start_y, self.cur_x - self.start_x, self.start_y - self.cur_y)

        elif self.start_x >= self.cur_x and self.start_y >= self.cur_y:
            print("left up")
            self._update_coords(self.cur_x, self.cur_y, self.start_x - self.cur_x, self.start_y - self.cur_y)

    def recPosition(self):
        print(self.start_x)
        print(self.start_y)
        print(self.cur_x)
        print(self.cur_y)
