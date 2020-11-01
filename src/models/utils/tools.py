import io
import pyautogui

from PIL import Image

from definitions import RES_DIR


def get_image(img):
    with open(RES_DIR + '/' + img, 'rb') as input_file:
        image_data = input_file.read()
    # image_data = ResourceManager().get_resource(img)
    return Image.open(io.BytesIO(image_data))


def takeBoundedScreenShot(x1, y1, x2, y2, file_name):
    x2 = x1 + 1 if x2 == 0 else x2
    y2 = y1 + 1 if y2 == 0 else y2

    print(x1, x2, y1, y2)
    im = pyautogui.screenshot(region=(x1, y1, x2, y2))
    im.save(RES_DIR + f'\\{file_name}')


def is_int(str):
    try:
        return int(str)
    except ValueError:
        return None
