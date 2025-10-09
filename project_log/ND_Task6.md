# ND TASK 6 · MNIST Classification (LAB PRE)

**Date:** 2025-10-09  
**Goal:** Run a complete deep learning experiment loop on MNIST (grayscale, CNN) — training, validation, metrics logging (CSV), and plotting accuracy/loss curves.

---

## Setup
- Framework: PyTorch + Torchvision
- Model: Simple CNN (Conv2d×2 → MaxPool → Dropout → FC×2)
- Input: 1 × 28 × 28 grayscale images
- Optimizer: Adam (lr = 1e-3)
- Loss: CrossEntropyLoss
- Epochs: 5
- Batches: train=64, val=1000
- Output dir: `runs/mnist_baseline/`

---

## Commands
```powershell
python ai\mnist_curves.py
```

---

## Results
**Per-epoch metrics:**
```
[Epoch 01] train_loss=0.2100 train_acc=0.9362 val_loss=0.0527 val_acc=0.9816
[Epoch 02] train_loss=0.0836 train_acc=0.9760 val_loss=0.0357 val_acc=0.9886
[Epoch 03] train_loss=0.0660 train_acc=0.9806 val_loss=0.0375 val_acc=0.9873
[Epoch 04] train_loss=0.0552 train_acc=0.9840 val_loss=0.0305 val_acc=0.9897
[Epoch 05] train_loss=0.0478 train_acc=0.9857 val_loss=0.0328 val_acc=0.9888
```

**Final Validation Accuracy:** **98.88%**  
**Artifacts saved to:** `runs/mnist_baseline/`

- `mnist_cnn.pth` — trained weights  
- `metrics.csv` — per-epoch `train_loss, train_acc, val_loss, val_acc`  
- `accuracy_train.png`, `accuracy_val.png`  
- `loss_train.png`, `loss_val.png`

> Curves show the expected trend: accuracy ↑ and loss ↓ over epochs.

---

## Takeaways
- A minimal CNN learns MNIST to ~99% val accuracy within 5 epochs.
- The full experiment loop (data → model → train → eval → log → plot) is working and reproducible.
- This lab prepares for future tasks (e.g., RL baselines, controller training) by standardizing the experiment workflow.

---

## Appendix (Environment)
- Python venv: `.venv`
- Torch / Torchvision: see `env_check.py`
