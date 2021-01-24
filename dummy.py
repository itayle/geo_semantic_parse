import torch

a= torch.tensor([[1,2,3]])

print(a.shape)
l = [a,a]
b = torch.cat(l, dim=0)
print(b)
print(b.shape)