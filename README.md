# Download the data
## Follow the link
```
https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format
```
## then put it in the folder "data" with the name is 
```
hand_written.csv
```
# Install the requirements
```
pip install -r requirements.txt
```
# Initialize dataset
## run this command
``` 
python3 src/utils/utils.py 
```
# Train model
## setting some parameters in src/app.py
```
batch_size: int (default=20)
learning_rate: float (default=0.001)
num_epoch: int (default=2)
```
## exec train
```
python3 src/app.py 
```
The model_weight is saved in folder data/model with the name is "weights_lenet5.pth" by default.
# Predict
```
python3 predict/predict.py 
```
# Current Accuracy
```
98%
```