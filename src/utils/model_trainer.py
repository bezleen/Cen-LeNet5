import os

import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
from tqdm import tqdm

from src.utils.lenet5 import LeNet5


class ModelTrainer(object):
    def __init__(self, train_dataset, val_dataset, test_dataset, batch_size, learning_rate=0.001, num_epoch=2, pretrained_path=None):
        # note: use "pretrained_path" when you have a pretrained weights and want to continue training from that point
        self.batch_size = batch_size
        self.num_epoch = num_epoch
        self.train_dataloader = self.init_dataloader(train_dataset, self.batch_size, shuffle=True)
        self.val_dataloader = self.init_dataloader(val_dataset, self.batch_size, shuffle=True)
        self.test_dataloader = self.init_dataloader(test_dataset, self.batch_size, shuffle=True)
        self.net = self.init_network(pretrained_path=pretrained_path)
        self.loss_func = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(self.net.parameters(), lr=learning_rate, momentum=0.9)

    def init_network(self, pretrained_path=None):
        net = LeNet5()
        if not pretrained_path:
            return net
        load_weights = torch.load(pretrained_path)
        net.load_state_dict(load_weights)
        return net

    def init_dataloader(self, dataset, batch_size, shuffle=True):
        dataloader = data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
        return dataloader

    def train_step(self, epoch):
        print("     Training...")
        self.net.train()
        epoch_loss = 0.0
        epoch_corrects = 0.0
        for inputs, labels in tqdm(self.train_dataloader):
            self.optimizer.zero_grad()
            forward_output = self.net(inputs)
            loss = self.loss_func(forward_output, labels)
            _, preds = torch.max(forward_output, 1)
            loss.backward()
            self.optimizer.step()
            epoch_loss += loss.item() * inputs.size(0)
            epoch_corrects += torch.sum(preds == labels.data)

        epoch_loss = epoch_loss / len(self.train_dataloader.dataset)
        epoch_accuracy = epoch_corrects.double() / len(self.train_dataloader.dataset)
        print("Train: ", "epoch: ", epoch, ", loss: ", epoch_loss, "accuracy: ", epoch_accuracy.item() * 100, "%")
        return

    def validate_step(self, epoch):
        print("     Validating...")
        self.net.eval()
        epoch_loss = 0.0
        epoch_corrects = 0.0
        for inputs, labels in tqdm(self.val_dataloader):
            self.optimizer.zero_grad()
            forward_output = self.net(inputs)
            loss = self.loss_func(forward_output, labels)
            _, preds = torch.max(forward_output, 1)

            epoch_loss += loss.item() * inputs.size(0)
            epoch_corrects += torch.sum(preds == labels.data)

        epoch_loss = epoch_loss / len(self.val_dataloader.dataset)
        epoch_accuracy = epoch_corrects.double() / len(self.val_dataloader.dataset)
        print("Validate: ", "epoch: ", epoch, ", loss: ", epoch_loss, "accuracy: ", epoch_accuracy.item() * 100, "%")

    def save_model(self, save_path='data/model/weights_lenet5.pth'):
        if not os.path.exists("data"):
            os.mkdir("data")
        if not os.path.exists("data/model"):
            os.mkdir("data/model")

        torch.save(self.net.state_dict(), save_path)
        return

    def train(self, save_path='data/model/weights_lenet5.pth'):
        for epoch in range(1, self.num_epoch + 1):
            print(f"Epoch {epoch}/{self.num_epoch}")
            self.train_step(epoch)
            self.validate_step(epoch)

        self.save_model(save_path)
        return
