from tkinter import ttk


class StyleManager:
    Title1 = 'Title.TLabelFrame.Label'

    def __init__(self):
        self.S = ttk.Style()
        self.S.configure(StyleManager.Title1, font=('Ariel', 15, 'bold'))
