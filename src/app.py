# --- Open cmt line bellow if run by cmd: python *.py
import sys  # nopep8
sys.path.append(".")  # nopep8
# ----
from src.extensions import train_dataset, val_dataset, test_dataset


if __name__ == '__main__':
    print(train_dataset.__len__())
    print(train_dataset.__getitem__(0))
    print(val_dataset.__len__())
    print(val_dataset.__getitem__(0))
    print(test_dataset.__len__())
    print(test_dataset.__getitem__(0))
