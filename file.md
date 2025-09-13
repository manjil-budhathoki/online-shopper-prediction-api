# Online Shopper Predictor API

<p align="center">
  <img src="assets/logo.png" alt="Project Logo" width="120" height="120"/>
</p>

<p align="center">
  Predict whether a website visitor will make a purchase based on their browsing behavior.  
  A full <b>MLOps end-to-end pipeline</b> project with automated data processing, model training, experiment tracking, and deployment.
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-orange" />
  <img src="https://img.shields.io/badge/build-passing-brightgreen" />
  <img src="https://img.shields.io/badge/license-MIT-blue" />
</p>

---

## 📖 About

This project demonstrates a **complete MLOps lifecycle** for predicting online shopper revenue.  
It automates the workflow from dataset ingestion → feature engineering → model training → experiment tracking → serving the model via a live API.

**Key Highlights:**
- Automated workflows using **Apache Airflow**
- Experiment tracking with **MLflow**
- REST API with **FastAPI**
- Containerized and deployable with **Docker**
- Cloud hosting on **Render**

---

## 🛠 Tech Stack

<p align="center">
  <img src="assets/python.png" alt="Python" height="45"/>
  <img src="assets/fastapi.png" alt="FastAPI" height="45"/>
  <img src="assets/docker.png" alt="Docker" height="45"/>
  <img src="assets/airflow.png" alt="Airflow" height="45"/>
  <img src="assets/mlflow.png" alt="MLflow" height="45"/>
  <img src="assets/scikit-learn.png" alt="Scikit-learn" height="45"/>
  <img src="assets/pandas.png" alt="Pandas" height="45"/>
  <img src="assets/render.png" alt="Render" height="45"/>
</p>

---

## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed:
- [Conda](https://docs.conda.io/en/latest/miniconda.html)  
- [Docker](https://docs.docker.com/get-docker/)

### Installation
```bash
# Clone the repository
git clone https://github.com/manjil-budhathoki/online-shopper-prediction-api.git
cd online-shopper-prediction-api

# Create and activate environment
conda create -n shopping_pipe python=3.9
conda activate shopping_pipe
pip install -r requirements.txt

# Run the API locally
uvicorn api.serve_model:app --reload
````

---

## 📌 Usage

Send a `POST` request to the `/predict` endpoint with session data.

**Example Request:**

```json
{
  "Month": "Nov",
  "VisitorType": "Returning_Visitor",
  "Administrative": 4,
  "Administrative_Duration": 85.5,
  "Informational": 2,
  "Informational_Duration": 50,
  "ProductRelated": 45,
  "ProductRelated_Duration": 1850.75,
  "BounceRates": 0.01,
  "ExitRates": 0.02,
  "PageValues": 25.4,
  "SpecialDay": 0.0
}
```

👉 Explore interactively: [Live API Docs](https://online-shopper-predictor.onrender.com/docs)

---

## 🗺 Roadmap

* ✅ Data pipelines with Airflow
* ✅ Model tracking with MLflow
* ✅ REST API with FastAPI
* ✅ Deployment on Render
* 🔲 CI for model quality checks
* 🔲 Drift monitoring
* 🔲 `docker-compose.yml` for simplified local setup

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE.txt) file for details.

---

## 📬 Contact

**Manjil Budhathoki** <br>
[LinkedIn](https://www.linkedin.com/in/manjil-budhathoki/) • [GitHub](https://github.com/manjil-budhathoki/online-shopper-prediction-api)

