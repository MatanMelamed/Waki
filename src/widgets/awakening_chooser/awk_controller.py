from core.controller import Controller
from models.aw_image_processor import *
from widgets.awakening_chooser.awk_view import AwView
from widgets.snipping_tool.snp_controller import SnippingController


class AwController(Controller):
    class AwEvents(Enum):
        SET_BUTTON = 0
        CLEAR_BUTTON = 1

    def __init__(self, ctx):
        super().__init__(ctx, [AwController.AwEvents])
        self.model = AwkImageProcessor()
        self.view = AwView(context=self.context)

        self.snp_ctrl = SnippingController()
        self.snp_ctrl.add_observer(SnippingController.SnippingEvents.FINISHED_SNIPPING, self.update)

        self.view.set_button.configure(command=self.set_button)
        self.view.clear_button.configure(command=self.clear_button)

    def set_button(self):
        print(f'{self.__class__.__name__} :: set_button')
        self.snp_ctrl.run(caller_window=self.context.window, new_file_name=self.view.img_name)

        self.notify_event(AwController.AwEvents.SET_BUTTON)

    def clear_button(self):
        print(f'{self.__class__.__name__} :: clear_button')

        self.view.update_view(self.model.get_stats())

        self.notify_event(AwController.AwEvents.CLEAR_BUTTON)

    def update(self):
        self.model.process_image('awk_img1.jpg')
        self.view.update_view(self.model.get_stats())
