import os
from PIL import Image

current = os.path.dirname(__file__)
path = current + "\\"
files = os.listdir(path)
index = 0
suffix = "00"

for index, file in enumerate(files):
    _, extension = os.path.splitext(file)
    if extension == ".py":
        continue
    filename = path + file
    im = None

    with Image.open(path + file) as image_file:
        if index >= 0:
            suffix = "00"
        elif index > 9:
            suffix = "0"
        elif index > 99:
            suffix = ""

        im = image_file
        left = 0
        top = 0
        # 2M resolution
        right = 1200
        bottom = 1600
        im = im.crop((left, top, right, bottom))
        name = f"img_{suffix}{index}.png"
        print(name)
        saved = im.save(path + name)
        index += 1
