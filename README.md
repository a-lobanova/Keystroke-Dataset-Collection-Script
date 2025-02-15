
This repository contains the code implementation for the paper titled "Machine-learning-based adaptive keyboard sound masking against acoustic channel attacks".


# **ML-acoustic-attack-defense**  

## **Abstract**  
Keyboard **acoustic side-channel attacks (ASCAs)** exploit sound leakage from typing to infer typed words with a certain level of accuracy. Researchers have improved these attacks using advanced **feature extraction** and **classification techniques**, including machine learning and deep learning. However, **defense mechanisms** have not kept pace with the increasing precision of these attacks.  

In this study, we introduce a **practical defense strategy** against keyboard acoustic attacks during password and text typing. Our approach generates **unique background sounds using Generative Adversarial Networks (GANs)** to mask keystroke sounds and prevent attackers from extracting usable information. The **background noise is dynamically generated by the user's device** to prevent attack models from isolating keypresses. We evaluate our method against multiple attack models and assess its usability over short and prolonged typing sessions. Our results demonstrate that this **adaptive masking strategy** does not interfere with user input efficiency while significantly reducing attack success rates.  

## **Project Overview**  
This repository contains the **data collection script, model training and comparison code, and train/test datasets** for ASCA research.  
⚠️ **Note:** The **GAN-based defense model** and **CoAtNet training scripts** are **not included** in this version and will be added later.  

## **How to Use This Repository**  

### **1. Install Dependencies**  
Ensure you have Python installed and install required packages:  
```sh
pip install numpy pandas scikit-learn matplotlib librosa torch torchvision sounddevice soundfile
```

### **2. Collect Keystroke Audio Data**  
Run the script to record keystroke audio and verify password input correctness:  
```sh
python collect_keystroke.py
```
Prepare a text file with passwords (one per line) and provide its path to the script.

### **3. Train Machine Learning Models**  
Train baseline machine learning models (**GaussianNB, Logistic Regression, KNN, Random Forest**):  
```sh
python model_comparison.ipynb
```

### **4. Compare Logistic Regression vs. CoAtNet**  
Evaluate and compare **Logistic Regression (best traditional model) with CoAtNet**:  
```sh
python model_comparison.ipynb
```

### **5. View Results**  
Accuracy reports and confusion matrix visualizations end of the file model_comparison.ipynb

---

## **Future Updates**  
✅ **GAN-based sound masking model** (Defense strategy)  
✅ **CoAtNet training & evaluation**  
