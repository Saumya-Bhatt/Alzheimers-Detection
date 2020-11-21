import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import numpy as np

from PIL import Image

class NeuralNet(nn.Module):

    def __init__(self, output_dim):
        super().__init__()

        self.conv1 = nn.Conv2d(in_channels = 1, 
                               out_channels = 3, 
                               kernel_size = 5)
        
        self.conv2 = nn.Conv2d(in_channels = 3, 
                               out_channels = 3, 
                               kernel_size = 5)
        self.fc_1 = nn.Linear(10017, 5000)
        self.fc_2 = nn.Linear(5000, 250)
        self.fc_3 = nn.Linear(250, output_dim)

    def forward(self, x):
        x = self.conv1(x)
        x = F.max_pool2d(x, kernel_size = 2)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.max_pool2d(x, kernel_size = 2)
        x = F.relu(x)
        x = x.view(x.shape[0], -1)
        h = x
        x = self.fc_1(x)
        x = F.relu(x)
        x = self.fc_2(x)
        x = F.relu(x)
        x = self.fc_3(x)
        return x, h






def generate_results(imgFile):

  model = NeuralNet(4)
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  model = model.to(device)

  model.load_state_dict(torch.load('alzeimer.pth'))
  data_transforms = transforms.Compose([
      transforms.Grayscale(num_output_channels=1),
      transforms.Resize(224),
      transforms.ToTensor()
  ])

  def image_loader(image_name):
    """load image, returns cuda tensor"""
    image = Image.open(image_name)
    image = data_transforms(image).float()
    image = torch.tensor(image, requires_grad=True).clone().detach()
    image = image.unsqueeze(0)  #this is for VGG, may not be needed for ResNet
    return image.cuda()  #assumes that you're using GPU


  image = image_loader(imgFile)
  out=model(image)
  pred_labels = torch.argmax(out[0], 1)
  pred_labels

  if pred_labels == torch.Tensor([0]).to(device):
    return 1
  if pred_labels == torch.Tensor([1]).to(device):
    return 2
  if pred_labels == torch.Tensor([2]).to(device):
    return 3
  if pred_labels == torch.Tensor([3]).to(device):
    return 4