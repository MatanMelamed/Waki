import tkinter as tk

from Model.config import AWK_FILE_NAME, BTN_FILE_NAME
from PIL import ImageTk, Image
import os


def start_main_ui():
    window = tk.Tk()
    window.geometry("800x600")
    # for i in range(2):
    #     for j in range(2):
    #
    #         label = tk.Label(master=frame, text=f'{i},{j}')
    #         label.pack()
    # global AWK_FILE_NAME, BTN_FILE_NAME
    # get_awakening_window_selection_widget(window,AWK_FILE_NAME).grid(row=0, column=0)
    # get_awakening_window_selection_widget(window,BTN_FILE_NAME).grid(row=0, column=1)

    tk.Label(master=window,
             text='~ FlyFF Awakening Bot ~',
             font="-weight bold",
             background='red',
             height=10).pack(pady=20, fill=tk.BOTH)

    upper_frame = tk.Frame(window, background="yellow")

    get_ok_button_selection_widget(upper_frame).grid(row=0, column=0, sticky='s')

    frame = tk.Frame(master=upper_frame, relief=tk.RAISED, borderwidth=5, background="blue", width=50, height=50)
    tk.Label(master=frame, text='@@@@@@@').pack()
    frame.grid(row=0, column=1, sticky='w')

    upper_frame.pack(fill=tk.BOTH)

    # get_ok_button_selection_widget(window).grid(row=0, column=1)

    # get_awakening_window_selection_widget().grid(row=0, column=0)
    # get_ok_button_selection_widget().grid(row=0, column=1)
    # window.grid_columnconfigure(2, minsize=100)
    # window.grid_rowconfigure(2, minsize=100)
    window.mainloop()


def get_ok_button_selection_widget(main_frame):
    frame = tk.LabelFrame(master=main_frame, relief=tk.RAISED, borderwidth=5, background="green", width=30, height=30)

    tk.Label(master=frame, text='Ok Button', width=25).grid(row=0, column=0, columnspan=2)

    tk.Button(master=frame, text='Clear', width=9).grid(row=1, column=0, pady=10)
    tk.Button(master=frame, text='Set', width=9).grid(row=1, column=1, pady=10)

    global BTN_FILE_NAME
    img = ImageTk.PhotoImage(Image.open(BTN_FILE_NAME))
    panel = tk.Label(master=frame, image=img, padx=10, pady=10)
    panel.image = img
    panel.grid(row=2, column=0, columnspan=2)

    return frame


def get_awakening_window_selection_widget(main_frame, s):
    frame = tk.Frame(master=main_frame, relief=tk.FLAT, borderwidth=5)

    tk.Label(master=frame, text='Awakening Window', width=25).pack()

    btn_frames = tk.Frame(master=frame)
    tk.Button(master=btn_frames, text='Clear', width=9).grid(row=1, column=0, pady=10)
    tk.Button(master=btn_frames, text='Set', width=9).grid(row=1, column=1, pady=10)
    btn_frames.pack()

    img = ImageTk.PhotoImage(Image.open(s))
    panel = tk.Label(master=frame, image=img, padx=10, pady=10)
    panel.image = img
    panel.pack()
    # panel.grid(row=2, column=0, columnspan=2)

    return frame
