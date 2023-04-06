# --- Open cmt line bellow if run by cmd: python *.py
import sys  # nopep8
sys.path.append(".")  # nopep8
# ----
from src.utils.predictor import Predictor

if __name__ == '__main__':
    predictor = Predictor("data/model/weights_lenet5.pth")
    # img_path = "data/dataset/test/j/642db0f263436e1e6a57f7d1.jpg"
    img_path = 'data/dataset/test/e/642db0e063436e1e6a578f8a.jpg'
    output = predictor.predict(img_path, show_img=True)
    print(output)
