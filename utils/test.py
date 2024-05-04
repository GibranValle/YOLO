from pyautogui import size
import os
from ImageProcessor import ImageProcessor
import cv2 as cv

path = os.getcwd()
cfg_file_name = f"cfg/yolov4-tiny-custom.cfg"
weights_file_name = f"training/yolov4-tiny-custom_last.weights"
processor = ImageProcessor(size(), cfg_file_name, weights_file_name)
imgs = "images2"
dir = os.listdir(imgs)
with open("results.txt", "w") as file:
    for img in dir:
        try:
            isDir = os.path.isdir(path + f"/images2/{img}")
            if isDir:
                continue
            image = cv.imread(f"images2/{img}")
            coordinates = processor.proccess_image(image)  # type: ignore
            founds = []
            for c in coordinates:
                name = c["class_name"]  # type: ignore
                founds.append(name)  # type: ignore
            print(f"in {img} found: {founds}")  # type: ignore
            file.write(f"in {img} found: {founds}\n")
        except cv.error:
            pass
