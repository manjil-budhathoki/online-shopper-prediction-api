<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/manjil-budhathoki/online-shopper-prediction-api">
    <!-- IMPORTANT: Replace this with a real image link -->
    <img src="https://imgur.com/83COL6N" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">End-to-End MLOps Prediction API</h3>

  <p align="center">
    A complete MLOps project to predict online shopper revenue, featuring automated pipelines, experiment tracking, and a live API deployed to the cloud.
    <br />
    <a href="https://github.com/manjil-budhathoki/online-shopper-prediction-api"><strong>Explore the code »</strong></a>
    <br />
    <br />
    <!-- IMPORTANT: Replace this with your live Render URL -->
    <a href="https://online-shopper-predictor.onrender.com/docs">View Live Demo</a>
    ·
    <a href="https://github.com/manjil-budhathoki/online-shopper-prediction-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/manjil-budhathoki/online-shopper-prediction-api/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- IMPORTANT: Replace this with a real screenshot link and your Render URL -->
[![API Docs Screenshot](https://imgur.com/a/fyb9KHP)[product-screenshot]](https://online-shopper-predictor.onrender.com/docs)

This project is a comprehensive demonstration of a full MLOps lifecycle, built from the ground up. It automates the entire process of taking a raw dataset, processing it through a series of orchestrated pipelines, training a machine learning model, tracking the experiment, and deploying the final model as a live, containerized REST API.

The core challenge is to predict whether a user's session on an e-commerce website will result in a purchase, based on their browsing behavior.

Here's why this project is a solid MLOps showcase:
*   **Automation:** Every step from data ingestion to model training is automated and orchestrated with Apache Airflow.
*   **Reproducibility:** MLflow tracks every experiment, ensuring that any model can be reproduced and audited.
*   **Scalability & Portability:** The final API is containerized with Docker, making it easy to deploy and scale anywhere.
*   **CI/CD:** The project is deployed on Render and configured for automatic redeployment on every code change, demonstrating a modern Continuous Deployment workflow.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This project was built with a modern, industry-standard MLOps tech stack.

*   [![Python][Python.org]][Python-url]
*   [![FastAPI][FastAPI.com]][FastAPI-url]
*   [![Docker][Docker.com]][Docker-url]
*   [![Airflow][Airflow.com]][Airflow-url]
*   [![MLflow][MLflow.com]][MLflow-url]
*   [![Scikit-learn][Scikit-learn.com]][Scikit-learn-url]
*   [![Pandas][Pandas.com]][Pandas-url]
*   [![Render][Render.com]][Render-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You will need Conda (or Miniconda) and Docker installed on your machine.
*   **Conda (for environment management)**
    ```sh
    # Instructions to install can be found at https://docs.conda.io/en/latest/miniconda.html
    ```
*   **Docker (for containerization)**
    ```sh
    # Instructions to install can be found at https://docs.docker.com/get-docker/
    ```

### Installation

1.  Clone the repo
    ```sh
    git clone https://github.com/manjil-budhathoki/online-shopper-prediction-api.git
    cd online-shopper-prediction-api
    ```
2.  Create and activate the Conda environment for the pipeline scripts
    ```sh
    conda create -n shopping_pipe python=3.9
    conda activate shopping_pipe
    pip install -r requirements.txt
    ```
3.  Run local services (MariaDB, MLflow, Airflow) as needed. A `docker-compose.yml` is planned to simplify this step.
4.  Run the local API server
    ```sh
    uvicorn api.serve_model:app --reload
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The primary use of this project is to interact with the live prediction API. You can send a `POST` request to the `/predict` endpoint with a JSON body containing the shopper's session data.

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
}```
<!-- IMPORTANT: Replace this with your live Render URL -->
Visit the [Live API Documentation](https://[YOUR-RENDER-APP-URL-HERE]/docs) for an interactive way to test the endpoint.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Automated Data Ingestion & Validation Pipeline (Airflow)
- [x] Automated Feature Engineering Pipeline (Airflow)
- [x] Automated Model Training Pipeline (Airflow)
- [x] Experiment Tracking and Model Management (MLflow)
- [x] Model Serving via REST API (FastAPI)
- [x] API Containerization (Docker)
- [x] Cloud Deployment (Render)
- [x] Continuous Deployment on Git Push
- [ ] Implement CI with Automated Model Quality Tests (GitHub Actions)
- [ ] Add Data and Model Drift Monitoring
- [ ] Create a `docker-compose.yml` for simplified local setup

See the [open issues](https://github.com/manjil-budhathoki/online-shopper-prediction-api/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information. (You may need to create this file).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Manjil Budhathoki - [@manjil-budhathoki](https://www.linkedin.com/in/manjil-budhathoki/) - your.email@example.com

Project Link: [https://github.com/manjil-budhathoki/online-shopper-prediction-api](https://github.com/manjil-budhathoki/online-shopper-prediction-api)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/manjil-budhathoki/online-shopper-prediction-api.svg?style=for-the-badge
[contributors-url]: https://github.com/manjil-budhathoki/online-shopper-prediction-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/manjil-budhathoki/online-shopper-prediction-api.svg?style=for-the-badge
[forks-url]: https://github.com/manjil-budhathoki/online-shopper-prediction-api/network/members
[stars-shield]: https://img.shields.io/github/stars/manjil-budhathoki/online-shopper-prediction-api.svg?style=for-the-badge
[stars-url]: https://github.com/manjil-budhathoki/online-shopper-prediction-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/manjil-budhathoki/online-shopper-prediction-api.svg?style=for-the-badge
[issues-url]: https://github.com/manjil-budhathoki/online-shopper-prediction-api/issues
[license-shield]: https://img.shields.io/github/license/manjil-budhathoki/online-shopper-prediction-api.svg?style=for-the-badge
[license-url]: https://github.com/manjil-budhathoki/online-shopper-prediction-api/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/manjil-budhathoki/
[product-screenshot]: https://i.imgur.com/your-screenshot-image.png
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org
[FastAPI.com]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://docker.com
[Airflow.com]: https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white
[Airflow-url]: https://airflow.apache.org/
[MLflow.com]: https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow
[MLflow-url]: https://mlflow.org/
[Scikit-learn.com]: https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white
[Scikit-learn-url]: https://scikit-learn.org/
[Pandas.com]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas
[Pandas-url]: https://pandas.pydata.org/
[Render.com]: https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render
[Render-url]: https://render.com