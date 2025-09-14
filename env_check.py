import torch, torchvision, torchaudio
print("torch:", torch.__version__)
print("torchvision:", torchvision.__version__)
print("torchaudio:", torchaudio.__version__)

print("cuda available:", torch.cuda.is_available())
print("device count:", torch.cuda.device_count())

if torch.cuda.is_available():
    print("device name:", torch.cuda.get_device_name(0))

# verify torchvision.ops.nms exists and runs
from torchvision.ops import nms
import torch as T
boxes = T.tensor([[0,0,10,10],[1,1,9,9]], dtype=T.float32)
scores = T.tensor([0.9, 0.8], dtype=T.float32)
print("nms result:", nms(boxes, scores, 0.5))
