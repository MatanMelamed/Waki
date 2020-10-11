from pynput.mouse import Listener

is_dragging = False
coords = []


def on_move(x, y):
    if is_dragging:
        print(f"Mouse moved {x},{y}")


def on_click(x, y, button, pressed):
    global is_dragging
    if f'{button.left}' == 'Button.left':
        is_dragging = pressed


def get_mouse():
    listener = Listener(on_move=on_move, on_click=on_click, on_scroll=None)
    listener.start()
    d = input('ffs')
    listener.stop()



