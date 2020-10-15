import pyHook


def onMouseDown(event):
    print(event)


def screen_selection():
    hm = pyHook.HookManager()
    hm.SubscribeMouseAllButtons(onMouseDown)
