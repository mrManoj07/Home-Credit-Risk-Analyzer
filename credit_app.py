
import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Credit Risk Analyzer",
    page_icon="🏦"
)

st.title("🏦 Credit Risk Analyzer")
st.subheader("Home Credit Default Risk Prediction")

@st.cache_resource
def load_model():
    return joblib.load("credit_risk_model.pkl")

@st.cache_data
def load_reference_customer():
    # Reference features ko CSV se load karenge
    return pd.read_csv("reference_customer.csv").iloc[[0]]

try:
    model = load_model()
    reference = load_reference_customer()
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"File loading error: {e}")
    st.stop()

st.divider()
st.write("### Customer Details")

income = st.number_input("Annual Income", min_value=0, value=360000)
credit = st.number_input("Credit Amount", min_value=0, value=500000)
annuity = st.number_input("Loan Annuity", min_value=0, value=25000)
goods_price = st.number_input("Goods Price", min_value=0, value=450000)
age = st.number_input("Age (years)", min_value=18, max_value=100, value=30)
employment = st.number_input("Employment Years", min_value=0, max_value=60, value=5)

st.warning(
    "Demo prediction: other features are copied from a reference "
    "customer. This is not a reliable real-world credit assessment."
)

if st.button("Predict Default Risk", type="primary"):
    customer = reference.copy()

    customer["AMT_INCOME_TOTAL"] = income
    customer["AMT_CREDIT"] = credit
    customer["AMT_ANNUITY"] = annuity
    customer["AMT_GOODS_PRICE"] = goods_price
    customer["DAYS_BIRTH"] = -(age * 365)
    customer["DAYS_EMPLOYED"] = -(employment * 365)

    probability = model.predict_proba(customer)[0, 1] * 100
    non_default = 100 - probability

    st.subheader("Prediction Result")
    st.metric("Estimated Default Probability", f"{probability:.2f}%")
    st.metric("Estimated Non-Default Probability", f"{non_default:.2f}%")

    if probability >= 50:
        st.error("Higher estimated default risk")
    else:
        st.success("Lower estimated default risk")
