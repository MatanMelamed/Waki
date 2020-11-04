import datetime
import os
import time

import cv2
import numpy as np

from models.aw_image_processor import AwkImageProcessor
from models.resource_manager import ResourceManager

# a = AwkImageProcessor()
# a.process_image('awk_img.jpg')
#

ac = datetime.timedelta(hours=0, minutes=59, seconds=59)
s = datetime.datetime.now().time()
time.sleep(1.11)
n = datetime.datetime.now().time()

d = datetime.timedelta(hours=n.hour - s.hour,
                       minutes=n.minute - s.minute,
                       seconds=n.second - s.second)

print(d + ac)

# for s in a.get_stats():
#     print(s)

# for i in range(5, 38):
#     a.process_image(f'test\\{i}_awk_img.jpg')
#     with open(f'resources/test/{i}_text_upgrade','w') as of:
#         for s in a.get_stats():
#             of.write(f'{s.__repr__()} ')
