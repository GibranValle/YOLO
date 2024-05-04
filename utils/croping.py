import os
from PIL import Image

path = os.getcwd() + "\\images\\"

files = os.listdir(path)

for index, file in enumerate(files):
    filename = path + file
    im = None
    with Image.open(path + file) as image_file:
        im = image_file
        left = 0
        top = 0
        # 2M resolution
        right = 1200
        bottom = 1600
        im = im.crop((left, top, right, bottom))
    im.save(filename)
