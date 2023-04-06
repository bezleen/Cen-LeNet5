import sys  # nopep8
sys.path.append(".")  # nopep8

import csv
import os
import random

import numpy as np
import pydash as py_
from PIL import Image
from bson.objectid import ObjectId

from src.config import NUM_TO_LABEL


def convert_csv_to_jpg():
    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.exists("data/dataset"):
        os.mkdir("data/dataset")
    if not os.path.exists("data/dataset/train"):
        os.mkdir("data/dataset/train")
    if not os.path.exists("data/dataset/val"):
        os.mkdir("data/dataset/val")
    if not os.path.exists("data/dataset/test"):
        os.mkdir("data/dataset/test")
    # Download csv here: https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format then put it in folder "data" with the name is "hand_written.csv"
    train_val_test = ["train", "val", "test"]
    train_val_test_rate = (6, 2, 2)

    with open('data/hand_written.csv', 'r') as csv_file:
        result = csv.reader(csv_file)
        for row in result:
            role = random.choices(train_val_test, weights=train_val_test_rate, k=1)[0]
            img_label = py_.get(NUM_TO_LABEL, int(row[0]))
            folder_path = f"data/dataset/{role}/{img_label}"
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            x = np.array([int(j) for j in row[1:]])
            x = x.reshape(28, 28)
            x_padded = np.pad(x, pad_width=2, constant_values=0).astype(np.uint8)  # from (28x28) to (32x32)

            img = Image.fromarray(x_padded)
            img_name = os.path.join(folder_path, f"{str(ObjectId())}.jpg")
            img.save(img_name)
    return


if __name__ == '__main__':
    convert_csv_to_jpg()
