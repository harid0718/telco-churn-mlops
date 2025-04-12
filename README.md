# Telco Customer Churn Prediction – End-to-End MLOps Pipeline

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-ready-success)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-containerized-blue)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-dashboard-orange)](https://streamlit.io/)
[![MLflow](https://img.shields.io/badge/MLflow-tracking-lightgrey)](https://mlflow.org/)

---

## 🚀 Project Overview

This project demonstrates a full end-to-end MLOps pipeline for predicting telecom customer churn. It includes data analysis, model training, versioning with MLflow, containerization using Docker, and a Streamlit dashboard to visualize churn predictions in real-time.

---

## 🧠 Problem Statement

Customer churn is a major issue in the telecom industry. This project helps identify which customers are most likely to churn, enabling companies to proactively improve retention.

---

## 🛠️ Tech Stack

| Category              | Tools / Libraries                        |
|-----------------------|------------------------------------------|
| Language              | Python                                   |
| Data Analysis         | Pandas, NumPy, Seaborn, Matplotlib        |
| Modeling              | Scikit-learn, XGBoost, Logistic Regression |
| Experiment Tracking   | MLflow                                   |
| Serving API           | FastAPI, Uvicorn                         |
| Containerization      | Docker                                   |
| Frontend Dashboard    | Streamlit                                |

---

## ✅ Highlights & Metrics

- **Accuracy**: 80.6%
- **ROC-AUC Score**: 0.85
- **Churn Precision**: 67%
- **FastAPI**: Real-time REST API with <100ms latency
- **Streamlit**: CSV upload, batch predictions, churn risk charts
- **Docker**: Containerized backend and frontend
- **MLflow**: Logged parameters, metrics, and models

---


## 🗂 Project Structure
```
telco-churn-mlops/
├── app.py                      # FastAPI backend
├── streamlit_app.py            # Streamlit dashboard
├── Dockerfile                  # Docker configuration
├── requirements.txt            # Dependencies
├── model/                      # Saved model (.pkl)
├── sample_churn_customers.csv  # Input sample for dashboard
├── README.md   # Project documentation
```

## ⚙️ How to Run

### 1. Clone and Set Up Environment

```bash
git clone https://github.com/harid0718/telco-churn-mlops.git
cd telco-churn-mlops
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt 

```

### 2. Run FastAPI
```bash
uvicorn app:app --reload --port 8000
```
Visit Swagger docs: http://localhost:8000/docs

### 3. Run Streamlit Dashboard
```bash
streamlit run streamlit_app.py
```
Visit dashboard: http://localhost:8501


## 🐳 Run with Docker
```bash
docker build -t telco-churn-api .
docker run -p 8000:8000 telco-churn-api
```

## 📈 Features
Batch predictions via CSV upload

Visualize churn probabilities

Highlight high-risk customers

End-to-end MLOps lifecycle


## 📌 Future Enhancements
GitHub Actions for CI/CD

Deploy on Azure or AWS ECS

Streamlit Cloud or Docker Compose hosting

Enhanced dashboard with filtering & export options


## 👨‍💻 Author
Hari Dave

Data Science | MLOps | Machine Learning Engineer

