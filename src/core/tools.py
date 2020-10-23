import io
import pkgutil
import pyautogui

from PIL import Image

AWK_IMAGE = 'awk_img.jpg'
OK_IMAGE = 'ok_img.jpg'


def get_image(img):
    image_data = pkgutil.get_data('resources', img)
    return Image.open(io.BytesIO(image_data))


def takeBoundedScreenShot(x1, y1, x2, y2, file_name):
    im = pyautogui.screenshot(region=(x1, y1, x2, y2))
    im.save('resources/' + file_name)
