from enum import Enum
from tkinter import *
from tkinter import ttk

from core.observable import Observable


class ContEvents(Enum):
    A = 1,
    B = 2


def printi(o):
    print('printing object')
    print(o.__repr__())
    print(id(o))
    print()


class MyController(Observable):
    def __init__(self):
        super().__init__(ContEvents)

    def update(self):
        print('notifying')
        self.notify_event(ContEvents.A)


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('400x400+100+200')
        self.l = ttk.Label(self, text='first')
        self.l.pack()
        self.controller = MyController()
        printi(self.controller)
        self.controller.add_observer(ContEvents.A, self.update)
        self.side = SideWindow(self, self.controller)
        # self.side.withdraw()

    def update(self):
        print('update')
        self.l.configure(text='second')


class SideWindow(Toplevel):

    def __init__(self, master, c, **kw):
        super().__init__(**kw)
        self.geometry('400x400+300+100')
        self.master = master
        self.c = c
        printi(self.c)

        b = ttk.Button(self, text='clicka', command=self.exit)
        b.pack()

    def exit(self):
        print(id(self.c))

        self.c.update()
        self.destroy()


if __name__ == '__main__':
    print('test')
    app = MainWindow()
    app.mainloop()
