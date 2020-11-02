from core.controller import Controller
from definitions import DEFAULT_OK_IMAGE
from models.aw_image_processor import *
from widgets.button_chooser.ok_view import OkView
from widgets.snipping_tool.snp_controller import SnippingController


class OkController(Controller):
    class OkEvents(Enum):
        SET_BUTTON = 0

    def __init__(self, ctx):
        super().__init__(ctx, [OkController.OkEvents])
        self.view = OkView(context=self.context)

        self.snp_ctrl = SnippingController()
        self.snp_ctrl.add_observer(SnippingController.SnippingEvents.FINISHED_SNIPPING, self.update)

        self.view.set_button.configure(command=self.set_button)

        self.view.update_view(img_name=DEFAULT_OK_IMAGE)

    def set_button(self):
        self.snp_ctrl.run(caller_window=self.context.window, new_file_name=self.view.img_name)

        self.notify_event(OkController.OkEvents.SET_BUTTON)

    def update(self):
        self.view.update_view()

    def get_rectangle(self):
        return self.snp_ctrl.get_rectangle()

    def set_state(self, state=True):
        super().toggle_widget(self.view.set_button, state)
