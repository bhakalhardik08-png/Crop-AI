# 🌾 Crop AI

### Turning Crop Images into Intelligent Agricultural Insights 🤖

> An AI-powered crop image classification system built with TensorFlow/Keras and MobileNetV2 to identify **Wheat, Rice, Maize, Banana, and Guava** from images.

<p align="center">
  <b>14,194 Images</b> · <b>5 Crop Classes</b> · <b>MobileNetV2</b> · <b>TensorFlow/Keras</b> · <b>93.74% Validation Accuracy</b>
</p>

---

## 🚀 Project Overview

Crop AI is a university project focused on applying deep learning and computer vision to agricultural image classification.

The system takes a crop image and predicts which of five supported crop categories it belongs to:

**🌾 Wheat · 🍚 Rice · 🌽 Maize · 🍌 Banana · 🍈 Guava**

The model uses **MobileNetV2 transfer learning** with ImageNet-pretrained weights and a 224×224 input size.

## 🧠 How It Works

```text
📷 Crop Image
      ↓
🔄 Image Preprocessing
      ↓
🧠 MobileNetV2 Feature Extraction
      ↓
🎯 Classification Head
      ↓
🌾 Predicted Crop Class
```

## 📊 Dataset

- **Total images:** 14,194
- **Wheat:** 4,000
- **Rice:** 4,000
- **Maize:** 4,000
- **Banana:** 1,194
- **Guava:** 1,000
- **Split:** 80% training / 10% validation / 10% test

## 🏆 Model Performance

The best recorded model achieved **93.74% validation accuracy** on the project's held-out validation set.

> **Important:** 93.74% is validation-set performance. It should not be interpreted as guaranteed real-world accuracy. External images can perform differently because of lighting, background, camera quality, crop variety, and other domain-shift factors.

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- MobileNetV2
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Google Colab

## 📁 Repository Structure

```text
Crop-AI/
├── notebook/          # Training and evaluation notebook
├── model/             # Trained model files (if distributed)
├── screenshots/       # Results and prediction visuals
├── src/               # Supporting source files
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

The main training and evaluation workflow is available in `notebook/Crop_AI_Project.ipynb`.

## 🔮 Roadmap

- [x] Multi-crop image classification
- [x] Transfer learning with MobileNetV2
- [x] Data augmentation
- [x] Model evaluation
- [ ] More real-world robustness testing
- [ ] Web/mobile deployment
- [x] Crop quality analysis
- [x] A/B/C/Reject quality grading
- [x] Farmer-focused prediction interface

## ⚠️ Limitations

This project is a university/research prototype. Predictions can be affected by image quality, lighting, backgrounds, crop varieties, and differences between training and real-world images. It should not be treated as an agricultural diagnosis or professional decision-making system.

## 📌 Dataset & Model Notes

The repository does not include the complete raw dataset. If you use external datasets or images, check and comply with their original licenses and attribution requirements.

Model files may be distributed separately when repository size limits make direct GitHub storage impractical.

## 🤝 Contributing

Suggestions, improvements, experiments, and bug reports are welcome. Open an issue or submit a pull request with a clear description of the change.

## 📄 License

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

## ⭐ Support the Project

If you find this project useful for learning, experimentation, or agricultural AI research, consider giving the repository a ⭐ and sharing it with others.

---

**Built as a university project exploring AI, computer vision, and agriculture. 🌾🤖**
