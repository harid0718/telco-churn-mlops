import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Telco Churn Predictor", layout="wide")

st.title("📊 Telco Customer Churn Dashboard")

st.markdown("""
Upload a CSV file to predict churn and view results visually.
""")

uploaded_file = st.file_uploader("Upload preprocessed CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    # Convert to list for FastAPI POST
    data_payload = {"data": df.values.tolist()}

    st.subheader("📨 Submitting to FastAPI for prediction...")

    try:
        response = requests.post("http://localhost:8000/predict", json=data_payload)
        if response.status_code == 200:
            predictions = response.json()
            df["Prediction"] = predictions["prediction"]
            df["Churn Probability"] = predictions["churn_probability"]

            st.success("✅ Predictions received!")

            st.subheader("🔍 Prediction Results")
            st.dataframe(df)

            st.subheader("📈 Churn Probability Distribution")
            st.bar_chart(df["Churn Probability"])

            st.subheader("🚨 High Risk Customers")
            st.dataframe(df[df["Prediction"] == 1])

        else:
            st.error(f"❌ FastAPI error: {response.status_code}")
    except Exception as e:
        st.error(f"🔥 Could not connect to FastAPI backend: {e}")
