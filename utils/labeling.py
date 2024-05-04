import os
from utils.labeling_functions import LabelingFunctions

lb = LabelingFunctions(os.getcwd())
lb.find_folders()
lb.create_list()
lb.createLabels()