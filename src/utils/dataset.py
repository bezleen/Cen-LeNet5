# --- Open cmt line bellow if run by cmd: python *.py
# import sys  # nopep8
# sys.path.append(".")  # nopep8
# ----
import glob
import src.constants as Consts
import torch.utils.data as data
from PIL import Image


class Dataset(data.Dataset):
    TRAIN = "train"
    VAL = "val"
    TEST = "test"

    def __init__(self, transform, label_mapping, phase):
        self.transform = transform
        self.phase = phase
        self.label_mapping = label_mapping
        self.file_list = self.datapath_list()

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, index):
        img_path = self.file_list[index]
        img = Image.open(img_path)
        img_transformed = self.transform(img, self.TRAIN)
        label = img_path.split(self.phase)[1][1:2]
        num_label = self.label_mapping[label]
        return img_transformed, num_label

    def datapath_list(self):
        target_path = f"data/dataset/{self.phase}/**/*.jpg"
        path_list = []
        for path in glob.glob(target_path):
            path_list.append(path)
        return path_list
