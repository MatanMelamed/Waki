from core.controller import Controller
from models.aw_image_processor import AwkImageProcessor
from models.threads.bot_thread import BotThread
from models.threads.timer_thread import TimerThread
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
        self.awk_img_processor = AwkImageProcessor()

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

        self.bot_thread = BotThread(self.context.window)
        self.bot_thread.add_observer(BotThread.BotEvents.BOT_LOOP_ENDED, self.update)
        self.bot_thread.add_observer(BotThread.BotEvents.BOT_STOPPED, self.bot_finished)
        self.bot_thread.start()

        self.timer_thread = TimerThread(0.1, self._update_timer)
        self.timer_thread.start()

        self.view.test_btn.configure(command=self.test)

    def test(self):
        print('controls :: test')
        self.bot_thread.configure(aw_coords=self.aw_ctrl.get_rectangle(),
                                  ok_coords=self.ok_ctrl.get_rectangle(),
                                  conditions=self.cm_ctrl.get_conditions(),
                                  refresh_time=float(self.view.get_refresh_time()))

        self.bot_thread.routine()
        self.update()
        print(self.view.get_refresh_time())

    def start(self):
        print('controls :: start')
        # run routine
        self.toggle_widget(self.view.start_button, False)
        self.toggle_widget(self.view.stop_button, True)
        self.aw_ctrl.set_state(False)
        self.ok_ctrl.set_state(False)
        self.cm_ctrl.set_state(False)

        self.view.set_status_label('Running')

        self.bot_thread.configure(aw_coords=self.aw_ctrl.get_rectangle(),
                                  ok_coords=self.ok_ctrl.get_rectangle(),
                                  conditions=self.cm_ctrl.get_conditions(),
                                  refresh_time=float(self.view.get_refresh_time()))

        self.bot_thread.resume()
        self.timer_thread.resume()

    def stop(self):
        print('controls :: stop')
        # stop routine
        self.toggle_widget(self.view.start_button, True)
        self.toggle_widget(self.view.stop_button, False)
        self.aw_ctrl.set_state(True)
        self.ok_ctrl.set_state(True)
        self.cm_ctrl.set_state(True)

        self.view.set_status_label('Idle')

        self.bot_thread.pause()
        self.timer_thread.pause()

    def _update_buttons_state(self, aw=None, ok=None):
        self.is_aw_set = aw if aw else self.is_aw_set
        self.is_ok_set = ok if ok else self.is_ok_set

        if self.is_aw_set and self.is_ok_set and self.cm_ctrl.get_conditions():
            self.toggle_widget(self.view.start_button, True)
        else:
            self.toggle_widget(self.view.start_button, False)

    def _update_timer(self, time_lapsed):
        self.view.set_timer('0' + str(time_lapsed))

    def update(self):
        print('controls :: update')
        self.view.set_step_counter(self.bot_thread.loop_count)
        self.aw_ctrl.update()
        s = self.awk_img_processor.get_stats()
        print(s)
        self.cm_ctrl.check_max_stat(s)

    def bot_finished(self):
        print('controls :: bot finished')
        self.stop()
        self.update()
        self.view.set_status_label('Success!')
