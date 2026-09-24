# ============================================================
# 1. IMPORTS
# ============================================================
from pathlib import Path
import shutil
import cv2
import yaml
import torch

#!pip install -q ultralytics
from ultralytics import YOLO

# ============================================================
# 2. CONFIGURATION (AJUSTADO A TU ESCRITORIO LOCAL)
# ============================================================

# Hi Emmaluz and Mateo: You only need to modify, at most, the following:
#
# 1. The video from which we take the samples (Solo el nombre del archivo):
#
VIDEO_NAME = "20260831_111348_f.mp4"
#
# 2. The original CVAT export folder. Please follow this naming convention:
#    CVAT_2026_09_17_test_01
#
CVAT_NAME = "CVAT_2026_09_23_test_02"
#
# 3. If you change the video or the YOLO base model, we need to run
#    the baseline model again:
#
RUN_BASELINE = False
#
# Don't change anything else! Hahaha

# ------------------------------------------------------------
# Rutas del Sistema Local (Mateo & Emmaluz)
# ------------------------------------------------------------
# Apunta automáticamente a la raíz de tu repositorio 'ERISE'
REPOS_ROOT = Path(__file__).resolve().parent

# Ruta de la carpeta de videos en el Escritorio (Desktop)
# Usando Path.home() funciona dinámicamente para el usuario 'MateoFlorez' o cualquier otro
DESKTOP_DIR = Path.home() / "Desktop" / "ERISE"
VIDEOS_DIR = DESKTOP_DIR / "Data_Videos_1_9-16-2026"

# ------------------------------------------------------------
# Archivos de entrada definitivos
# ------------------------------------------------------------
VIDEO = VIDEOS_DIR / VIDEO_NAME
CVAT_DIR = REPOS_ROOT / CVAT_NAME
CVAT_YAML = CVAT_DIR / "data.yaml"
CVAT_LABEL_DIR = CVAT_DIR / "labels" / "train"

# ------------------------------------------------------------
# Temporary dataset used for training
# ------------------------------------------------------------
WORK_DIR = REPOS_ROOT / "CAPcell_YOLO"

DATASET_DIR = WORK_DIR / "dataset"
IMAGE_DIR = DATASET_DIR / "images" / "train"
LABEL_DIR = DATASET_DIR / "labels" / "train"

# ------------------------------------------------------------
# Training outputs
# ------------------------------------------------------------
RUNS_DIR = REPOS_ROOT / f"runs_{CVAT_NAME}"

# ------------------------------------------------------------
# YOLO model & Parameters
# ------------------------------------------------------------
BASE_MODEL = "yolo26n.pt"
EPOCHS = 50
IMAGE_SIZE = 640
BATCH_SIZE = 8
CONFIDENCE = 0.20

# ============================================================
# 3. CHECK ENVIRONMENT
# ============================================================
print("=" * 60)
print("ENVIRONMENT")
print("=" * 60)

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

device = 0 if torch.cuda.is_available() else "cpu"
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("WARNING: No GPU detected, training will be on CPU (slower).")