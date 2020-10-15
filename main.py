from Core.controller import Controller
from View.view_manager import ViewManager

if __name__ == "__main__":
    controller = Controller(ViewManager(), None)
    controller.run()
