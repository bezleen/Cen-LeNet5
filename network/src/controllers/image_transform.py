
import torch
import torch.nn as nn


import src.constants as Consts

class ImageTransform():
    def __init__(self, resize: tuple, mean: tuple,std: tuple):
        self.data_transform= {
            Consts.TRAIN: 1
        }