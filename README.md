# 🌿 CropGuard – Plant Disease Detection System

CropGuard is a deep learning-based plant disease detection system designed to address **class imbalance** in agricultural datasets. It combines **GAN-based data augmentation** with a **ResNet-18 CNN classifier** to improve performance, especially for underrepresented plant disease classes.

---

## 🚀 Features

- 🌱 Detects plant diseases from leaf images  
- 🧠 Uses GANs to generate synthetic data for minority classes  
- 🔍 Fine-tuned ResNet-18 CNN for accurate classification  
- ⚖️ Handles class imbalance effectively  
- 🌐 Flask-based web app for real-time predictions  
- 📊 High performance (Macro F1-score > 0.97)  

---

## 🏗️ Project Architecture

1. **Dataset**  
   - PlantVillage dataset  
   - 38 classes (diseases + healthy) across 14 crops  

2. **Baseline Model**  
   - CNN trained on imbalanced dataset  

3. **GAN Augmentation**  
   - Synthetic images generated for minority classes  

4. **Improved Model**  
   - ResNet-18 trained on augmented dataset  

5. **Deployment**  
   - Flask web app for real-time classification  

---

## 🧠 Technologies Used

- Python  
- PyTorch / TensorFlow  
- GAN (Generative Adversarial Networks)  
- CNN (ResNet-18)  
- Flask  
- NumPy, OpenCV, Matplotlib  

---
