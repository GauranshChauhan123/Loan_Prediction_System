from typing import Annotated

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# Load model once at startup
model = joblib.load("loan_prediction_model.pkl")

app = FastAPI(
    title="Loan Prediction API",
    description="Predict whether a loan application will be approved.",
    version="1.0.0"
)


class LoanRequest(BaseModel):
    Married: Annotated[
        str,
        Field(description="Marital Status", examples=["Yes"])
    ]

    Dependents: Annotated[
        str,
        Field(description="Number of Dependents", examples=["0"])
    ]

    Education: Annotated[
        str,
        Field(description="Education Level", examples=["Graduate"])
    ]

    Self_Employed: Annotated[
        str,
        Field(description="Self Employed", examples=["No"])
    ]

    LoanAmount: Annotated[
        float,
        Field(gt=0, description="Requested Loan Amount", examples=[150])
    ]

    Loan_Amount_Term: Annotated[
        float,
        Field(gt=0, description="Loan Term (Months)", examples=[360])
    ]

    Credit_History: Annotated[
        int,
        Field(description="Credit History (1 = Good, 0 = Bad)", examples=[1])
    ]

    Property_Area: Annotated[
        str,
        Field(description="Property Area", examples=["Urban"])
    ]

    total_income: Annotated[
        float,
        Field(gt=0, description="Total Monthly Income", examples=[7000])
    ]

    DTI_Ratio: Annotated[
        float,
        Field(ge=0, description="Debt-to-Income Ratio", examples=[0.25])
    ]


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Loan Prediction API is Running"
    }


@app.post("/predict", tags=["Prediction"])
def predict(data: LoanRequest):

    try:

        input_df = pd.DataFrame([data.model_dump()])

        prediction = int(model.predict(input_df)[0])


        return JSONResponse(
          status_code=200,
          content={
        "success": True,
        "prediction": prediction,
         }
)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )