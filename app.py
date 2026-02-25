import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# --------------------------
# 1️⃣ Load saved ANN and scaler
# --------------------------
classifier = load_model('models/my_ann_model.keras')
scaler = pickle.load(open('scaler/scaler.pkl', 'rb'))

# --------------------------
# 2️⃣ Streamlit App Title
# --------------------------
st.title("Bank Customer Churn Prediction")

st.write("Fill in the customer details below to predict if the customer will exit (churn).")

# --------------------------
# 3️⃣ Input fields for features
# --------------------------
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=40)
tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", min_value=0.0, value=60000.0)
num_products = st.number_input("Number of Products", min_value=1, max_value=5, value=2)
has_credit_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

# --------------------------
# 4️⃣ Encode categorical variables like in training
# --------------------------
# Geography: drop_first=True used in training → France is baseline
geography_germany = 1 if geography == "Germany" else 0
geography_spain = 1 if geography == "Spain" else 0

# Gender: Male=1, Female=0 (assuming drop_first=True)
gender_male = 1 if gender == "Male" else 0

# --------------------------
# 5️⃣ Prepare input array
# --------------------------
X_new = np.array([[credit_score, age, tenure, balance, num_products, 
                   has_credit_card, is_active_member, estimated_salary,
                   geography_germany, geography_spain, gender_male]])

# Scale numeric input using the same scaler (scaler was fitted on numeric columns)
# Numeric columns order: credit_score, age, tenure, balance, num_products,
# has_credit_card, is_active_member, estimated_salary
X_numeric = X_new[:, :8]
X_numeric_scaled = scaler.transform(X_numeric)

# The ANN was trained on the 8 scaled numeric features only.
# Provide only those scaled features to the classifier (shape (1, 8)).
X_new_scaled = X_numeric_scaled

# --------------------------
# 6️⃣ Predict button
# --------------------------
if st.button("Predict Churn"):
    y_pred = classifier.predict(X_new_scaled)
    y_pred = (y_pred >= 0.5)  # Convert probability to class label
    if y_pred[0]:
        st.error("Customer is likely to EXIT (Churn) ❌")
    else:
        st.success("Customer is likely to STAY ✅")
