# 🔥 Calorie Burned Predictor

A Streamlit web app that predicts the number of **calories burned** during a workout session using a **Multiple Linear Regression (MLR)** model.

[🔗 Live App](https://lnkd.in/dQVcW4hD) 

---

## 🧾 Overview

This project combines machine learning and health-tech to estimate calories burned based on user-specific physical and workout details. The app provides real-time predictions through a clean and responsive web interface.

It showcases an end-to-end ML pipeline — from data preprocessing and feature engineering to model training, deployment, and browser-based interaction using Streamlit.

---

## 🎯 Features

- ✅ Takes multiple workout and body profile inputs
- 📈 Calculates **BMI** internally for improved accuracy
- ⚡ Instant predictions using a lightweight MLR model
- 💻 Clean and responsive UI with **Streamlit**
- 🌐 Deployed and accessible online
- 🗃️ Cached model loading for optimized performance

---

## 📊 Input Parameters

| Feature            | Description                        |
|--------------------|------------------------------------|
| Gender             | Male = 0, Female = 1               |
| Age                | In years                           |
| Height             | In centimeters                     |
| Weight             | In kilograms                       |
| Duration           | Exercise duration in minutes       |
| Heart Rate         | During the workout                 |
| Body Temperature   | In degrees Celsius                 |
| BMI                | Auto-calculated from Height & Weight |

---

## 🧠 Machine Learning Model

- **Algorithm**: Multiple Linear Regression  
- **Library**: `scikit-learn`  
- **Training Data**: Fitness dataset with 700+ rows  
- **Preprocessing**: Label Encoding, BMI feature engineering  
- **Serialization**: `Joblib`

---

## 🛠️ Tech Stack

| Category         | Tools / Libraries                    |
|------------------|--------------------------------------|
| Language         | Python                               |
| Web Framework    | Streamlit                            |
| ML Library       | scikit-learn                         |
| Data Handling    | Pandas, NumPy                        |
| Visualization    | Matplotlib                           |
| Deployment Tools | Joblib (model download)       |

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.8 or later  
- pip

### 📦 Installation
```bash
git clone https://github.com/yourusername/calorie-burned-predictor.git
cd calorie-burned-predictor
pip install -r requirements.txt
