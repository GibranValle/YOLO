import glob, os
from LabelUtils import LabelUtils
from utils.labeling_constants import LABELS

lbUtils = LabelUtils()
lbUtils.create_labeled_images()
lbUtils.update_config_files(LABELS)  # type: ignore

# Current directory
current_dir = "data/obj"

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open("data/train.txt", "w")
file_test = open("data/test.txt", "w")

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.png")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write("data/obj" + "/" + title + ".png" + "\n")
    else:
        file_train.write("data/obj" + "/" + title + ".png" + "\n")
        counter = counter + 1
