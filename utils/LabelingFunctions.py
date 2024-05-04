import os
import shutil

from labeling_constants import *


class LabelingFunctions:

    def __init__(self, cwd: str):
        self.root = cwd
        self.folders: list[str] = []
        self.list = {}

    def rename_pending(self):
        path = self.root + "\\renaming_pending\\"
        files = os.listdir(path)
        last_index = self.getLastIndex()
        for index, file in enumerate(files):
            if os.path.isdir(path + file):
                continue
            os.rename(path + file, path + f"img_{index+last_index}.png")

    def copy_from_folder_2_images(self):
        if not os.path.exists("images"):
            os.mkdir("images")
        index = 0
        self.find_folders()
        for folder in self.folders:
            path = f"{self.root}\\image_groups\\{folder}"
            dir = os.listdir(path)
            for file in dir:
                # suffix = ""
                # if index > 999:
                #     suffix = ""
                # elif index > 99:
                #     suffix = "0"
                # elif index > 9:
                #     suffix = "00"
                # elif index >= 0:
                #     suffix = "000"
                source = f"{self.root}\\image_groups\\{folder}\\{file}"
                destiny = f"{self.root}\\images\\{file}"
                index += 1
                # print(destiny, source)
                shutil.copy(source, destiny)

    def getLastIndex(self):
        path_images = os.getcwd() + "\\images\\"
        max = 0
        for file in os.listdir(path_images):
            if not os.path.isdir(path_images + file):
                num = int(file.replace("img_", "").replace(".png", ""))
                print(num)
                max = num if num > max else max
        return max

    def find_folders(self):
        path = self.root + "\\image_groups\\"
        print(path)
        dir = os.listdir(path)
        for file in dir:
            if os.path.isdir(f"{path}{file}"):
                self.folders.append(file)
        return self.folders

    def create_list(self):
        for folder in self.folders:
            path = f"{self.root}\\image_groups\\{folder}\\"
            dir = os.listdir(path)
            for file in dir:
                filepath = f"{path}{file}"
                if not os.path.isdir(filepath):
                    try:
                        self.list[file].append(f"{folder}")  # type: ignore
                    except KeyError:
                        self.list[file] = [f"{folder}"]  # type: ignore
        # print(list)  # type: ignore

    def create_label_folder(self):
        if not os.path.exists("label"):
            os.mkdir("label")
        for filename, labels in self.list.items():  # type: ignore
            filepath: str = f"{self.root}\\label\\{filename.replace('png', 'txt')}"  # type: ignore
            try:
                with open(filepath, "w") as file:
                    for label in labels:  # type: ignore
                        i = LABELS.index(label)  # type: ignore
                        p = POSITIONS[label]["position"]
                        # print(i, p)
                        text = f"{i} {p}"
                        file.write(text + "\n")
            except:
                pass
