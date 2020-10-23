from tkinter import Tk

from windows.awakening_window.awk_controller import AwController


class TkinterRunner:

    def __init__(self):
        self.controller1 = AwController()

    def run(self):
        self.controller1.mainloop()


if __name__ == '__main__':
    runner = TkinterRunner()
    runner.run()
