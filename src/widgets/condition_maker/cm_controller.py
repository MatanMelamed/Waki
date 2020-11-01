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
        self._conditions = []

    def get_conditions(self):
        return self._conditions

    def delete_condition(self):
        deleted_stat_str = self.view.delete_condition()
        stat = Stat.convert_str_to_stat(deleted_stat_str)
        if stat:
            self._conditions.remove(stat)
            self.notify_event(CMController.CMEvents.CON_REMOVED)

    def add_condition(self):
        new_stat = Stat(*self.view.get_condition_maker())

        if new_stat is None:
            self.view.set_error_value()
        else:
            self.view.clear_error_value()
            self._conditions.append(new_stat)
            self.view.add_condition(new_stat.__str__())
            self.notify_event(CMController.CMEvents.CON_ADDED)

        self.view.clear_condition_maker()

    def clear_all_stat_conditions(self):
        self._conditions.clear()
        self.view.clear_all_conditions()
        self.notify_event(CMController.CMEvents.CON_CLEARED)

    def set_state(self, state=True):
        super().toggle_widget(self.view.add_btn, state)
        super().toggle_widget(self.view.remove_btn, state)
        super().toggle_widget(self.view.clear_btn, state)
