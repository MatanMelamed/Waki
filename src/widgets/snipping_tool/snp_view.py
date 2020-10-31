from tkinter import *

from core.view import View


class SnipperView(View):

    def __init__(self, context, binds=None, **kw):
        context.window = Toplevel()
        context.master = context.window
        super().__init__(context, **kw)

        self.sc = None
        self.rect = None

        self.binds = binds if binds else self._get_def_binds()

        self.picture_frame = Frame(self.context.master, background="blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

        self.context.window.withdraw()
        self.context.window.attributes("-transparent", "blue")

    def _conv_points(self, x, y):
        return self.sc.canvasx(x), self.sc.canvasy(y)

    def _get_def_binds(self):
        return {
            "<ButtonPress-1>": lambda e: self.context.controller.start_snipping(*self._conv_points(e.x, e.y)),
            "<B1-Motion>": lambda e: self.context.controller.update_snipping(*self._conv_points(e.x, e.y)),
            "<ButtonRelease-1>": lambda e: self.context.controller.finish_snipping(*self._conv_points(e.x, e.y)),
        }

    def enable(self):
        print('running snipping view')
        self.context.window.deiconify()

        self.sc = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.sc.pack(fill=BOTH, expand=YES)

        for bind, function in self.binds.items():
            self.sc.bind(bind, function)

        self.sc.focus()

        self.context.window.attributes('-fullscreen', True)
        self.context.window.attributes('-alpha', .3)
        self.context.window.lift()
        self.context.window.attributes("-topmost", True)

    def disable(self):
        print("snipper exit")
        self.sc.destroy()
        self.context.window.withdraw()

    def create_rectangle(self, x, y):
        print('create rectangle')
        self.rect = self.sc.create_rectangle(x, y, x + 1, y + 1, outline='red', width=3, fill="blue")

    def update_rectangle(self, start_x, start_y, end_x, end_y):
        self.sc.coords(self.rect, start_x, start_y, end_x, end_y)
