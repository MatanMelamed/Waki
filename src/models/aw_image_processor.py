import cv2
import numpy as np
import pytesseract as tess

from models.resource_manager import ResourceManager
from models.stat import Stat
from enum import Enum

from core.observable import Observable
from core.singleton import Singleton

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class AwkImageProcessor(Observable, metaclass=Singleton):
    class AwkImgProcEvents(Enum):
        STARTED_IMG_PROC = 0
        FINISHED_IMG_PROC = 1

    def __init__(self):
        Observable.__init__(self, [AwkImageProcessor.AwkImgProcEvents])
        self.current_stats = []

    @staticmethod
    def _prepare_image(img_name):
        img_new_name = img_name.replace('\\', '/').rsplit('/', 2)
        img_new_name = img_new_name[0] if len(img_new_name) == 1 else img_new_name[1]
        img_new_name = f'processed_images/{img_new_name}'

        img_name = ResourceManager.get_path(img_name)
        img = cv2.imread(img_name)
        img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        img = cv2.filter2D(img, -1, kernel)
        img = cv2.multiply(img, 1.2)

        # img = cv2.bilateralFilter(img, 9, 75, 75)
        cv2.imwrite(ResourceManager.get_path(img_new_name), img)

        return img_new_name

    def process_image(self, img_file_name):
        self.current_stats.clear()
        img_file_name = self._prepare_image(img_file_name)

        img = ResourceManager.get_image(img_file_name)
        text = tess.image_to_string(img)

        lines = (s.strip().replace('.', '') for s in text.splitlines())
        raw_stats = (line.split('+') for line in lines if '+' in line)
        str_stats = ((a[0].strip(), a[1].strip().replace('%', '')) for a in raw_stats if len(a) >= 2)

        for a, b in str_stats:
            new_stat = Stat(a, b)
            if new_stat is not None:
                self.current_stats.append(new_stat)

        self.notify_event(AwkImageProcessor.AwkImgProcEvents.FINISHED_IMG_PROC)

    def get_stats(self):
        return self.current_stats
