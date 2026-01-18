import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/predict"


# -----------------------------
# Prediction Function
# -----------------------------
def predict_churn(
    Age,
    Gender,
    Tenure,
    Usage_Frequency,
    Support_Calls,
    Payment_Delay,
    Subscription_Type,
    Contract_Length,
    Total_Spend,
    Last_Interaction,
):
    payload = {
        "Age": int(Age),
        "Gender": Gender,
        "Tenure": int(Tenure),
        "Usage_Frequency": int(Usage_Frequency),
        "Support_Calls": int(Support_Calls),
        "Payment_Delay": int(Payment_Delay),
        "Subscription_Type": Subscription_Type,
        "Contract_Length": Contract_Length,
        "Total_Spend": float(Total_Spend),
        "Last_Interaction": int(Last_Interaction),
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()

        churn = result.get("churn_prediction")
        prob = result.get("churn_probability")

        if churn == 1:
            status = "⚠️ Customer Likely to Churn"
        else:
            status = "✅ Customer Likely to Stay"

        return {"Status": status, "Churn Probability": prob}

    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# Gradio UI
# -----------------------------
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # 🚀 Customer Churn Prediction System  
        AI-powered churn prediction using **Random Forest + FastAPI + Hugging Face + Docker**
        
        Fill in customer details and get real-time churn prediction.
        """
    )

    with gr.Row():
        with gr.Column():
            Age = gr.Number(label="Age", value=30)
            Gender = gr.Dropdown(
                choices=["Male", "Female"], label="Gender", value="Male"
            )
            Tenure = gr.Number(label="Tenure (Months)", value=12)
            Usage_Frequency = gr.Number(label="Usage Frequency / Month", value=10)
            Support_Calls = gr.Number(label="Support Calls", value=1)

        with gr.Column():
            Payment_Delay = gr.Number(label="Payment Delay (Days)", value=0)
            Subscription_Type = gr.Dropdown(
                choices=["Basic", "Standard", "Premium"],
                label="Subscription Type",
                value="Standard",
            )
            Contract_Length = gr.Dropdown(
                choices=["Monthly", "Quarterly", "Annual"],
                label="Contract Length",
                value="Monthly",
            )
            Total_Spend = gr.Number(label="Total Spend", value=500)
            Last_Interaction = gr.Number(label="Last Interaction (Days Ago)", value=5)

    predict_btn = gr.Button("🔍 Predict Churn")
    output = gr.JSON(label="Prediction Result")

    predict_btn.click(
        fn=predict_churn,
        inputs=[
            Age,
            Gender,
            Tenure,
            Usage_Frequency,
            Support_Calls,
            Payment_Delay,
            Subscription_Type,
            Contract_Length,
            Total_Spend,
            Last_Interaction,
        ],
        outputs=output,
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
