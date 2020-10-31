from core.controller import Controller
from models.aw_image_processor import *
from widgets.button_chooser.btn_view import BtnView
from widgets.snipping_tool.snp_controller import SnippingController


class BtnController(Controller):
    class BtnEvents(Enum):
        SET_BUTTON = 0
        CLEAR_BUTTON = 1

    def __init__(self, ctx):
        super().__init__(ctx, [BtnController.BtnEvents])
        self.view = BtnView(context=self.context)

        self.snp_ctrl = SnippingController()
        self.snp_ctrl.add_observer(SnippingController.SnippingEvents.FINISHED_SNIPPING, self.update)

        self.view.set_button.configure(command=self.set_button)
        self.view.clear_button.configure(command=self.clear_button)

    def set_button(self):
        print(f'{self.__class__.__name__} :: set_button')
        # self.snp_ctrl.run(caller_window=self.window, new_file_name=self.view.img_name)

        self.notify_event(BtnController.BtnEvents.SET_BUTTON)

    def clear_button(self):
        print(f'{self.__class__.__name__} :: clear_button')
        self.view.update_view()

        self.notify_event(BtnController.BtnEvents.CLEAR_BUTTON)

    def update(self):
        print(f'{self.__class__.__name__} :: update')
        self.view.update_view()
