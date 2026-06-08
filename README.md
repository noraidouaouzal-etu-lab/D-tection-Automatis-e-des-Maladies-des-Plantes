# 🌿 Plant Disease Detection using Deep Learning

## 📌 Project Description
This project is a Deep Learning-based system for automatic detection of plant diseases from leaf images using a Convolutional Neural Network (EfficientNetB0).

The model classifies plant leaf images into 38 different disease classes using the PlantVillage dataset.

---

## 🚀 Objectives
- Automate plant disease detection using AI
- Help farmers detect diseases early
- Achieve high accuracy using transfer learning

---

## 🧠 Model Architecture
- Base Model: EfficientNetB0 (pretrained on ImageNet)
- Transfer Learning applied
- Fine-tuning of last layers
- Dense layers + Softmax (38 classes)

---

## 📊 Dataset
- PlantVillage dataset
- 38 classes of plant diseases
- ~87,000 images
- Preprocessing:
  - Resize images (224x224)
  - Normalization
  - Data augmentation

⚠️ Dataset not included in this repository due to size constraints.

---

## 📈 Results
- Accuracy: ~96.5%
- F1-score: ~0.95+
- AUC-ROC: 1.00

---

## 📁 Project Structure
