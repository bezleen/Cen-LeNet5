# --- Open cmt line bellow if run by cmd: python *.py
import sys  # nopep8
sys.path.append(".")  # nopep8
# ----
from src.extensions import train_dataset, val_dataset, test_dataset
from src.utils.model_trainer import ModelTrainer


if __name__ == '__main__':
    model_trainer = ModelTrainer(
        train_dataset,
        val_dataset,
        test_dataset,
        batch_size=20,
        learning_rate=0.001,
        num_epoch=2,
        pretrained_path='data/model/weights_lenet5.pth')
    model_trainer.train()
