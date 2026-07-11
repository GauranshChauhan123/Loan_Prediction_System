# 🏦 Loan Prediction System

A production-ready Loan Prediction System built using **Machine Learning**, **FastAPI**, **Streamlit**, **Docker**, and **GitHub Actions**.

The application predicts whether a loan application is likely to be approved based on applicant information. The backend serves predictions through a REST API, while the frontend provides an interactive user interface.

---

## 🚀 Features

- Loan approval prediction using a trained Random Forest model
- FastAPI REST API backend
- Streamlit interactive frontend
- Scikit-learn Pipeline with ColumnTransformer
- Dockerized frontend and backend
- Docker Compose support
- GitHub Actions CI/CD
- Automatic Docker Hub image publishing

---

## 🛠 Tech Stack

- Python
- Scikit-learn
- Pandas
- FastAPI
- Streamlit
- Pydantic
- Docker
- Docker Compose
- GitHub Actions

---

## 📂 Project Structure

```text
loan_prediction_system/
│
├── app.py
├── main.py
├── loan_prediction_model.pkl
├── requirements.txt
├── Dockerfile.fastapi
├── Dockerfile.streamlit
├── docker-compose.yml
├── .github/
│   └── workflows/
├── .gitignore
├── .dockerignore
└── model.ipynb
```

---

## 📊 Features Used

- Married
- Dependents
- Education
- Self Employed
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area
- Total Income
- Debt-to-Income Ratio (DTI)

---

## ⚙️ Running Locally

### Clone the repository

```bash
git clone <your-repository-url>
cd loan_prediction_system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI

```bash
uvicorn main:app --reload
```

### Run Streamlit

```bash
streamlit run app.py
```

---

## 🐳 Run with Docker Compose

Build and start the application:

```bash
docker compose up --build
```

Frontend:

```
http://localhost:8501
```

Backend API Docs:

```
http://localhost:8000/docs
```

---

## 🔄 CI/CD

GitHub Actions automatically:

- Builds Docker images
- Pushes images to Docker Hub
- Keeps the latest version available after every push to the `main` branch

---

## 📌 Future Improvements

- Model explainability using SHAP
- Probability/confidence score
- User authentication
- Cloud deployment
- Monitoring and logging

---

## 👨‍💻 Author

**Gauransh Chauhan**

GitHub: https://github.com/GauranshChauhan123