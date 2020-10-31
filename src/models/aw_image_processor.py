import pytesseract as tess

from models.stats_manager import Stat
from enum import Enum

from core.observable import Observable
from core.singleton import Singleton
from utils.tools import get_image

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class AwkImageProcessor(Observable, metaclass=Singleton):
    class AwkImgProcEvents(Enum):
        STARTED_IMG_PROC = 0
        FINISHED_IMG_PROC = 1

    def __init__(self):
        super().__init__([AwkImageProcessor.AwkImgProcEvents])
        self.current_stats = []

    def process_image(self, img_file_name):
        self.current_stats.clear()

        img = get_image(img_file_name)
        text = tess.image_to_string(img)

        lines = (s.strip() for s in text.splitlines())
        raw_stats = (line.split('+') for line in lines if '+' in line)
        str_stats = ((a[0].strip(), a[1].strip().replace('%', '')) for a in raw_stats if len(a) >= 2)

        for stat in (Stat(a, b) for a, b in str_stats):
            self.current_stats.append(stat)

        self.notify_event(AwkImageProcessor.AwkImgProcEvents.FINISHED_IMG_PROC)

    def get_stats(self):
        return self.current_stats
