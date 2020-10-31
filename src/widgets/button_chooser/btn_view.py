from tkinter import ttk

from PIL import ImageTk

from definitions import OK_IMAGE
from utils.tools import get_image
from archive.tests.models.base_view import View


class BtnView(View):
    img_k = 'image_name'

    def __init__(self, context, img_name=OK_IMAGE, **kw):
        super().__init__(context, **kw)

        self.img_name = img_name
        self.clear_button = ttk.Button(self, text='Clear')
        self.set_button = ttk.Button(self, text='Set')
        self.image = ttk.Label(self, text='image')

        self.clear_button.grid(row=0, column=0)
        self.set_button.grid(row=0, column=1)
        self.image.grid(row=1, column=0, columnspan=2)

        self._refresh_image()

    def _refresh_image(self):
        img = ImageTk.PhotoImage(get_image(self.img_name))
        self.image.configure(image=img)
        self.image.img = img

    def update_view(self, *args, **kwargs):
        print(f'Update Widget :: {self.__class__.__name__}')
        self._refresh_image()
