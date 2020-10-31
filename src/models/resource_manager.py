from models.singleton import Singleton
from definitions import RES_DIR, OK_IMAGE, AWK_IMAGE


class ResourceManager(metaclass=Singleton):
    _resources = {}

    def get_resource(self, file_name):
        if file_name not in self._resources:
            with open(RES_DIR + f'\\{file_name}', 'rb') as input_file:
                self._resources[file_name] = input_file.read()
        return self._resources[file_name]

    def get_image(self, img_file_name):
        if img_file_name in (AWK_IMAGE, OK_IMAGE):
            with open(RES_DIR + f'\\{img_file_name}', 'rb') as input_file:
                input_file.read()
        return self.get_resource(img_file_name)

    def save_resource(self, file_name, data):
        if file_name not in self._resources:
            self._resources[file_name] = data
