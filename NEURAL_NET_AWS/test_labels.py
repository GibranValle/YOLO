import sys
import os
from os import mkdir
from os.path import join, abspath, exists

# MADE TO RUN INDIVIDUALLY
os.system("cls")
PATH = sys.path
current = os.getcwd()
root = current
utils = abspath(join(root, "utils"))
path = current + "\\NEURAL_NET_AWS"

if utils not in PATH:
    PATH.append(utils)

from ImageProcessor import ImageProcessor  # type: ignore
from pyautogui import size
import cv2 as cv

width, height = size()
if height < 1600:
    width, height = 1200, 1600

obj_path = f"{path}\\data"
img_path = f"{path}\\images"
cfg_file = f"{path}\\cfg\\yolov4-tiny-custom.cfg"
wights_file_last = f"{path}\\training\\yolov4-tiny-custom_last.weights"
dir = os.listdir(img_path)
results = abspath(join(root, "RESULT_IMAGES"))
result_path = abspath(join(root, "RESULT_IMAGES", "NEURAL_NET_AWS"))
if not exists(results):  # type: ignore
    mkdir(results)
    if not exists(result_path):  # type: ignore
        mkdir(result_path)


processor = ImageProcessor(obj_path, (width, height), cfg_file, wights_file_last, result_path)  # type: ignore
print("Result images folder: ", result_path)
print("creating images with labels", end="\r")
i = 0
counter = 0
for file in dir:
    i += 1
    times = int(i / 5)
    print("creating images with labels" + "." * times, end="\r")
    image = cv.imread(f"{img_path}/{file}")
    cv.waitKey()
    coordinates = processor.proccess_image(image, file)  # type: ignore
    if coordinates != 0:
        counter += 1

dir = os.listdir(result_path)
if len(dir) > 0:
    print(f"\nResult {counter} images ready!!!")
else:
    print("Error! images not created")
