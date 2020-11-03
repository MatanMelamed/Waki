from enum import Enum

from core.context import Context
from core.controller import Controller
from models.stat import Stat
from widgets.condition_maker.cm_view import CMView


class CMController(Controller):
    class CMEvents(Enum):
        CON_ADDED = 0
        CON_CLEARED = 1
        CON_REMOVED = 2

    def __init__(self, context):
        super().__init__(context, [CMController.CMEvents])

        self.view = CMView(context=Context(context.window, self, context.master))
        self._conditions = {}

    def get_conditions(self):
        return self._conditions.values()

    def remove_condition(self):
        removed_stat = Stat.convert_str_to_stat(self.view.remove_condition())
        del self._conditions[removed_stat.name]

        self.notify_event(CMController.CMEvents.CON_REMOVED)

    def _get_new_stat_from_input(self):
        new_stat = Stat(*self.view.get_input())

        # check new stat
        if new_stat is None:
            self.view.set_error_value()
        else:
            self.view.clear_error_value()

        return new_stat

    def _update_stat(self, new_stat):
        old_str = self._conditions[new_stat.name].__str__()
        self.view.remove_condition(old_str)
        self.view.add_condition(new_stat.__str__())
        self._conditions[new_stat.name] = new_stat

    def add_condition(self):
        new_stat = self._get_new_stat_from_input()
        if new_stat is None:
            return

        # check if new stat exists in conditions
        if new_stat.name in self._conditions:
            if new_stat.value > (self._conditions[new_stat.name]).value:
                # update stat
                self._update_stat(new_stat)
        else:
            # insert new stat
            self.view.add_condition(new_stat.__str__())
            self._conditions[new_stat.name] = new_stat

        self.notify_event(CMController.CMEvents.CON_ADDED)
        self.view.clear_condition_maker()

    def clear_all_stat_conditions(self):
        self._conditions.clear()
        self._idx_to_con.clear()
        self.view.clear_all_conditions()
        self.notify_event(CMController.CMEvents.CON_CLEARED)

    def set_state(self, state=True):
        super().toggle_widget(self.view.add_btn, state)
        super().toggle_widget(self.view.remove_btn, state)
        super().toggle_widget(self.view.clear_btn, state)
