from core.controller import Controller
from models.bot_thread import BotThread
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

        self.is_aw_set = False or True
        self.is_ok_set = False or True

        self.view = ControlsView(context=self.context)
        self.view.start_button.configure(command=self.start)
        self.view.stop_button.configure(command=self.stop)

        # listen to other widgets run_counter, to enable / disable start
        aw_ctrl.add_observer(AwController.AwEvents.SET_BUTTON, lambda: self._update_buttons_state(aw=True))
        ok_ctrl.add_observer(OkController.OkEvents.SET_BUTTON, lambda: self._update_buttons_state(ok=True))
        for event in CMController.CMEvents:
            cm_ctrl.add_observer(event, self._update_buttons_state)

        # set buttons to start disabled
        self.toggle_widget(self.view.start_button, False)
        self.toggle_widget(self.view.stop_button, False)

        self.bot_thread = BotThread()
        self.bot_thread.add_observer(BotThread.BotEvents.BOT_LOOP_STATED, self.update)
        self.bot_thread.add_observer(BotThread.BotEvents.BOT_STOPPED, self.bot_finished)
        self.bot_thread.start()

        self.view.test_btn.configure(command=self.test)

    def test(self):
        print(f'aw')
        ok_coords = self.ok_ctrl.get_rectangle()
        r = [ok_coords[0] + ok_coords[2] / 2, ok_coords[1] + ok_coords[3] / 2]
        print('ok button ', ok_coords, '\nok coords', r)
        pass

    def start(self):
        print('start')
        # run routine
        self.toggle_widget(self.view.start_button, False)
        self.toggle_widget(self.view.stop_button, True)

        self.bot_thread.configure(aw_coords=self.aw_ctrl.get_rectangle(),
                                  ok_coords=self.ok_ctrl.get_rectangle(),
                                  conditions=self.cm_ctrl.get_conditions())
        self.bot_thread.resume()

        self.aw_ctrl.set_state(False)
        self.ok_ctrl.set_state(False)
        self.cm_ctrl.set_state(False)

        self.view.set_state_label('_running')

    def stop(self):
        print('stop')
        # stop routine
        self.toggle_widget(self.view.start_button, True)
        self.toggle_widget(self.view.stop_button, False)

        self.bot_thread.stop()

        self.aw_ctrl.set_state(True)
        self.ok_ctrl.set_state(True)
        self.cm_ctrl.set_state(True)

    def _update_buttons_state(self, aw=None, ok=None):
        self.is_aw_set = aw if aw else self.is_aw_set
        self.is_ok_set = ok if ok else self.is_ok_set

        if self.is_aw_set and self.is_ok_set and self.cm_ctrl.get_conditions():
            self.toggle_widget(self.view.start_button, True)
        else:
            self.toggle_widget(self.view.start_button, False)

    def update(self):
        print('updating control')
        if self.bot_thread.is_running():
            self.view.set_run_counter(self.bot_thread.loop_count)
            self.aw_ctrl.update()

    def bot_finished(self):
        print('bot finished')
        self.stop()
        self.view.set_state_label('not _running')
