# 🌾 Crop AI — Intelligent Crop Classification & Quality Grading

### Turning Crop Images into Intelligent Agricultural Insights 🤖🌱

Crop AI is a deep-learning based agricultural computer-vision project that combines **crop classification** with **crop quality grading**.

The system first identifies the crop from an image and then, for the supported quality-analysis workflow, can grade **Guava** into **A / B / C / Reject** categories.

---

## 🚀 What the Project Does

```text
📷 Input Crop Image
        ↓
🖼️ Image Preprocessing (224×224)
        ↓
🧠 Crop Classification Model
        ↓
🌾 Banana / Guava / Maize / Rice / Wheat
        ↓
🍈 If Guava → Quality Grading Model
        ↓
🏷️ A / B / C / Reject
```

The final pipeline uses **two trained models** rather than one model containing both tasks:

1. **Crop Classification Champion** — identifies 5 crop categories.
2. **Quality Grading Champion** — grades Guava quality into A/B/C/Reject.

The notebook loads the crop champion and quality model separately for the final pipeline. 

## 🧠 Models

### 1. Crop Classification Champion

**File:** `model/CROP_MODEL_CHAMPION_91_76_TEST.keras`

- Architecture: **EfficientNetB0** transfer learning
- Classes: Banana, Guava, Maize, Rice, Wheat
- Test accuracy recorded for the champion: **91.76%**
- Input size: `224 × 224`
- Fine-tuned model selected as the project crop-classification champion

### 2. Quality Grading Champion

**File:** `model/CROP_QUALITY_MODEL_CHAMPION_78_27_TEST.keras`

- Architecture: **EfficientNetB0**
- Classes: A, B, C, Reject
- Test accuracy recorded for the champion: **78.27%**
- Used for the Guava quality-grading workflow

> **Important:** The quality model is currently used for **Guava** because that is the crop for which the project has quality labels. The pipeline therefore does not claim A/B/C/Reject grading for all five crops.

## 📊 Dataset

### Crop Classification Dataset

- **Total images:** 14,194
- **Wheat:** 4,000
- **Rice:** 4,000
- **Maize:** 4,000
- **Banana:** 1,194
- **Guava:** 1,000
- **Split:** 80% training / 10% validation / 10% test

The complete raw dataset is **not included** in this repository.

### Quality Dataset

The quality-grading workflow uses labelled Guava images divided into:

**A · B · C · Reject**

## 📈 Results

| Component | Model | Classes | Recorded Test Accuracy |
|---|---|---|---:|
| Crop Classification | EfficientNetB0 | 5 crops | **91.76%** |
| Guava Quality Grading | EfficientNetB0 | A/B/C/Reject | **78.27%** |

> These are recorded evaluation results on the project's test data. They should not be interpreted as guaranteed real-world accuracy. Performance can change with lighting, backgrounds, camera quality, crop varieties, image source, and other domain-shift factors.

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- EfficientNetB0
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Google Colab

## 📁 Repository Structure

```text
Crop-AI/
├── notebook/
│   └── Crop_AI_Project.ipynb
├── model/
│   ├── CROP_MODEL_CHAMPION_91_76_TEST.keras
│   └── CROP_QUALITY_MODEL_CHAMPION_78_27_TEST.keras
├── screenshots/
├── src/
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

## ⚡ Getting Started

Clone the repository:

```bash
git clone https://github.com/prabhtheone/Crop-AI.git
cd Crop-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the main notebook:

```text
notebook/Crop_AI_Project.ipynb
```

The notebook contains the dataset preparation, model training/evaluation, crop prediction, quality grading, and final combined prediction workflow.

## 🔮 Roadmap

- [x] Multi-crop image classification
- [x] EfficientNetB0 transfer learning
- [x] Data augmentation
- [x] Crop model evaluation
- [x] Guava quality analysis
- [x] A/B/C/Reject quality grading
- [x] Combined crop + quality prediction pipeline
- [ ] More diverse real-world robustness testing
- [ ] Quality grading for additional crops
- [ ] Web/mobile deployment
- [ ] Explainable AI / visual attention

## ⚠️ Limitations

This project is a university/research prototype. Predictions may be affected by image quality, lighting, backgrounds, crop varieties, camera conditions, and differences between training and real-world images.

The quality-grading component is currently designed around **Guava quality labels**, so A/B/C/Reject should not be assumed to apply to every crop category.

The system should not be treated as an agricultural diagnosis or professional decision-making system.

## 📌 Dataset & Model Notes

- Complete raw dataset files are not included because of size and redistribution considerations.
- Trained champion model files are included in `model/` when repository storage permits.
- If you use third-party datasets or images, check and comply with their original licenses and attribution requirements.

## 🤝 Contributing

Suggestions, improvements, experiments, and bug reports are welcome. Open an issue or submit a pull request with a clear description of the change.

## 📄 License

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

## ⭐ Support the Project

If you find Crop AI useful for learning, experimentation, or agricultural AI research, consider giving the repository a ⭐ and sharing feedback.

---

**Built as a university project exploring AI, computer vision, and agriculture. 🌾🤖**
