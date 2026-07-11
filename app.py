import streamlit as st
import requests
import os


st.set_page_config(
    page_title="Loan Prediction System",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Prediction System")
st.write("Fill in the applicant details to predict loan approval.")


API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/predict"
)


with st.form("loan_form"):

    married = st.selectbox(
        "Marital Status",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["0", "1", "2", "3+"]
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=150.0
    )

    loan_term = st.number_input(
        "Loan Term (Months)",
        min_value=0.0,
        value=360.0
    )

    credit_history = st.selectbox(
        "Credit History",
        [1, 0]
    )

    property_area = st.selectbox(
        "Property Area",
        ["Urban", "Semiurban", "Rural"]
    )

    total_income = st.number_input(
        "Total Income",
        min_value=0.0,
        value=7000.0
    )

    dti_ratio = st.number_input(
        "DTI Ratio",
        min_value=0.0,
        value=0.25,
        format="%.2f"
    )

    submit = st.form_submit_button("Predict")


if submit:

    payload = {
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area,
        "total_income": total_income,
        "DTI_Ratio": dti_ratio
    }

    try:

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()

            if result["prediction"] == 1:
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Rejected")

            

        else:
            st.error(response.json())

    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to FastAPI server.")