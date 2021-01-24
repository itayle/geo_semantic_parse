import torch
import random

a = torch.tensor([[1,2],[3,4]])
b=torch.zeros(a.shape)
print(a.shape, b.shape)