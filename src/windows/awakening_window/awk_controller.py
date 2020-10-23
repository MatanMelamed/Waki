from core.base_main_controller import BaseMainController
from core.tools import AWK_IMAGE
from windows.awakening_window.awk_view import AwView
from windows.snipping.snp_controller import SnipperController, SnipperEvents


class AwController(BaseMainController):

    def __init__(self):
        super().__init__()

        self.view = AwView(self)
        self.view.set_button.configure(command=self.set_button)
        self.view.clear_button.configure(command=self.clear_button)

        self.snipper_controller = SnipperController(self)
        self.snipper_controller.add_observer(SnipperEvents.FINISHED_CROPPING, self.re)

    def re(self):
        print('main window finished cropping event triggered')
        self.view.refresh_awk_image()

    def clear_button(self):
        print('clear button')
        self.view.refresh_awk_image()

    def set_button(self):
        print('set button')
        self.snipper_controller.run(self, AWK_IMAGE)
