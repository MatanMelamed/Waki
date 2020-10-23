import pkgutil

from pkg_resources import resource_listdir


from src.core.tkinter_runner import TkinterRunner

if __name__ == "__main__":
    runner = TkinterRunner()
    runner.run()

