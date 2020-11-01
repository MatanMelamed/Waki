from tkinter import ttk


class StyleManager:
    unset_button = 'unset_btn.TButton'

    def __init__(self):
        style = ttk.Style()
        style.configure(StyleManager.unset_button, color='yellow')
