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

[![Live Demo](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-blue)](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688.svg)](https://fastapi.tiangolo.com)
[![Gradio](https://img.shields.io/badge/Gradio-5.9.1-orange)](https://gradio.app)

> **AI-powered system to predict customer churn and help businesses retain customers**

## 🚀 Live Demo

**Try it now**: [https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)

---

## 📖 What is This?

This project predicts whether a customer will **stay** or **leave** your business using machine learning. It helps you:
- ✅ Identify at-risk customers before they leave
- ✅ Take proactive retention actions
- ✅ Save money by retaining existing customers
- ✅ Make data-driven business decisions

---

## ✨ Features

- 🤖 **Random Forest ML Model** - Trained on customer behavior data
- 🌐 **Beautiful Web UI** - Interactive Gradio interface with modern design
- 🔌 **REST API** - FastAPI backend for programmatic access
- 📊 **Real-time Predictions** - Get instant churn probability scores
- 🐳 **Docker Ready** - Easy deployment with Docker
- ☁️ **Cloud Hosted** - Live on Hugging Face Spaces

---

## 🛠️ Technology Stack

- **Backend**: FastAPI + Uvicorn
- **Frontend**: Gradio with custom CSS
- **ML Model**: scikit-learn Random Forest
- **Model Hosting**: Hugging Face Hub
- **Deployment**: Docker + Hugging Face Spaces

---

## 📁 Project Structure

```
Customer Churn Prediction System/
│
├── app.py                      # Gradio web interface
├── main.py                     # FastAPI backend server
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── example_request.json        # Sample API request
└── README.md                   # This file
```

---

## 🚀 Quick Start

### Option 1: Use the Live Demo (Easiest)

Just visit: **[https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)**

### Option 2: Run Locally

#### Prerequisites
- Python 3.10+
- pip

#### Installation

```bash
# Clone the repository
git clone https://github.com/Samay-AI-Verse/customer-churn-prediction.git
cd customer-churn-prediction

# Install dependencies
pip install -r requirements.txt
```

#### Run the Application

**Terminal 1 - Start API:**
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Start UI:**
```bash
python app.py
```

**Access:**
- 🌐 Web UI: http://localhost:7860
- 📚 API Docs: http://localhost:8000/docs

### Option 3: Run with Docker

```bash
# Build Docker image
docker build -t customer-churn-prediction .

# Run container
docker run -p 7860:7860 -p 8000:8000 customer-churn-prediction
```

**Access:**
- 🌐 Web UI: http://localhost:7860
- 📚 API Docs: http://localhost:8000/docs

---

## 💻 API Usage

### Predict Churn

**Endpoint:** `POST /predict`

**Example Request:**
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

**Example Response:**
```json
{
  "churn_prediction": 0,
  "churn_probability": 0.23
}
```

**Python Example:**
```python
import requests

url = "http://localhost:8000/predict"
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

response = requests.post(url, json=data)
result = response.json()

print(f"Churn Prediction: {result['churn_prediction']}")
print(f"Churn Probability: {result['churn_probability']:.2%}")
```

**cURL Example:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d @example_request.json
```

---

## 📊 Input Features

| Feature | Type | Options/Range | Description |
|---------|------|---------------|-------------|
| Age | Integer | 0-120 | Customer's age |
| Gender | String | Male, Female | Customer's gender |
| Tenure | Integer | 0+ | Months with service |
| Usage_Frequency | Integer | 0+ | Usage per month |
| Support_Calls | Integer | 0+ | Support interactions |
| Payment_Delay | Integer | 0+ | Payment delay (days) |
| Subscription_Type | String | Basic, Standard, Premium | Subscription tier |
| Contract_Length | String | Monthly, Quarterly, Annual | Contract type |
| Total_Spend | Float | 0+ | Total spent ($) |
| Last_Interaction | Integer | 0+ | Days since last activity |

---

## 🤖 Model Details

- **Algorithm**: Random Forest Classifier
- **Framework**: scikit-learn 1.6.1
- **Hosted On**: [Hugging Face Hub](https://huggingface.co/Samay-Verse/Customer-Churn-Prediction-Model)
- **Features**: 10 customer attributes
- **Output**: Binary prediction (0=Stay, 1=Leave) + Probability score

### Model Performance

The model demonstrates excellent performance with strong generalization:

| Metric | Score |
|--------|-------|
| **Accuracy** | 95.40% |
| **Precision** | 99.99% |
| **Recall** | 91.92% |
| **F1-Score** | 95.79% |
| **Training Score** | 95.49% |
| **Test Score** | 95.40% |

**Key Insights:**
- High precision (99.99%) means very few false positives - when the model predicts churn, it's almost always correct
- Strong recall (91.92%) ensures we catch most customers who will actually churn
- Minimal gap between training and test scores indicates excellent generalization with no overfitting
- Overall accuracy of 95.4% makes this model reliable for real-world business decisions

---

## 🌐 Deployment

### Hugging Face Spaces (Current)

Live at: **[https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)**

The app runs on Hugging Face Spaces using Docker SDK.

### Local Deployment

See [Quick Start](#-quick-start) section above.

---

## 🔧 Troubleshooting

### API Not Responding
```bash
# Check if API is running
curl http://localhost:8000/health
```

### Port Already in Use
```bash
# Windows - Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <process_id> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

---

## 📦 Dependencies

```
fastapi==0.115.6
uvicorn==0.34.0
pandas==2.2.3
joblib==1.4.2
huggingface_hub==0.27.1
pydantic==2.10.5
scikit-learn==1.6.1
gradio==5.9.1
requests==2.32.3
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---

## 📄 License

MIT License - See LICENSE file for details

---

## 📞 Contact

- **GitHub**: [@Samay-AI-Verse](https://github.com/Samay-AI-Verse)
- **Hugging Face**: [@Samay-Verse](https://huggingface.co/Samay-Verse)
- **Live Demo**: [Customer Churn Predictor](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)

---

## 🎯 Quick Links

- 🚀 **[Live Demo](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)** - Try it now!
- 📚 **[API Documentation](http://localhost:8000/docs)** - When running locally
- 🤖 **[Model on Hugging Face](https://huggingface.co/Samay-Verse/Customer-Churn-Prediction-Model)** - Pre-trained model
- 💻 **[GitHub Repository](https://github.com/Samay-AI-Verse/customer-churn-prediction)** - Source code
- 📓 **[Jupyter Notebook](YOUR_NOTEBOOK_LINK_HERE)** - Model training & evaluation

---

<div align="center">

**Built with ❤️ by Samay-AI-Verse**

⭐ Star this repo if you find it helpful!

**[Try Live Demo](https://huggingface.co/spaces/Samay-Verse/Customer-Churn-Prediction)** | **[Report Bug](https://github.com/Samay-AI-Verse/customer-churn-prediction/issues)** | **[Request Feature](https://github.com/Samay-AI-Verse/customer-churn-prediction/issues)**

</div>