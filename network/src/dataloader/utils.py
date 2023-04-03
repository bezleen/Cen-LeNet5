import sys  # nopep8
sys.path.append(".")  # nopep8

import csv
import os

import numpy as np
import matplotlib.pyplot as plt
import pydash as py_
from PIL import Image
from bson.objectid import ObjectId

from network.src.config import LABEL


def convert_csv_to_jpg():
    # Download csv here: https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format then put it in folder "data" with the name is "hand_written.csv"
    with open('data/hand_written.csv', 'r') as csv_file:
        result = csv.reader(csv_file)
        for row in result:
            img_label = py_.get(LABEL,int(row[0]))
            folder_path = f"data/dataset/{img_label}"
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            x = np.array([int(j) for j in row[1:]])
            x = x.reshape(28, 28)
            x_padded = np.pad(x, pad_width=2, constant_values=0).astype(np.uint8) # from (28x28) to (32x32)
            
            img = Image.fromarray(x_padded)
            img_name = os.path.join(folder_path,f"{str(ObjectId())}.jpg")
            img.save(img_name)
    return
# if __name__ == '__main__':
#     convert_csv_to_jpg()