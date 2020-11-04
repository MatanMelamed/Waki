from tkinter import ttk

from PIL import ImageTk

from core.view import View
from definitions import OK_IMAGE
from models.resource_manager import ResourceManager


class OkView(View):
    img_k = 'image_name'

    def __init__(self, context, img_name=OK_IMAGE, **kw):
        super().__init__(context, **kw)

        self.img_name = img_name

        self.set_button = ttk.Button(self, text='Set')
        self.image = ttk.Label(self, text='image')

        self.set_button.pack(pady=10)
        ttk.Label(self, text='Image Preview', font=('Arial', '10')).pack(pady=7)
        self.image.pack(padx=10, pady=10)

    def _refresh_image(self, image_name):
        pil_image = ResourceManager.get_image(image_name).resize((130, 60))
        img = ImageTk.PhotoImage(pil_image)
        self.image.configure(image=img)
        self.image.img = img

    def update_view(self, img_name=None):
        self._refresh_image(img_name if img_name else self.img_name)
