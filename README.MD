# Insurance Claim Prediction App

A complete **Machine Learning project** to predict **health insurance claim amounts** based on customer demographic and health data.  
The project includes **data preprocessing, exploratory data analysis (EDA), model training**, and an interactive **Streamlit web application** for live predictions.

---

## Project Overview

This project aims to help insurance companies estimate claim amounts efficiently by leveraging machine learning.  
It analyzes key features such as **age, BMI, number of children, blood pressure, diabetic status, gender, and smoking habits** to predict the **expected insurance payment**.

---

## Key Features

- Data preprocessing and cleaning of `insurance.csv`
- Handling missing values and categorical encoding
- Exploratory Data Analysis (EDA) with visual insights
- Feature scaling with `StandardScaler`
- Model training using **XGBoost Regressor**
- Deployment-ready **Streamlit web app**
- Interactive user inputs and real-time prediction display

---

## Project Structure

```
insurance-claim-prediction/
│
├── app.py                          # Streamlit application
├── project.ipynb                   # Data analysis and model training notebook
├── insurance.csv                   # Dataset
├── scaler.pkl                      # Scaler used for numeric features
├── best_model.pkl                  # Trained ML model (XGBoost)
├── encoders/
│   ├── label_encoder_gender.pkl
│   ├── label_encoder_smoker.pkl
│   └── label_encoder_diabetic.pkl
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
```

---

## Installation and Setup

### Clone this repository
```bash
git clone https://github.com/<your-username>/insurance-claim-prediction.git
cd insurance-claim-prediction
```

### Install dependencies
Create a virtual environment and install required libraries:
```bash
pip install -r requirements.txt
```

**Example dependencies:**
```
streamlit
pandas
numpy
scikit-learn
xgboost
joblib
matplotlib
seaborn
```

### Run the Streamlit App
```bash
streamlit run app.py
```

Your app will open in the browser at `http://localhost:8501`.

---

## Dataset Description

| Feature | Description |
|----------|--------------|
| **age** | Age of the insured person |
| **gender** | Gender of the insured person |
| **bmi** | Body Mass Index |
| **children** | Number of children covered |
| **bloodpressure** | Average blood pressure reading |
| **diabetic** | Whether the person is diabetic (Yes/No) |
| **smoker** | Whether the person smokes (Yes/No) |
| **region** | Residential region |
| **claim** | Insurance claim amount (target variable) |

---

## Model Details

- **Algorithm:** XGBoost Regressor  
- **Scaling:** StandardScaler  
- **Encoders:** LabelEncoders for categorical variables  
- **Evaluation Metrics:** R² score, MAE, RMSE 
- **Saved Models:** `joblib` library for reuse in app.py

---

## Streamlit Web App

The app allows users to input personal and health data and get an **instant prediction** of their estimated insurance payment.

**Preview:**
- Input form (Age, BMI, Children, Blood Pressure, Gender, Diabetic, Smoker)
- "Predict Payment" button
- Output: Predicted Insurance Payment in USD 

---
