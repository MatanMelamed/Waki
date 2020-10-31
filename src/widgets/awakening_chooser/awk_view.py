from tkinter import *
from tkinter import ttk

from PIL import ImageTk

from core.view import View
from definitions import AWK_IMAGE
from models.aw_image_processor import AwkImageProcessor
from models.utils.tools import get_image


class AwView(View):
    img_k = 'image_name'

    def __init__(self, context, img_name=AWK_IMAGE, **kw):
        super().__init__(context, **kw)
        # self.configure(bg='RED')

        self.img_name = img_name
        self.frame1 = Frame(self)
        self.clear_button = ttk.Button(self.frame1, text='Clear')
        self.set_button = ttk.Button(self.frame1, text='Set')

        ttk.Label(self, text='Image Preview', font=('Arial', '10')).grid(row=1, column=0, pady=5)
        ttk.Label(self, text='Stats Preview', font=('Arial', '10')).grid(row=1, column=1, pady=5)

        self.image = ttk.Label(self, text='image')
        self.val_list = Listbox(self, height=5)
        self.val_list.bindtags((self.val_list, self, "all"))

        self.frame1.grid(row=0, column=0, columnspan=2, pady=10)
        self.clear_button.pack(side=LEFT, padx=10)
        self.set_button.pack(side=RIGHT, padx=10)

        self.image.grid(row=2, column=0, padx=10)
        self.val_list.grid(row=2, column=1, padx=10)

    def _refresh_image(self):
        pil_image = get_image(self.img_name).resize((151, 85))
        img = ImageTk.PhotoImage(pil_image)
        self.image.configure(image=img)
        self.image.img = img

    def _refresh_values(self, stats_list):
        self.val_list.delete(0, END)

        for i, stat in enumerate(stats_list):
            self.val_list.insert(i + 1, f'{stat.name} {stat.value}')

    def update_view(self, stats_list):
        self._refresh_values(stats_list)
        self._refresh_image()
