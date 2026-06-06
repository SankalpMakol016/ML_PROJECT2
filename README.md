![CI](https://github.com/SankalpMakol016/ML_PROJECT2/actions/workflows/main.yaml/badge.svg)
# 🎓 Student Performance Prediction - End-to-End MLOps Project

## 📌 Project Overview

This project predicts a student's Mathematics score based on demographic and academic factors such as gender, race/ethnicity, parental education level, lunch type, test preparation course, reading score, and writing score.

The project was built following an end-to-end MLOps workflow, covering data ingestion, preprocessing, model training, model evaluation, deployment, containerization, CI/CD automation, and cloud deployment on AWS.

---

## 🚀 Features

- Data Ingestion Pipeline
- Data Transformation Pipeline
- Model Training Pipeline
- Prediction Pipeline
- Flask Web Application
- Docker Containerization
- CI/CD Automation using GitHub Actions
- AWS ECR Integration
- AWS EC2 Deployment
- Automated Deployment Pipeline

---

## 🛠️ Tech Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn

### Backend

- Flask

### DevOps & MLOps

- Docker
- GitHub Actions
- AWS EC2
- AWS ECR

### Version Control

- Git
- GitHub

---

## 📊 Model Performance

| Model | Performance |
|---------|------------|
| Linear Regression | ~88% R² Score |

Linear Regression was selected as the final production model after evaluating multiple machine learning algorithms.

---

## 🏗️ Project Architecture

```text
Dataset
   │
   ▼
Data Ingestion
   │
   ▼
Data Transformation
   │
   ▼
Model Training
   │
   ▼
Model Selection
   │
   ▼
Prediction Pipeline
   │
   ▼
Flask Application
   │
   ▼
Docker Container
   │
   ▼
Amazon ECR
   │
   ▼
Amazon EC2
   │
   ▼
End Users
```
---

## 📸 Application Screenshots

### Application Interface

![Application UI](screenshots/application-ui1.png)

### Prediction Output

![Prediction Output](screenshots/application-ui2.png)

### Docker Container Running

![Docker Container](screenshots/docker-container.png)

### GitHub Actions Deployment Pipeline

![GitHub Actions](screenshots/github-actions-success.png)

### AWS EC2 Deployment

![AWS EC2](screenshots/ec2-instance.png)

### AWS ECR Repository

![AWS ECR](screenshots/ecr-repository.png)

---

## 🔄 CI/CD Pipeline

Implemented a complete CI/CD pipeline using GitHub Actions.

Workflow:

1. Push code to GitHub
2. Build Docker Image
3. Push Image to Amazon ECR
4. Connect to AWS EC2
5. Pull Latest Docker Image
6. Restart Container
7. Deploy Updated Application

---

## ☁️ AWS Deployment

The application is deployed using:

- Amazon EC2
- Amazon ECR
- Docker
- GitHub Actions

Deployment is fully automated through CI/CD workflows.

---

## 📂 Project Structure

```text
src/
├── components/
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   └── model_trainer.py
│
├── pipeline/
│   ├── train_pipeline.py
│   └── predict_pipeline.py
│
├── exception.py
├── logger.py
└── utils.py

templates/
├── home.html
└── index.html

artifacts/
├── model.pkl
└── preprocessor.pkl
```

## ▶️ Run Locally

```bash
git clone <repo-url>

cd ML_PROJECT2

pip install -r requirements.txt

python app.py
```

---

## 🎯 Future Improvements

- Model Monitoring
- MLflow Integration
- Kubernetes Deployment
- Automated Retraining Pipeline
- Cloud Monitoring and Logging

---

## 👨‍💻 Author

Sankalp Makol

Machine Learning | MLOps | Software Development