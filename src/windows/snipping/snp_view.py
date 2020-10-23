from tkinter import *
from tkinter import ttk

from tests.models.base_view import BaseView


class SnipperView(BaseView):

    def __init__(self, master, model, **kw):
        super().__init__(master, **kw)
        self.screenCanvas = None
        self.rect = None

        self.model = model
        self.picture_frame = Frame(self.master, background="blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

        self.master.withdraw()
        self.master.attributes("-transparent", "blue")

    def run(self):
        print('running snp view')
        self.master.deiconify()

        self.screenCanvas = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.screenCanvas.pack(fill=BOTH, expand=YES)

        self.screenCanvas.bind("<ButtonPress-1>", self.on_mouse_press)
        self.screenCanvas.bind("<B1-Motion>", self.on_mouse_move)
        self.screenCanvas.bind("<ButtonRelease-1>", self.model.finish_snipping)
        self.screenCanvas.focus()

        self.master.attributes('-fullscreen', True)
        self.master.attributes('-alpha', .3)
        self.master.lift()
        self.master.attributes("-topmost", True)

    def on_mouse_press(self, event):
        print('presed')
        self.model.start_snipping(self.screenCanvas.canvasx(event.x), self.screenCanvas.canvasy(event.y))

    def on_mouse_move(self, event):
        self.model.update_snipping(event)
        self.screenCanvas.coords(
            self.rect,
            self.model.start_x,
            self.model.start_y,
            self.model.cur_x,
            self.model.cur_y)

    def create_rectangle(self, x, y):
        print('create rec')
        self.rect = self.screenCanvas.create_rectangle(x, y, x + 1, y + 1, outline='red', width=3, fill="blue")

    def update_rectange(self, start_x, start_y, end_x, end_y):
        print('update rec')
        self.screenCanvas.coords(self.rect, start_x, start_y, end_x, end_y)

    def exit_snipper(self):
        print("snipper exit")
        self.screenCanvas.destroy()
        self.master.withdraw()
