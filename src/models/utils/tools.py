import io
import os

import pyautogui

from PIL import Image

from definitions import RES_DIR, ROOT_DIR


def takeBoundedScreenShot(x1, y1, x2, y2, file_name):
    x2 = x1 + 1 if x2 == 0 else x2
    y2 = y1 + 1 if y2 == 0 else y2

    im = pyautogui.screenshot(region=(x1, y1, x2, y2))
    im.save(RES_DIR + f'\\{file_name}')


def mouse_click(x, y):
    old_x, old_y = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.moveTo(old_x, old_y)


def is_stat_satisfy(stat, condition):
    if stat is None or condition is None:
        raise ValueError(f'tried to check if {stat} satisfy {condition}')
    return condition.name == stat.name and condition.value <= stat.value


def are_stats_satisfy(stats, conditions):
    conditions_copy = conditions.copy()

    for stat in stats:
        for condition in conditions_copy:
            if is_stat_satisfy(stat, condition):
                conditions.remove(condition)
                break

    return len(conditions) == 0


def is_int(str):
    try:
        return int(str)
    except ValueError:
        return None
