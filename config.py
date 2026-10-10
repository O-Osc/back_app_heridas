from pathlib import Path
import torch

BASE_DIR = Path(__file__).resolve().parent

# Carpetas
INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"
WEIGHTS_DIR = BASE_DIR / "weights"

# Modelos
WOUND_MODEL_PATH = WEIGHTS_DIR / "wound_model.pth"
TISSUE_MODEL_PATH = WEIGHTS_DIR / "tissue_model.pth"

# Tamaño de entrada del modelo
IMAGE_SIZE = (512, 512)

# Dispositivo
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Clases de tejido
TISSUE_CLASSES = {
    1: "Granular",
    2: "Epitelial",
    3: "Esfacelo",
    4: "Necrosis",
}