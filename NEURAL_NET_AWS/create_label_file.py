import sys
import os
from os import pardir
from os.path import join, abspath

PATH = sys.path
current = os.getcwd()
root = abspath(join(current, pardir))
utils = abspath(join(root, "utils"))
print(f"cwd: {current}")
print(f"root: {root}")

if utils not in PATH:
    PATH.append(utils)

from LabelingFunctions import LabelingFunctions  # type: ignore

lb = LabelingFunctions(current)  # type: ignore
labels = lb.find_folders()  # type: ignore


with open("label_list.py", "w") as file:
    file.write("LABELS = [")
    for label in labels:  # type: ignore
        file.write(f"'{label}', ")
    file.write("]")
