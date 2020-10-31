import tkinter
from tkinter import Listbox

from definitions import AWK_IMAGE
from models.aw_image_processor import AwkImageProcessor
from widgets.button_chooser.btn_view import BtnView


class AwView(BtnView):
    def __init__(self, context, img_name=AWK_IMAGE, **kw):
        super().__init__(context, img_name, **kw)

        self.model = AwkImageProcessor()

        self.val_list = Listbox(self, height=5)
        self.val_list.bindtags((self.val_list, self, "all"))
        self.val_list.grid(row=1, column=2)

        self._refresh_values()

    def _refresh_values(self):
        self.val_list.delete(0, tkinter.END)
        stats = self.model.get_stats()
        for i, stat in enumerate(stats):
            self.val_list.insert(i + 1, f'{stat.name} {stat.value}')

    def update_view(self, stats_list):
        super().update_view()
        self._refresh_values()
