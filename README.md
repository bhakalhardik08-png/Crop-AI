# 🌾 Crop AI — Intelligent Crop Classification & Quality Grading

### Computer Vision for Crop Recognition + Guava Quality Analysis 🤖🌱

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red.svg)](https://keras.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Crop AI is a deep-learning agricultural computer-vision project that uses a **two-stage pipeline**:

1. **Crop classification** — identifies Banana, Guava, Maize, Rice, or Wheat.
2. **Quality grading** — when the predicted crop is Guava, a second model grades it as **A / B / C / Reject**.

> **Important:** The quality model is currently trained for Guava only. The project does not claim A/B/C/Reject grading for all five crops.

---

## 🚀 Pipeline

```text
📷 Crop Image
      ↓
🖼️ Resize to 224 × 224
      ↓
🧠 EfficientNetB0 — Crop Classifier
      ↓
🌾 Banana / Guava / Maize / Rice / Wheat
      ↓
   Is it Guava?
     ↙       ↘
   YES        NO
    ↓          ↓
🍈 EfficientNetB0   Quality: N/A
 Quality Model
    ↓
 A / B / C / Reject
```

The final system uses **two separately trained Keras models**, which makes the crop-recognition and quality-grading stages independently reusable.

## 🧠 Released Models

| Model | Architecture | Classes | Recorded test accuracy |
|---|---|---|---:|
| Crop Classification Champion | EfficientNetB0 | 5 crops | **91.76%** |
| Guava Quality Champion | EfficientNetB0 | A / B / C / Reject | **78.27%** |

### Crop Classification Champion

`model/CROP_MODEL_CHAMPION_91_76_TEST.keras`

- EfficientNetB0 transfer learning
- Input: 224 × 224 × 3
- Classes: Banana, Guava, Maize, Rice, Wheat
- Recorded final test accuracy: **91.76%**

The training notebook shows the EfficientNetB0 backbone, augmentation, global average pooling, dropout, and a 5-class softmax head. citeturn31file0

### Guava Quality Champion

`model/CROP_QUALITY_MODEL_CHAMPION_78_27_TEST.keras`

- EfficientNetB0
- Input: 224 × 224 × 3
- Classes: A, B, C, Reject
- Recorded final test accuracy: **78.27%**
- Evaluation test set reported in the notebook: **520 images**

The quality model uses EfficientNetB0 with augmentation, global average pooling, dropout, and a 4-class softmax head. citeturn30file1

---

## 📊 Dataset

### Crop Classification

**14,194 images total:**

| Crop | Images |
|---|---:|
| Wheat | 4,000 |
| Rice | 4,000 |
| Maize | 4,000 |
| Banana | 1,194 |
| Guava | 1,000 |
| **Total** | **14,194** |

The classification data was split using an **80% / 10% / 10% stratified train/validation/test split** with `random_state=42`. The resulting sets contain 11,355 training images, 1,419 validation images, and 1,420 test images. fileciteturn23file0

The complete raw dataset is intentionally not included in this repository.

### Quality Dataset

The quality workflow uses labelled Guava images with four classes:

**A · B · C · Reject**

---

## 🧪 Quick Inference

Clone the repository and install dependencies:

```bash
git clone https://github.com/prabhtheone/Crop-AI.git
cd Crop-AI
pip install -r requirements.txt
```

Run the included inference helper:

```bash
python src/predict.py path/to/your/image.jpg
```

Or open:

`notebook/Crop_AI_Inference_Demo.ipynb`

The demo loads the two released models and runs the same two-stage idea used by the project.

---

## 📁 Repository Structure

```text
Crop-AI/
├── model/
│   ├── CROP_MODEL_CHAMPION_91_76_TEST.keras
│   └── CROP_QUALITY_MODEL_CHAMPION_78_27_TEST.keras
├── notebook/
│   └── Crop_AI_Inference_Demo.ipynb
├── src/
│   └── predict.py
├── README.md
├── LICENSE
├── requirements.txt
├── .gitattributes
└── .gitignore
```

The `.keras` model files are tracked with **Git LFS**. The repository does not contain the raw training dataset.

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- EfficientNetB0
- NumPy
- Pillow
- Pandas
- Scikit-learn
- Matplotlib
- Google Colab
- Git LFS

---

## 📈 Evaluation Notes

The reported accuracies are evaluation results on the project's test data:

- Crop classification: **91.76%** test accuracy. fileciteturn24file2
- Guava quality grading: **78.27%** test accuracy on a reported 520-image test set. fileciteturn24file3

These numbers are **not guarantees of real-world accuracy**. Results may change with lighting, backgrounds, camera quality, crop varieties, image source, and other domain-shift conditions.

---

## ⚠️ Limitations

- Quality grading is currently available for **Guava only**.
- The project is a research/learning prototype, not a professional agricultural diagnosis system.
- Real-world robustness should be tested on larger and more diverse field images.
- Dataset licensing and attribution requirements should be checked for any third-party data used outside this repository.

---

## 🔮 Roadmap

- [x] Multi-crop classification
- [x] EfficientNetB0 transfer learning
- [x] Crop evaluation
- [x] Guava quality classification
- [x] A/B/C/Reject grading
- [x] Two-stage crop + quality inference
- [ ] Larger real-world robustness evaluation
- [ ] Quality labels for additional crops
- [ ] Web/mobile deployment
- [ ] Explainable AI / visual attention

---

## 🤝 Contributing

Ideas, bug reports, experiments, and improvements are welcome. Please open an issue or pull request with enough context to reproduce the change.

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE).

## ⭐ Support

If Crop AI is useful for your learning, experiments, or agricultural AI work, consider starring the repository and sharing constructive feedback.

---

**Built as a student project exploring AI, computer vision, and agriculture. 🌾🤖**
