import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if device.type == "cuda":
        torch.backends.cudnn.benchmark = True

    tfm = transforms.ToTensor()
    train = datasets.MNIST(root="data", train=True, download=True, transform=tfm)
    test  = datasets.MNIST(root="data", train=False, download=True, transform=tfm)

    num_workers = 0 if os.name == "nt" else 2
    pin = (device.type == "cuda")

    train_loader = DataLoader(train, batch_size=128, shuffle=True,  num_workers=num_workers, pin_memory=pin)
    test_loader  = DataLoader(test,  batch_size=256, shuffle=False, num_workers=num_workers, pin_memory=pin)

    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(28*28, 128), nn.ReLU(),
        nn.Linear(128, 10)
    ).to(device)

    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()

    model.train()
    for x, y in train_loader:
        x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
        opt.zero_grad(set_to_none=True)
        loss = loss_fn(model(x), y)
        loss.backward()
        opt.step()

    model.eval()
    correct = total = 0
    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
            pred = model(x).argmax(1)
            correct += (pred == y).sum().item()
            total += y.size(0)

    print(f"Device: {device.type}")
    print(f"Test accuracy: {correct/total:.3f}")

if __name__ == "__main__":
    main()
