# bank-churn-prediction-ann

# 🚀 Bank Churn Prediction using ANN

## Project Overview
This project predicts whether a bank customer will **exit (churn)** or **stay** using an **Artificial Neural Network (ANN)**.  
The model is deployed using **Streamlit** for interactive predictions.

---

## Problem Statement
Customer churn is a major problem in banking.  
This project predicts:

- `0` → Customer stays  
- `1` → Customer exits  

---

## Dataset Features

The model uses the following features:

- **Credit Score** – Financial stability of customer  
- **Geography** – Country (France, Germany, Spain)  
- **Gender** – Male/Female  
- **Age** – Age of customer  
- **Tenure** – Number of years with the bank  
- **Balance** – Bank account balance  
- **NumOfProducts** – Number of bank products used  
- **HasCrCard** – Has credit card (1 = Yes, 0 = No)  
- **IsActiveMember** – Customer active status (1 = Active, 0 = Not active)  
- **EstimatedSalary** – Estimated annual salary  

---

## Model Information

- **Type:** Artificial Neural Network (ANN)  
- **Output Layer:** Sigmoid activation  
- **Loss Function:** Binary Crossentropy  
- **Optimizer:** Adam  
- **Feature Scaling:** StandardScaler  

---

## Project Structure

BankChurnPrediction/
│
├── app.py # Streamlit app
├── models/
│ └── my_ann_model.keras # Saved ANN model
├── scaler/
│ └── scaler.pkl # Scaler used during training
├── requirements.txt # Python dependencies
└── README.md


---

## How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/MungaiHub/bank-churn-prediction-ann.git
cd bank-churn-prediction-ann
python3 -m venv venv
pip install -r requirements.txt
streamlit run app.py

Goal

To help banks identify customers likely to churn and take proactive retention measures.

Author

Amos Mungai
