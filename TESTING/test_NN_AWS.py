import os

os.system("cls")

from ImageProcessor import ImageProcessor  # type: ignore
from pyautogui import size
import cv2 as cv

path = os.getcwd()
folder = "NEURAL_NET_AWS"
cfg_file = f"{path}\\{folder}\\cfg\\yolov4-tiny-custom.cfg"
wights_file_last = f"{path}\\{folder}\\training\\yolov4-tiny-custom_last.weights"
wights_file_final = f"{path}\\{folder}\\training\\yolov4-tiny-custom_final.weights"

obj_path = f"{path}\\{folder}\\data"
img_path = f"{path}\\{folder}\\images"
dir = os.listdir(img_path)

width, height = size()
if height < 1600:
    width, height = 1200, 1600

processor = ImageProcessor(obj_path, (width, height), cfg_file, wights_file_last)  # type: ignore
print("creating images with labels", end="\r")
i = 0
for file in dir:
    i += 1
    times = int(i / 5)
    print("creating images with labels" + "." * times, end="\r")
    image = cv.imread(f"{img_path}/{file}")
    cv.waitKey()
    coordinates = processor.proccess_image(image, file)  # type: ignore

results = f"{path}\\TESTING\\results"
dir = os.listdir(results)
if len(dir) > 0:
    print("\nResult images ready!!!")
else:
    print("Error! images not created")
