from core.controller import Controller
from definitions import DEFAULT_AWK_IMAGE
from models.aw_image_processor import *
from models.style_manager import StyleManager
from widgets.awakening_chooser.awk_view import AwView
from widgets.snipping_tool.snp_controller import SnippingController


class AwController(Controller):
    class AwEvents(Enum):
        SET_BUTTON = 0

    def __init__(self, ctx):
        super().__init__(ctx, [AwController.AwEvents])
        self.model = AwkImageProcessor()
        self.view = AwView(context=self.context)

        self.snp_ctrl = SnippingController()
        self.snp_ctrl.add_observer(SnippingController.SnippingEvents.FINISHED_SNIPPING, self.update)

        self.view.set_button.configure(command=self.set_button, style=StyleManager.unset_button)

        self.model.process_image(DEFAULT_AWK_IMAGE)
        self.view.update_view(self.model.get_stats(), img_name=DEFAULT_AWK_IMAGE)

    def set_button(self):
        print(f'{self.__class__.__name__} :: set_button')
        self.snp_ctrl.run(caller_window=self.context.window, new_file_name=self.view.img_name)

        self.notify_event(AwController.AwEvents.SET_BUTTON)

    def update(self):
        self.model.process_image(self.view.img_name)
        self.view.update_view(self.model.get_stats())

    def set_state(self, state=True):
        super().toggle_widget(self.view.set_button, state)
