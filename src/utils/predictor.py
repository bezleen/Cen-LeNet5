import torch
import numpy as np
import pydash as py_
from src.utils.lenet5 import LeNet5
from src.utils.image_transform import ImageTransform
from PIL import Image
import matplotlib.pyplot as plt
from src.config import NUM_TO_LABEL


class Predictor(object):
    def __init__(self, model_path):
        self.model = self.load_model(model_path)
        self.img_transform = ImageTransform()

    def load_model(self, model_path):
        load_weights = torch.load(model_path)
        net = LeNet5()
        net.load_state_dict(load_weights)
        return net

    def predict(self, img_path, show_img=False):

        img = Image.open(img_path)
        img_transformed = self.img_transform(img, "test")
        img_transformed = img_transformed.unsqueeze_(0)  # (channel, height, width) -> (1, channel, height, width)
        # predict
        output = self.model(img_transformed)
        letter_output = py_.get(NUM_TO_LABEL, np.argmax(output.detach().numpy()))
        if show_img:
            # (channel, height, width) -> (height, width, channel)
            plt.imshow(img)
            plt.show()
        return letter_output
