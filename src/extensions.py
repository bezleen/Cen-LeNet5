from src.utils.image_transform import ImageTransform
from src.utils.dataset import Dataset
import src.constants as Consts
from src.config import LABEL_TO_NUM

image_transform = ImageTransform()

train_dataset = Dataset(image_transform, LABEL_TO_NUM, Consts.TRAIN)
val_dataset = Dataset(image_transform, LABEL_TO_NUM, Consts.VAL)
test_dataset = Dataset(image_transform, LABEL_TO_NUM, Consts.TEST)
