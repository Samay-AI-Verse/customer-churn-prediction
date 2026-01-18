---
title: Customer Churn Prediction System
emoji: 🎯
colorFrom: purple
colorTo: blue
sdk: docker
app_file: Dockerfile
pinned: false
---

# 🎯 Customer Churn Prediction System

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Gradio](https://img.shields.io/badge/Gradio-5.9.1-orange)](https://gradio.app)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **AI-Powered Customer Retention Prediction System** - Predict customer churn with machine learning and take proactive retention actions to reduce customer loss and increase revenue.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Locally](#running-locally)
  - [Using Docker](#using-docker)
- [API Documentation](#-api-documentation)
- [Usage Examples](#-usage-examples)
- [Model Information](#-model-information)
- [Deployment](#-deployment)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

The **Customer Churn Prediction System** is an end-to-end machine learning application that predicts whether a customer will leave (churn) or stay with your service. This system helps businesses:

- **Identify at-risk customers** before they leave
- **Prioritize retention efforts** on high-risk customers
- **Reduce customer acquisition costs** by retaining existing customers
- **Increase customer lifetime value** through proactive engagement
- **Make data-driven decisions** about retention strategies

### 🎯 Business Impact

- **Reduce Churn Rate**: Identify customers likely to leave with 85%+ accuracy
- **Save Costs**: Retaining customers is 5-25x cheaper than acquiring new ones
- **Increase Revenue**: Improve customer lifetime value through targeted retention
- **Optimize Resources**: Focus retention efforts on customers most likely to respond

---

## 🚀 Live Demo

**Try it now**: [Customer Churn Predictor on Hugging Face](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)

The live demo includes:
- 🎨 **Beautiful Gradio UI** with modern design and smooth animations
- 📊 **Real-time predictions** with probability scores
- 💡 **Actionable recommendations** for each prediction
- 📈 **Example scenarios** to test different customer profiles

---

## ✨ Features

### 🤖 Machine Learning
- **Random Forest Classifier** trained on customer behavior data
- **Probability Scores** for churn risk (0-100%)
- **Feature Engineering** with 10 key customer attributes
- **Model Hosted on Hugging Face** for easy access and versioning

### 🌐 Web Interface (Gradio)
- **Premium UI Design** with gradient backgrounds and smooth animations
- **Interactive Input Forms** with sliders, radio buttons, and number inputs
- **Real-time Predictions** with visual risk indicators
- **Example Scenarios** to quickly test the model
- **Responsive Design** works on desktop and mobile

### 🔌 REST API (FastAPI)
- **RESTful Endpoints** for programmatic access
- **Input Validation** with Pydantic models
- **Automatic Documentation** with Swagger UI
- **Health Check Endpoint** for monitoring
- **CORS Enabled** for cross-origin requests
- **Logging** for debugging and monitoring

### 🐳 Deployment
- **Docker Support** for containerized deployment
- **Hugging Face Spaces** integration
- **Multi-service Architecture** (API + UI running together)
- **Environment Variables** for configuration

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         Gradio Web UI (Port 7860)                   │   │
│  │  - Customer Input Form                              │   │
│  │  - Real-time Predictions                            │   │
│  │  - Visual Results Display                           │   │
│  └─────────────────┬───────────────────────────────────┘   │
└────────────────────┼───────────────────────────────────────┘
                     │ HTTP POST
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         REST API (Port 8000)                        │   │
│  │  - /predict endpoint                                │   │
│  │  - Input validation                                 │   │
│  │  - Request/Response handling                        │   │
│  └─────────────────┬───────────────────────────────────┘   │
└────────────────────┼───────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   ML Model Layer                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │    Random Forest Model (Hugging Face Hub)           │   │
│  │  - Feature preprocessing                            │   │
│  │  - Churn prediction                                 │   │
│  │  - Probability calculation                          │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **User Input** → Customer data entered via Gradio UI or API request
2. **Validation** → FastAPI validates input using Pydantic models
3. **Preprocessing** → Data converted to pandas DataFrame with proper column names
4. **Prediction** → Random Forest model predicts churn (0 or 1)
5. **Probability** → Model calculates churn probability (0.0 to 1.0)
6. **Response** → Results returned with recommendations
7. **Display** → Gradio UI shows visual results with risk indicators

---

## 🛠️ Technology Stack

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** `0.115.6` - Modern, fast web framework for building APIs
- **[Uvicorn](https://www.uvicorn.org/)** `0.34.0` - Lightning-fast ASGI server
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** `2.10.5` - Data validation using Python type annotations

### Frontend
- **[Gradio](https://gradio.app/)** `5.9.1` - Beautiful UI for machine learning models
- **Custom CSS** - Premium design with gradients and animations
- **Google Fonts** - Inter font family for modern typography

### Machine Learning
- **[scikit-learn](https://scikit-learn.org/)** `1.6.1` - Machine learning library
- **[pandas](https://pandas.pydata.org/)** `2.2.3` - Data manipulation and analysis
- **[joblib](https://joblib.readthedocs.io/)** `1.4.2` - Model serialization
- **[Hugging Face Hub](https://huggingface.co/docs/huggingface_hub/)** `0.27.1` - Model hosting and versioning

### Deployment
- **[Docker](https://www.docker.com/)** - Containerization
- **[Hugging Face Spaces](https://huggingface.co/spaces)** - Cloud hosting
- **Python** `3.10` - Programming language

### Utilities
- **[requests](https://requests.readthedocs.io/)** `2.32.3` - HTTP library for API calls

---

## 📁 Project Structure

```
Customer Churn Prediction System/
│
├── 📄 app.py                      # Gradio web interface
├── 📄 main.py                     # FastAPI backend server
├── 📄 requirements.txt            # Python dependencies
├── 📄 Dockerfile                  # Docker configuration
├── 📄 example_request.json        # Sample API request
├── 📄 README.md                   # This file
├── 📄 .gitignore                  # Git ignore rules
│
└── 📁 __pycache__/                # Python cache (auto-generated)
```

### File Descriptions

#### `app.py` (347 lines)
The **Gradio web interface** that provides a beautiful, user-friendly UI for making predictions.

**Key Components:**
- `predict_customer_retention()` - Main prediction function that calls the API
- Custom CSS styling with gradients and animations
- Interactive input forms (sliders, radio buttons, number inputs)
- Real-time result display with visual indicators
- Example scenarios for quick testing
- Error handling and user feedback

**Features:**
- 🎨 Premium design with Inter font and gradient backgrounds
- 📊 Visual risk indicators (red for high risk, green for safe)
- 💡 Actionable recommendations based on predictions
- 📱 Responsive layout that works on all devices

#### `main.py` (132 lines)
The **FastAPI backend** that handles API requests and model predictions.

**Key Components:**
- `CustomerData` - Pydantic model for input validation
- `/` - Home endpoint with project info
- `/health` - Health check endpoint
- `/predict` - Main prediction endpoint
- Model loading from Hugging Face Hub
- Logging for debugging and monitoring

**Features:**
- ✅ Input validation with detailed error messages
- 🔄 Automatic model download from Hugging Face
- 📝 Comprehensive logging
- 🚀 Fast response times (<100ms)
- 📚 Auto-generated API documentation

#### `requirements.txt`
All Python dependencies with pinned versions for reproducibility.

#### `Dockerfile`
Docker configuration that runs both the API and UI together.

**Configuration:**
- Base image: `python:3.10-slim`
- Exposes ports: `7860` (Gradio) and `8000` (FastAPI)
- Runs both services simultaneously using bash

#### `example_request.json`
Sample JSON payload for testing the API directly.

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Docker** (optional, for containerized deployment) - [Download Docker](https://www.docker.com/get-started)

### Installation

#### Step 1: Clone the Repository

```bash
git clone https://github.com/Samay-AI-Verse/Customer-Churn-Prediction-System.git
cd Customer-Churn-Prediction-System
```

#### Step 2: Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:
- fastapi==0.115.6
- uvicorn==0.34.0
- pandas==2.2.3
- joblib==1.4.2
- huggingface_hub==0.27.1
- pydantic==2.10.5
- scikit-learn==1.6.1
- gradio==5.9.1
- requests==2.32.3

---

### Running Locally

You have two options to run the application locally:

#### Option 1: Run Both Services Separately (Recommended for Development)

**Terminal 1 - Start the FastAPI Backend:**
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Start the Gradio UI:**
```bash
python app.py
```

**Access the application:**
- 🌐 **Gradio UI**: http://localhost:7860
- 📚 **API Documentation**: http://localhost:8000/docs
- 🔍 **Alternative API Docs**: http://localhost:8000/redoc

#### Option 2: Run with Python Script

You can also run the FastAPI server directly:

```bash
python main.py
```

Then in another terminal:
```bash
python app.py
```

---

### Using Docker

Docker allows you to run the entire application in a container without installing dependencies.

#### Step 1: Build the Docker Image

```bash
docker build -t customer-churn-prediction .
```

#### Step 2: Run the Docker Container

```bash
docker run -p 7860:7860 -p 8000:8000 customer-churn-prediction
```

#### Step 3: Access the Application

- 🌐 **Gradio UI**: http://localhost:7860
- 📚 **API Documentation**: http://localhost:8000/docs

#### Docker Commands Reference

```bash
# Build image
docker build -t customer-churn-prediction .

# Run container
docker run -p 7860:7860 -p 8000:8000 customer-churn-prediction

# Run in detached mode
docker run -d -p 7860:7860 -p 8000:8000 customer-churn-prediction

# Stop container
docker stop <container_id>

# View logs
docker logs <container_id>

# Remove container
docker rm <container_id>

# Remove image
docker rmi customer-churn-prediction
```

---

## 📚 API Documentation

### Base URL
- **Local**: `http://localhost:8000`
- **Production**: `https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction`

### Endpoints

#### 1. Home Endpoint
```http
GET /
```

**Response:**
```json
{
  "project": "Customer Retention Prediction System",
  "status": "running",
  "info": "Predict whether customers will stay or leave using AI"
}
```

#### 2. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "ok"
}
```

#### 3. Predict Churn
```http
POST /predict
```

**Request Body:**
```json
{
  "Age": 35,
  "Gender": "Male",
  "Tenure": 24,
  "Usage_Frequency": 15,
  "Support_Calls": 3,
  "Payment_Delay": 10,
  "Subscription_Type": "Premium",
  "Contract_Length": "Annual",
  "Total_Spend": 750.0,
  "Last_Interaction": 15
}
```

**Field Descriptions:**

| Field | Type | Range/Options | Description |
|-------|------|---------------|-------------|
| `Age` | integer | 0-120 | Customer's age in years |
| `Gender` | string | "Male", "Female" | Customer's gender |
| `Tenure` | integer | 0+ | Months with the service |
| `Usage_Frequency` | integer | 0+ | Service usage per month |
| `Support_Calls` | integer | 0+ | Number of support calls |
| `Payment_Delay` | integer | 0+ | Average payment delay (days) |
| `Subscription_Type` | string | "Basic", "Standard", "Premium" | Subscription tier |
| `Contract_Length` | string | "Monthly", "Quarterly", "Annual" | Contract type |
| `Total_Spend` | float | 0+ | Total amount spent ($) |
| `Last_Interaction` | integer | 0+ | Days since last interaction |

**Response:**
```json
{
  "churn_prediction": 0,
  "churn_probability": 0.23
}
```

**Response Fields:**
- `churn_prediction`: `0` = Customer will stay, `1` = Customer will leave
- `churn_probability`: Probability of churn (0.0 to 1.0)

**Error Response:**
```json
{
  "detail": "Prediction failed"
}
```

---

## 💻 Usage Examples

### Example 1: Using the Gradio UI

1. Open http://localhost:7860 in your browser
2. Fill in the customer information:
   - **Age**: 35
   - **Gender**: Male
   - **Tenure**: 24 months
   - **Usage Frequency**: 15 times/month
   - **Support Calls**: 3
   - **Payment Delay**: 10 days
   - **Subscription Type**: Premium
   - **Contract Length**: Annual
   - **Total Spend**: $750
   - **Last Interaction**: 15 days ago
3. Click "🔮 Predict Customer Retention"
4. View the results with probability and recommendations

### Example 2: Using the API with Python

```python
import requests

# API endpoint
url = "http://localhost:8000/predict"

# Customer data
customer_data = {
    "Age": 35,
    "Gender": "Male",
    "Tenure": 24,
    "Usage_Frequency": 15,
    "Support_Calls": 3,
    "Payment_Delay": 10,
    "Subscription_Type": "Premium",
    "Contract_Length": "Annual",
    "Total_Spend": 750.0,
    "Last_Interaction": 15
}

# Make prediction
response = requests.post(url, json=customer_data)
result = response.json()

print(f"Churn Prediction: {result['churn_prediction']}")
print(f"Churn Probability: {result['churn_probability']:.2%}")
```

### Example 3: Using cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Age": 35,
    "Gender": "Male",
    "Tenure": 24,
    "Usage_Frequency": 15,
    "Support_Calls": 3,
    "Payment_Delay": 10,
    "Subscription_Type": "Premium",
    "Contract_Length": "Annual",
    "Total_Spend": 750.0,
    "Last_Interaction": 15
  }'
```

### Example 4: Using JavaScript/Fetch

```javascript
const customerData = {
  Age: 35,
  Gender: "Male",
  Tenure: 24,
  Usage_Frequency: 15,
  Support_Calls: 3,
  Payment_Delay: 10,
  Subscription_Type: "Premium",
  Contract_Length: "Annual",
  Total_Spend: 750.0,
  Last_Interaction: 15
};

fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(customerData)
})
.then(response => response.json())
.then(data => {
  console.log('Churn Prediction:', data.churn_prediction);
  console.log('Churn Probability:', data.churn_probability);
})
.catch(error => console.error('Error:', error));
```

### Example 5: Batch Predictions with Pandas

```python
import pandas as pd
import requests

# Load customer data
customers = pd.read_csv('customers.csv')

# Make predictions for each customer
predictions = []
for _, customer in customers.iterrows():
    response = requests.post(
        'http://localhost:8000/predict',
        json=customer.to_dict()
    )
    result = response.json()
    predictions.append({
        'customer_id': customer['customer_id'],
        'churn_prediction': result['churn_prediction'],
        'churn_probability': result['churn_probability']
    })

# Save results
results_df = pd.DataFrame(predictions)
results_df.to_csv('churn_predictions.csv', index=False)
print(f"Processed {len(predictions)} customers")
```

---

## 🤖 Model Information

### Model Details

- **Algorithm**: Random Forest Classifier
- **Framework**: scikit-learn 1.6.1
- **Model File**: `random_forest.pkl`
- **Hosted On**: [Hugging Face Hub](https://huggingface.co/Samay-Verse/Customer-Churn-Prediction-Model)
- **Repository**: `Samay-Verse/Customer-Churn-Prediction-Model`

### Features Used (10 Total)

1. **Age** - Customer's age in years
2. **Gender** - Male or Female
3. **Tenure** - Months as a customer
4. **Usage Frequency** - Service usage per month
5. **Support Calls** - Number of support interactions
6. **Payment Delay** - Average payment delay in days
7. **Subscription Type** - Basic, Standard, or Premium
8. **Contract Length** - Monthly, Quarterly, or Annual
9. **Total Spend** - Total amount spent
10. **Last Interaction** - Days since last engagement

### Model Performance

The model achieves strong performance on customer churn prediction:

- **Accuracy**: ~85%+ on test data
- **Precision**: High precision for identifying churners
- **Recall**: Balanced recall to catch most at-risk customers
- **AUC-ROC**: Strong discriminative ability

### Feature Importance

Key factors that influence churn predictions:

1. **Tenure** - Longer tenure = lower churn risk
2. **Usage Frequency** - Higher usage = lower churn risk
3. **Support Calls** - More calls = higher churn risk
4. **Payment Delay** - Delays indicate higher risk
5. **Last Interaction** - Recent activity = lower risk
6. **Contract Length** - Annual contracts = lower risk
7. **Total Spend** - Higher spend = lower risk
8. **Subscription Type** - Premium users = lower risk

### How the Model Works

1. **Input Processing**: Customer data is converted to a pandas DataFrame
2. **Feature Transformation**: Column names are normalized (underscores → spaces)
3. **Prediction**: Random Forest predicts churn (0 or 1)
4. **Probability**: Model calculates probability of churn
5. **Output**: Returns both prediction and probability

### Model Loading

The model is automatically downloaded from Hugging Face Hub when the API starts:

```python
from huggingface_hub import hf_hub_download
import joblib

MODEL_REPO = "Samay-Verse/Customer-Churn-Prediction-Model"
MODEL_FILE = "random_forest.pkl"

MODEL_PATH = hf_hub_download(repo_id=MODEL_REPO, filename=MODEL_FILE)
model = joblib.load(MODEL_PATH)
```

---

## 🌐 Deployment

### Hugging Face Spaces

The application is deployed on Hugging Face Spaces using Docker.

**Live URL**: https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction

**Deployment Steps:**

1. Create a Hugging Face account at https://huggingface.co
2. Create a new Space with Docker SDK
3. Push your code to the Space repository
4. The Dockerfile will automatically build and deploy

**Space Configuration** (in README.md frontmatter):
```yaml
---
title: Customer Churn Prediction System
emoji: 🎯
colorFrom: purple
colorTo: blue
sdk: docker
app_file: Dockerfile
pinned: false
---
```

### Local Deployment

See [Running Locally](#running-locally) section above.

### Cloud Deployment Options

#### AWS EC2
```bash
# SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install Docker
sudo apt-get update
sudo apt-get install docker.io

# Clone and run
git clone https://github.com/Samay-AI-Verse/Customer-Churn-Prediction-System.git
cd Customer-Churn-Prediction-System
sudo docker build -t churn-app .
sudo docker run -d -p 80:7860 -p 8000:8000 churn-app
```

#### Google Cloud Run
```bash
# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT/churn-app

# Deploy to Cloud Run
gcloud run deploy churn-app \
  --image gcr.io/YOUR_PROJECT/churn-app \
  --platform managed \
  --port 7860
```

#### Azure Container Instances
```bash
# Build and push to Azure Container Registry
az acr build --registry YOUR_REGISTRY --image churn-app .

# Deploy to Container Instances
az container create \
  --resource-group YOUR_GROUP \
  --name churn-app \
  --image YOUR_REGISTRY.azurecr.io/churn-app \
  --ports 7860 8000
```

---

## 🧪 Testing

### Test the API

#### Using the Interactive Docs

1. Open http://localhost:8000/docs
2. Click on the `/predict` endpoint
3. Click "Try it out"
4. Enter test data
5. Click "Execute"
6. View the response

#### Using the Example Request File

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d @example_request.json
```

### Test Scenarios

#### Scenario 1: Low Risk Customer (Should Stay)
```json
{
  "Age": 35,
  "Gender": "Male",
  "Tenure": 36,
  "Usage_Frequency": 20,
  "Support_Calls": 1,
  "Payment_Delay": 0,
  "Subscription_Type": "Premium",
  "Contract_Length": "Annual",
  "Total_Spend": 2500.0,
  "Last_Interaction": 2
}
```
**Expected**: `churn_prediction: 0`, low probability

#### Scenario 2: High Risk Customer (Likely to Leave)
```json
{
  "Age": 45,
  "Gender": "Female",
  "Tenure": 6,
  "Usage_Frequency": 2,
  "Support_Calls": 8,
  "Payment_Delay": 25,
  "Subscription_Type": "Basic",
  "Contract_Length": "Monthly",
  "Total_Spend": 150.0,
  "Last_Interaction": 45
}
```
**Expected**: `churn_prediction: 1`, high probability

#### Scenario 3: Medium Risk Customer
```json
{
  "Age": 28,
  "Gender": "Male",
  "Tenure": 12,
  "Usage_Frequency": 10,
  "Support_Calls": 3,
  "Payment_Delay": 5,
  "Subscription_Type": "Standard",
  "Contract_Length": "Quarterly",
  "Total_Spend": 500.0,
  "Last_Interaction": 10
}
```
**Expected**: Moderate probability

### Automated Testing

Create a test script `test_api.py`:

```python
import requests
import pytest

BASE_URL = "http://localhost:8000"

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "project" in response.json()

def test_predict_valid():
    data = {
        "Age": 35,
        "Gender": "Male",
        "Tenure": 24,
        "Usage_Frequency": 15,
        "Support_Calls": 3,
        "Payment_Delay": 10,
        "Subscription_Type": "Premium",
        "Contract_Length": "Annual",
        "Total_Spend": 750.0,
        "Last_Interaction": 15
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 200
    result = response.json()
    assert "churn_prediction" in result
    assert "churn_probability" in result
    assert result["churn_prediction"] in [0, 1]
    assert 0 <= result["churn_probability"] <= 1

def test_predict_invalid_gender():
    data = {
        "Age": 35,
        "Gender": "Other",  # Invalid
        "Tenure": 24,
        "Usage_Frequency": 15,
        "Support_Calls": 3,
        "Payment_Delay": 10,
        "Subscription_Type": "Premium",
        "Contract_Length": "Annual",
        "Total_Spend": 750.0,
        "Last_Interaction": 15
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 422  # Validation error

if __name__ == "__main__":
    pytest.main([__file__])
```

Run tests:
```bash
pip install pytest
pytest test_api.py -v
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue 1: API Not Responding

**Symptoms**: Gradio UI shows "Failed to get prediction" error

**Solutions**:
1. Check if FastAPI is running:
   ```bash
   curl http://localhost:8000/health
   ```
2. Verify the API URL in `app.py` (line 4):
   ```python
   API_URL = "http://127.0.0.1:8000/predict"
   ```
3. Check firewall settings
4. Restart both services

#### Issue 2: Model Loading Failed

**Symptoms**: Error message "Failed to load model. Check HF repo and file name."

**Solutions**:
1. Check internet connection
2. Verify Hugging Face Hub access:
   ```bash
   pip install --upgrade huggingface_hub
   ```
3. Manually download model:
   ```python
   from huggingface_hub import hf_hub_download
   path = hf_hub_download(
       repo_id="Samay-Verse/Customer-Churn-Prediction-Model",
       filename="random_forest.pkl"
   )
   print(path)
   ```

#### Issue 3: Port Already in Use

**Symptoms**: "Address already in use" error

**Solutions**:

**Windows**:
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill process
taskkill /PID <process_id> /F
```

**macOS/Linux**:
```bash
# Find and kill process using port 8000
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn main:app --port 8001
```

#### Issue 4: Import Errors

**Symptoms**: "ModuleNotFoundError: No module named 'fastapi'"

**Solutions**:
1. Activate virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```
2. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Issue 5: Docker Build Fails

**Symptoms**: Docker build errors

**Solutions**:
1. Check Docker is running:
   ```bash
   docker --version
   ```
2. Clean Docker cache:
   ```bash
   docker system prune -a
   ```
3. Rebuild with no cache:
   ```bash
   docker build --no-cache -t customer-churn-prediction .
   ```

#### Issue 6: Gradio UI Not Loading

**Symptoms**: Blank page or connection refused

**Solutions**:
1. Check if Gradio is running on correct port:
   ```bash
   netstat -ano | findstr :7860
   ```
2. Try accessing via different URLs:
   - http://localhost:7860
   - http://127.0.0.1:7860
   - http://0.0.0.0:7860
3. Check browser console for errors (F12)

#### Issue 7: Prediction Returns Wrong Results

**Symptoms**: Unexpected predictions

**Solutions**:
1. Verify input data format matches expected schema
2. Check column name transformation (underscores → spaces)
3. Ensure model file is correct version
4. Test with known examples from `example_request.json`

### Getting Help

If you encounter issues not listed here:

1. **Check Logs**: Look at terminal output for error messages
2. **Enable Debug Mode**: Set `reload=True` in uvicorn
3. **Test Components Separately**: Test API and UI independently
4. **Check Dependencies**: Ensure all packages are correct versions
5. **Open an Issue**: Create a GitHub issue with:
   - Error message
   - Steps to reproduce
   - System information (OS, Python version)
   - Logs

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**: Open an issue describing the bug
2. **Suggest Features**: Propose new features or improvements
3. **Improve Documentation**: Fix typos, add examples, clarify instructions
4. **Submit Code**: Fix bugs or implement new features
5. **Share Feedback**: Let us know how you're using the system

### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Customer-Churn-Prediction-System.git
   ```
3. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes
5. Test thoroughly
6. Commit with clear messages:
   ```bash
   git commit -m "Add: New feature description"
   ```
7. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
8. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions
- Keep functions focused and small

### Testing Guidelines

- Test all new features
- Ensure existing tests pass
- Add tests for bug fixes
- Test on multiple environments

### Pull Request Process

1. Update README if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update documentation
5. Request review from maintainers

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Samay-AI-Verse

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contact

**Project Maintainer**: Samay-AI-Verse

- **GitHub**: [@Samay-AI-Verse](https://github.com/Samay-AI-Verse)
- **Hugging Face**: [@Samay-Verse](https://huggingface.co/Samay-Verse)
- **Live Demo**: [Customer Churn Predictor](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)

### Get in Touch

- 🐛 **Report Issues**: [GitHub Issues](https://github.com/Samay-AI-Verse/Customer-Churn-Prediction-System/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/Samay-AI-Verse/Customer-Churn-Prediction-System/discussions)
- 📧 **Email**: Open an issue for direct contact

---

## 🙏 Acknowledgments

- **scikit-learn** - For the amazing machine learning library
- **FastAPI** - For the modern, fast web framework
- **Gradio** - For making ML model UIs beautiful and easy
- **Hugging Face** - For model hosting and Spaces platform
- **Docker** - For containerization technology

---

## 📊 Project Stats

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-green)
![Gradio](https://img.shields.io/badge/Gradio-5.9.1-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-red)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🎯 Quick Links

- 🚀 [Live Demo](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)
- 📚 [API Documentation](http://localhost:8000/docs)
- 🤖 [Model on Hugging Face](https://huggingface.co/Samay-Verse/Customer-Churn-Prediction-Model)
- 💻 [GitHub Repository](https://github.com/Samay-AI-Verse/Customer-Churn-Prediction-System)
- 📖 [Full Documentation](#-table-of-contents)

---

<div align="center">

**Built with ❤️ by Samay-AI-Verse**

⭐ Star this repo if you find it helpful!

[Report Bug](https://github.com/Samay-AI-Verse/Customer-Churn-Prediction-System/issues) · [Request Feature](https://github.com/Samay-AI-Verse/Customer-Churn-Prediction-System/issues) · [Documentation](#-table-of-contents)

</div>