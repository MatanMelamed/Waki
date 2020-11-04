import io
import os

from PIL import Image

from core.singleton import Singleton
from definitions import RES_DIR, ROOT_DIR


class ResourceManager(metaclass=Singleton):

    @staticmethod
    def get_path(file_name):
        if os.path.isfile(file_name):
            return file_name
        if os.path.isfile(ROOT_DIR + f'\\{file_name}'):
            return ROOT_DIR + f'\\{file_name}'
        else:  # elif os.path.isfile(RES_DIR + f'\\{file_name}'):
            return RES_DIR + f'\\{file_name}'

    @staticmethod
    def get_file(res_path):
        with open(RES_DIR + f'\\{res_path}', 'rb') as input_file:
            data = input_file.read()
        return data

    @staticmethod
    def get_resource(res_path):
        with open(RES_DIR + f'\\{res_path}', 'rb') as input_file:
            data = input_file.read()
        return data

    @staticmethod
    def get_image(img):
        return Image.open(io.BytesIO(ResourceManager.get_resource(img)))
