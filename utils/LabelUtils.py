import os
from shutil import copy, make_archive


class LabelUtils:

    def create_labeled_images_zip_file(self):
        if not os.path.exists("obj"):
            os.mkdir("obj")

        file_prefixes = [
            f.split(".")[0] for f in os.listdir("label") if f.endswith(".txt")
        ]

        for prefix in file_prefixes:
            copy(f"label/{prefix}.txt", f"obj/{prefix}.txt")
            copy(f"images/{prefix}.png", f"obj/{prefix}.png")

        make_archive("yolov4-tiny/obj", "zip", ".", "obj")

    def create_labeled_images(self):
        if not os.path.exists("data/obj"):
            os.mkdir("data/obj")

        file_prefixes = [
            f.split(".")[0] for f in os.listdir("label") if f.endswith(".txt")
        ]

        for prefix in file_prefixes:
            copy(f"label/{prefix}.txt", f"data/obj/{prefix}.txt")
            copy(f"images/{prefix}.png", f"data/obj/{prefix}.png")

    def update_config_files(self, classes):  # type: ignore
        with open("./data/obj.names", "w") as file:
            file.write("\n".join(classes))  # type: ignore

        with open("./cfg/yolov4-tiny-custom_template.cfg", "r") as file:
            cfg_content = file.read()
            cfg_content = cfg_content.replace("_CLASS_NUMBER_", str(len(classes)))  # type: ignore
            cfg_content = cfg_content.replace(
                "_NUMBER_OF_FILTERS_", str((len(classes) + 5) * 3)  # type: ignore
            )
            cfg_content = cfg_content.replace(
                "_MAX_BATCHES_", str(max(6000, len(classes) * 2000))  # type: ignore
            )

        with open("./cfg/yolov4-tiny-custom.cfg", "w") as file:
            file.write(cfg_content)
