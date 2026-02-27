# AI-ML-Exit-Exam
# 🌍 Intel Image Classification – AIML Exit Test

## 📌 Project Overview
This project focuses on classifying natural scene images such as buildings, forests, glaciers, mountains, sea, and street using deep learning techniques.

A Convolutional Neural Network (CNN) and Transfer Learning (MobileNetV2) were used to achieve good performance while reducing training time.

---

## 📊 Dataset
Intel Image Classification Dataset from Kaggle:
https://www.kaggle.com/datasets/puneet6060/intel-image-classification

- Images categorized into 6 classes:
  - buildings
  - forest
  - glacier
  - mountain
  - sea
  - street

---

## ⚙️ Technologies Used
- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit

---

## 🚀 Project Workflow

### 1. Data Preparation
- Loaded dataset from Kaggle
- Downsampled to 500 images per class (for faster training)
- Resized images to 150x150
- Split into training and validation sets

### 2. Data Augmentation
- Rotation
- Zoom
- Horizontal flipping

### 3. Model Training
- Built CNN model
- Used MobileNetV2 for transfer learning

### 4. Model Evaluation
- Classification report
- Confusion matrix

### 5. Error Analysis
- Visualized misclassified images

### 6. Model Improvement
- Improved accuracy using transfer learning

### 7. Deployment
- Built Streamlit web app for real-time prediction

---

## 📈 Results
- Achieved good accuracy with reduced dataset
- Transfer learning improved performance significantly
- Model can classify scene images in real time

---

## ▶️ How to Run the Project

### Step 1: Clone Repository
```bash
git clone <your-repo-link>
cd ai-ml-project
