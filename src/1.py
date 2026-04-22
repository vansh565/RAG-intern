import torch

print(torch.cuda.is_available())  # True means GPU ready

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

x = torch.tensor([1.0, 2.0]).to(device)
print(x)