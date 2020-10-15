import win32gui
from pynput.mouse import Listener

is_dragging = False
start = (0, 0)

# grab a handle to the main desktop window
hdesktop = win32gui.GetDesktopWindow()

# create a device context
desktop_dc = win32gui.GetWindowDC(hdesktop)


def on_move(x, y):
    if is_dragging:
        win32gui.DrawFocusRect(desktop_dc, (start[0], start[1], x, y))


def on_click(x, y, button, pressed):
    global is_dragging
    if f'{button.left}' == 'Button.left':
        global start
        if pressed:
            start = (x, y)
        is_dragging = pressed


if __name__ == '__main__':
    listener = Listener(on_move=on_move, on_click=on_click, on_scroll=None)
    listener.start()
    d = input('ffs')
    listener.stop()
