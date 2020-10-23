from tkinter import ttk

from PIL import ImageTk

from core.tools import get_image, AWK_IMAGE
from tests.models.base_view import BaseView


class AwView(BaseView):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.clear_button = ttk.Button(self, text='Clear')
        self.clear_button.grid(row=0, column=0)

        self.set_button = ttk.Button(self, text='Set')
        self.set_button.grid(row=0, column=1)

        self.image = ttk.Label(self, text='image')
        self.image.grid(row=1, column=0, columnspan=2)

        self.refresh_awk_image()

    def refresh_awk_image(self):
        img = ImageTk.PhotoImage(get_image(AWK_IMAGE))
        self.image.configure(image=img)
        self.image.img = img

    def update_ui(self):
        print('update ui')
        self.refresh_awk_image()
