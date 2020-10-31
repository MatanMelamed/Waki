from tkinter import *
from tkinter import ttk

from PIL import ImageTk

from core.view import View
from definitions import OK_IMAGE
from models.utils.tools import get_image


class BtnView(View):
    img_k = 'image_name'

    def __init__(self, context, img_name=OK_IMAGE, **kw):
        super().__init__(context, **kw)

        # self.configure(bg='BLUE')

        self.img_name = img_name
        self.buttons_frame = Frame(self)
        self.clear_button = ttk.Button(self.buttons_frame, text='Clear')
        self.set_button = ttk.Button(self.buttons_frame, text='Set')

        self.image = ttk.Label(self, text='image')

        self.buttons_frame.pack(pady=10)
        self.clear_button.pack(side=LEFT, padx=10)
        self.set_button.pack(side=RIGHT, padx=10)

        ttk.Label(self, text='Image Preview', font=('Arial', '10')).pack(pady=5)
        self.image.pack()

        self._refresh_image()

    def _refresh_image(self):
        pil_image = get_image(self.img_name).resize((130, 60))
        img = ImageTk.PhotoImage(pil_image)
        self.image.configure(image=img)
        self.image.img = img

    def update_view(self):
        print(f'Update Widget :: {self.__class__.__name__}')
        self._refresh_image()
