"""Inference helper for the Crop AI two-stage pipeline.

Usage:
    python src/predict.py path/to/image.jpg

The crop model predicts one of:
    Banana, Guava, Maize, Rice, Wheat

The quality model is applied only when the predicted crop is Guava and
crop confidence is at least 50%.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import img_to_array, load_img

ROOT = Path(__file__).resolve().parents[1]
CROP_MODEL = ROOT / "model" / "CROP_MODEL_CHAMPION_91_76_TEST.keras"
QUALITY_MODEL = ROOT / "model" / "CROP_QUALITY_MODEL_CHAMPION_78_27_TEST.keras"

CROP_CLASSES = ["Banana", "Guava", "Maize", "Rice", "Wheat"]
QUALITY_CLASSES = ["A", "B", "C", "Reject"]
IMG_SIZE = (224, 224)


def load_image(path: str | Path) -> np.ndarray:
    image = load_img(path, target_size=IMG_SIZE)
    array = img_to_array(image).astype("float32")
    return np.expand_dims(array, axis=0)


def predict(image_path: str | Path) -> dict:
    crop_model = tf.keras.models.load_model(CROP_MODEL)
    quality_model = tf.keras.models.load_model(QUALITY_MODEL)

    array = load_image(image_path)

    crop_probs = crop_model.predict(array, verbose=0)[0]
    crop_index = int(np.argmax(crop_probs))
    crop = CROP_CLASSES[crop_index]
    crop_confidence = float(crop_probs[crop_index] * 100)

    result = {
        "crop": crop,
        "crop_confidence": round(crop_confidence, 2),
    }

    if crop == "Guava" and crop_confidence >= 50:
        quality_probs = quality_model.predict(array, verbose=0)[0]
        quality_index = int(np.argmax(quality_probs))
        result["quality"] = QUALITY_CLASSES[quality_index]
        result["quality_confidence"] = round(float(quality_probs[quality_index] * 100), 2)
    else:
        result["quality"] = None
        result["quality_confidence"] = None

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python src/predict.py path/to/image.jpg")

    image = Path(sys.argv[1])
    if not image.exists():
        raise SystemExit(f"Image not found: {image}")

    print(predict(image))
