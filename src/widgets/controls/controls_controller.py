from core.controller import Controller
from widgets.awakening_chooser.awk_controller import AwController
from widgets.button_chooser.ok_controller import OkController
from widgets.condition_maker.cm_controller import CMController
from widgets.controls.controls_view import ControlsView


class ControlsController(Controller):

    def __init__(self, context, aw_ctrl, ok_ctrl, cm_ctrl):
        super().__init__(context)
        self.aw_ctrl = aw_ctrl
        self.ok_ctrl = ok_ctrl
        self.cm_ctrl = cm_ctrl

        self.view = ControlsView(context=self.context)
        self.view.start_button.configure(command=self.start)
        self.view.stop_button.configure(command=self.stop)

        self.is_aw_set = False or True
        self.is_ok_set = False or True

        aw_ctrl.add_observer(AwController.AwEvents.SET_BUTTON, lambda: self.update(aw=True))
        ok_ctrl.add_observer(OkController.OkEvents.SET_BUTTON, lambda: self.update(ok=True))
        for event in CMController.CMEvents:
            cm_ctrl.add_observer(event, self.update)

        self.toggle_widget(self.view.start_button, False)
        self.toggle_widget(self.view.stop_button, False)

    def start(self):
        print('start')
        # run routine
        self.toggle_widget(self.view.start_button, False)
        self.toggle_widget(self.view.stop_button, True)

        self.aw_ctrl.set_state(False)
        self.ok_ctrl.set_state(False)
        self.cm_ctrl.set_state(False)

    def stop(self):
        print('stop')
        # stop routine
        self.toggle_widget(self.view.start_button, True)
        self.toggle_widget(self.view.stop_button, False)

        self.aw_ctrl.set_state(True)
        self.ok_ctrl.set_state(True)
        self.cm_ctrl.set_state(True)

    def update(self, aw=None, ok=None):
        self.is_aw_set = aw if aw else self.is_aw_set
        self.is_ok_set = ok if ok else self.is_ok_set

        if self.is_aw_set and self.is_ok_set and self.cm_ctrl.get_conditions():
            self.toggle_widget(self.view.start_button, True)
        else:
            self.toggle_widget(self.view.start_button, False)
