# Purpose:
# - Train a small CNN on MNIST (28x28 grayscale).
# - Log per-epoch metrics to CSV.
# - Save four PNG curves: train/val accuracy & train/val loss.
# - Save model weights (.pth).

import os, csv, random
from dataclasses import dataclass
from typing import List
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import shutil

def load_mnist_clean(data_dir, transform):
    """
    Try loading MNIST with download=True. If it fails due to a corrupted file,
    clean `raw/` and `processed/` folders and retry once.
    """
    raw_dir = os.path.join(data_dir, "MNIST", "raw")
    proc_dir = os.path.join(data_dir, "MNIST", "processed")

    def _safe_rm(path):
        try:
            if os.path.exists(path):
                shutil.rmtree(path)
        except Exception as e:
            print(f"[WARN] Failed to remove {path}: {e}")

    # First attempt
    try:
        train_ds = datasets.MNIST(root=data_dir, train=True, download=True, transform=transform)
        val_ds   = datasets.MNIST(root=data_dir, train=False, download=True, transform=transform)
        return train_ds, val_ds
    except Exception as e:
        print("[INFO] MNIST download failed once, cleaning cache and retrying...", e)

    # Clean and retry once
    _safe_rm(raw_dir)
    _safe_rm(proc_dir)
    train_ds = datasets.MNIST(root=data_dir, train=True, download=True, transform=transform)
    val_ds   = datasets.MNIST(root=data_dir, train=False, download=True, transform=transform)
    return train_ds, val_ds


# Utilities

def set_seed(seed: int = 42):
    """Best-effort reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

@dataclass
class EpochMetrics:
    epoch: int
    train_loss: float
    train_acc: float
    val_loss: float
    val_acc: float

def plot_curve(values: List[float], ylabel: str, out_path: str, xlabel: str = "Epoch"):
    """Save a single curve as a PNG."""
    plt.figure()
    plt.plot(range(1, len(values)+1), values, marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"{ylabel} over {xlabel.lower()}s")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

# Model

class SimpleCNN(nn.Module):
    """A small CNN for MNIST."""
    def __init__(self, num_classes: int = 10):
        super().__init__()
        # Input: (N,1,28,28)
        self.conv1 = nn.Conv2d(1, 32, 3, 1)   # -> (N,32,26,26)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)  # -> (N,64,24,24)
        self.pool  = nn.MaxPool2d(2, 2)       # -> (N,64,12,12)
        self.drop1 = nn.Dropout(0.25)
        self.fc1   = nn.Linear(64*12*12, 128) # 9216 -> 128
        self.drop2 = nn.Dropout(0.5)
        self.fc2   = nn.Linear(128, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = self.drop1(x)
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = self.drop2(x)
        x = self.fc2(x)
        return x

# Main training routine

def main():
    # Configs
    seed = 42
    epochs = 5
    batch_train, batch_val = 64, 1000
    lr = 1e-3
    data_dir = "data"
    out_dir  = "runs/mnist_baseline"
    os.makedirs(out_dir, exist_ok=True)

    # Setup
    set_seed(seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tfm = transforms.Compose([
        transforms.ToTensor(),
        # Standard MNIST normalization:
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_ds, val_ds = load_mnist_clean(data_dir, tfm)

    # Windows tip: num_workers=0 avoids multiprocessing issues on some setups.
    num_workers = 0 if os.name == "nt" else 2
    pin = (device.type == "cuda")

    train_loader = DataLoader(train_ds, batch_size=batch_train, shuffle=True,
                              num_workers=num_workers, pin_memory=pin)
    val_loader   = DataLoader(val_ds,   batch_size=batch_val,   shuffle=False,
                              num_workers=num_workers, pin_memory=pin)

    model = SimpleCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    history: List[EpochMetrics] = []

    # Train epochs
    for epoch in range(1, epochs+1):
        # Train
        model.train()
        total, correct, loss_sum = 0, 0, 0.0
        for x, y in train_loader:
            x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()

            loss_sum += loss.item() * x.size(0)
            correct  += (logits.argmax(1) == y).sum().item()
            total    += x.size(0)

        train_loss = loss_sum / total
        train_acc  = correct / total

        # Eval
        model.eval()
        total, correct, loss_sum = 0, 0, 0.0
        with torch.no_grad():
            for x, y in val_loader:
                x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
                logits = model(x)
                loss = criterion(logits, y)
                loss_sum += loss.item() * x.size(0)
                correct  += (logits.argmax(1) == y).sum().item()
                total    += y.size(0)

        val_loss = loss_sum / total
        val_acc  = correct / total

        history.append(EpochMetrics(epoch, train_loss, train_acc, val_loss, val_acc))
        print(f"[Epoch {epoch:02d}] "
              f"train_loss={train_loss:.4f} train_acc={train_acc:.4f} "
              f"val_loss={val_loss:.4f} val_acc={val_acc:.4f}")

    # Save artifacts
    # 1) Model weights
    torch.save(model.state_dict(), os.path.join(out_dir, "mnist_cnn.pth"))

    # 2) CSV log
    csv_path = os.path.join(out_dir, "metrics.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["epoch","train_loss","train_acc","val_loss","val_acc"])
        for m in history:
            w.writerow([m.epoch, m.train_loss, m.train_acc, m.val_loss, m.val_acc])

    # 3) Curves
    acc_tr = [m.train_acc for m in history]
    acc_va = [m.val_acc  for m in history]
    ls_tr  = [m.train_loss for m in history]
    ls_va  = [m.val_loss  for m in history]

    plot_curve(acc_tr, "Train Accuracy",      os.path.join(out_dir, "accuracy_train.png"))
    plot_curve(acc_va, "Validation Accuracy", os.path.join(out_dir, "accuracy_val.png"))
    plot_curve(ls_tr,  "Train Loss",          os.path.join(out_dir, "loss_train.png"))
    plot_curve(ls_va,  "Validation Loss",     os.path.join(out_dir, "loss_val.png"))

    print("Artifacts saved to:", out_dir)
    print("Final Val Acc: {:.2f}%".format(acc_va[-1]*100))

if __name__ == "__main__":
    main()