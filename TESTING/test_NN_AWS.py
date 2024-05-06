import os
from os import mkdir
from os.path import exists

os.system("cls")

from ImageProcessor import ImageProcessor  # type: ignore
from pyautogui import size
import cv2 as cv

path = os.getcwd()
folder = "NEURAL_NET_AWS"
cfg_file = f"{path}\\{folder}\\cfg\\yolov4-tiny-custom.cfg"
wights_file_last = f"{path}\\{folder}\\training\\yolov4-tiny-custom_last.weights"
wights_file_final = f"{path}\\{folder}\\training\\yolov4-tiny-custom_final.weights"
wights_file_4icons = f"{path}\\{folder}\\weight\\aws_4icons.weights"
wights_file_9icons = f"{path}\\{folder}\\weight\\aws_9icons.weights"


print(wights_file_9icons)
obj_path = f"{path}\\{folder}\\data"
img_path = f"{path}\\{folder}\\images"
dir = os.listdir(img_path)

result = f"{path}\\RESULT_IMAGES"
result_path = f"{path}\\RESULT_IMAGES\\NEURAL_NET_AWS"
if not exists(result):  # type: ignore
    mkdir(result)
    if not exists(result_path):  # type: ignore
        mkdir(result_path)


width, height = size()
if height < 1600:
    width, height = 1200, 1600

processor = ImageProcessor(obj_path, (width, height), cfg_file, wights_file_9icons, result_path)  # type: ignore
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
