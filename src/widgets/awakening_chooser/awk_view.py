from tkinter import *
from tkinter import ttk

from PIL import ImageTk

from core.view import View
from definitions import AWK_IMAGE
from models.resource_manager import ResourceManager


class AwView(View):
    img_k = 'image_name'

    def __init__(self, context, img_name=AWK_IMAGE, **kw):
        super().__init__(context, **kw)

        self.img_name = img_name

        self.set_button = ttk.Button(self, text='Set')
        self.image = ttk.Label(self, text='image')
        self.val_list = Listbox(self, height=5)
        self.val_list.bindtags((self.val_list, self, "all"))

        self.set_button.grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self, text='Image Preview', font=('Arial', '10')).grid(row=1, column=0, pady=5)
        ttk.Label(self, text='Stats Preview', font=('Arial', '10')).grid(row=1, column=1, pady=5)
        self.image.grid(row=2, column=0, padx=10)
        self.val_list.grid(row=2, column=1, padx=10)

    def _refresh_image(self, image_name):
        pil_image = ResourceManager.get_image(image_name).resize((151, 85))
        # pil_image = ResourceManager.get_image(image_name)
        # pil_image.thumbnail((151, 85))
        img = ImageTk.PhotoImage(pil_image)
        self.image.configure(image=img)
        self.image.img = img

    def _refresh_values(self, stats_list):
        self.val_list.delete(0, END)

        for i, stat in enumerate(stats_list):
            self.val_list.insert(i + 1, f'{stat.name} {stat.value}')

    def update_view(self, stats_list=None, img_name=None):
        if stats_list is not None:
            self._refresh_values(stats_list)

        self._refresh_image(img_name if img_name else self.img_name)
