---
title: Customer Churn Prediction
emoji: 🎯
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# 🎯 Customer Churn Prediction System

An AI-powered customer churn prediction system that helps businesses identify at-risk customers and take proactive retention actions.

## 🚀 Features

- **Real-time Predictions**: Instant churn risk assessment
- **Beautiful UI**: Modern, gradient-based interface with smooth animations
- **Actionable Insights**: Get specific recommendations for each prediction
- **Probability Scores**: See confidence levels for each prediction
- **Interactive Examples**: Pre-loaded customer profiles to test

## 🤖 Model Details

- **Algorithm**: Random Forest Classifier
- **Accuracy**: ~85%
- **Features**: 10 customer attributes including demographics, usage patterns, and financial data
- **Model Repository**: [Samay-Verse/Customer-Churn-Prediction-Model](https://huggingface.co/Samay-Verse/Customer-Churn-Prediction-Model)

## 📊 Input Features

1. **Demographics**: Age, Gender
2. **Account Info**: Tenure, Subscription Type, Contract Length
3. **Usage**: Usage Frequency, Last Interaction
4. **Financial**: Total Spend, Payment Delay
5. **Support**: Support Calls

## 💡 Use Cases

- Identify high-risk customers before they churn
- Prioritize retention efforts
- Optimize customer success strategies
- Reduce customer acquisition costs

## 🛠️ Technology Stack

- **Framework**: Gradio
- **ML Library**: scikit-learn
- **Model Hosting**: Hugging Face Hub
- **Deployment**: Hugging Face Spaces

## 📝 How to Use

1. Adjust the sliders and dropdowns to match your customer's profile
2. Click "Predict Churn Risk"
3. Review the prediction, confidence score, and recommendations
4. Take action based on the insights!

## 🐳 Docker Deployment

### Option 1: Docker Compose (Recommended)

Run both Gradio UI and FastAPI with one command:

```bash
docker-compose up -d
```

- **Gradio UI**: http://localhost:7860
- **FastAPI**: http://localhost:8000

### Option 2: Docker Build & Run

Build the image:
```bash
docker build -t churn-prediction .
```

Run Gradio UI:
```bash
docker run -p 7860:7860 churn-prediction
```

Run FastAPI:
```bash
docker run -p 8000:8000 churn-prediction python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Stop Services

```bash
docker-compose down
```

## 🚀 Local Development

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Gradio UI

```bash
python app.py
```

### Run FastAPI

```bash
python -m uvicorn main:app --reload
```

## 📁 Project Structure

```
├── app.py                 # Gradio UI application
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Multi-service Docker setup
├── .gitignore          # Git ignore rules
├── .dockerignore       # Docker ignore rules
├── example_request.json # Sample API request
└── README.md           # This file
```

## 👨‍💻 Developer

Built by Samay | [GitHub](https://github.com/Samay-AI-Verse)

---

*Powered by Hugging Face 🤗*
