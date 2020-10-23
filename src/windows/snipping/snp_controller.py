from core.base_side_controller import BaseSideController
from core.tools import takeBoundedScreenShot
from windows.snipping.snp_events import SnipperEvents
from windows.snipping.snp_model import SnipperModel
from windows.snipping.snp_view import SnipperView


class SnipperController(BaseSideController):

    def __init__(self, master):
        super().__init__(SnipperEvents, master=master)
        self.file_name = ''
        self.caller = None

        self.model = SnipperModel()
        self.model.add_observer(SnipperEvents.STARTED_CROPPING, self.start_snipping)
        self.model.add_observer(SnipperEvents.FINISHED_CROPPING, self.end_snipping)

        self.view = SnipperView(self, self.model)

    def start_snipping(self):
        print('started snipping')
        self.view.create_rectangle(self.model.start_x, self.model.start_y)

    def end_snipping(self):
        takeBoundedScreenShot(
            self.model.start_x,
            self.model.start_y,
            self.model.cur_x,
            self.model.cur_y,
            self.file_name)
        self.notify_event(SnipperEvents.FINISHED_CROPPING)
        self.caller.deiconify()
        self.view.exit_snipper()

    def run(self, caller_master, new_file_name):
        self.caller = caller_master
        # self.caller.withdraw()
        self.file_name = new_file_name
        self.view.run()
