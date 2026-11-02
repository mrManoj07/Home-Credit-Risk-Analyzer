# 🏦 Home Credit Default Risk Analyzer

A Machine Learning project that predicts the probability of customer loan default using financial and personal information. This project uses Random Forest and Logistic Regression models and provides an interactive web application built with Streamlit.

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA) and data visualization.
- 🧹 Data preprocessing and missing value handling.
- 🤖 Train Random Forest and Logistic Regression models.
- 📈 Compare model performance using ROC-AUC.
- 🎯 Threshold tuning for default prediction.
- 🔮 Predict loan default probabilities.
- 🧑‍💻 Interactive Streamlit web application.
- 💡 Display estimated default and non-default probabilities.

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## 🤖 Machine Learning Models

Two classification algorithms were implemented:

1. Random Forest Classifier
2. Logistic Regression

### 📈 Model Performance

| Model | ROC-AUC Score |
|---|---:|
| Random Forest | 0.733 |
| Logistic Regression | 0.749 |

**Best Performing Model:** Logistic Regression

## 🖥️ Application Interface

The Streamlit application allows users to enter customer details such as:

- Annual Income
- Credit Amount
- Loan Annuity
- Goods Price
- Age
- Employment Duration

It displays estimated loan default and non-default probabilities.

**Note:** The current UI uses reference-customer values for other required features. Predictions are for demonstration purposes and should not be used for real lending decisions.

## 📂 Project Structure

```text
Home-Credit-Risk-Analyzer/
│
├── Home_Credit_Default_Risk.ipynb
├── credit_app.py
├── credit_risk_model.pkl
├── reference_customer.csv
├── README.md
└── .gitignore
```

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/mrManoj07/Home-Credit-Risk-Analyzer.git
```

### 2. Open the project folder

```bash
cd Home-Credit-Risk-Analyzer
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

### 4. Run the Streamlit application

```bash
streamlit run credit_app.py
```

The application will open in your web browser.

## 📁 Dataset

This project uses the Home Credit Default Risk dataset from Kaggle.

The original dataset files are not included in this repository because of their large size.

## 🎯 Project Objective

The main objective is to estimate the probability of loan default using Machine Learning and help financial institutions assess customer credit risk.

## 👨‍💻 Author

**mrManoj07**

GitHub: [@mrManoj07](https://github.com/mrManoj07)

---

⭐ If you find this project interesting, feel free to explore the repository!
