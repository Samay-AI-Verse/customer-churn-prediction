import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/predict"


# -----------------------------
# Prediction Function
# -----------------------------
def predict_customer_retention(
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

        prediction = result.get("churn_prediction")
        probability = result.get("churn_probability")

        # 0 = Customer will stay, 1 = Customer will leave
        if prediction == 1:
            status = "🚨 High Risk - Customer Will Likely Leave"
            risk_level = "High Risk"
            color = "#ff4444"
            recommendation = "⚠️ Immediate action recommended: Reach out with retention offers, personalized discounts, or customer support."
        else:
            status = "✅ Safe - Customer Will Likely Stay"
            risk_level = "Low Risk"
            color = "#00C851"
            recommendation = "👍 Customer is satisfied. Continue providing excellent service to maintain loyalty."

        # Format probability as percentage
        leave_probability = f"{probability * 100:.1f}%" if probability else "N/A"
        stay_probability = f"{(1 - probability) * 100:.1f}%" if probability else "N/A"

        # Create detailed result
        result_html = f"""
        <div style="padding: 25px; border-radius: 15px; background: linear-gradient(135deg, {color}15 0%, {color}05 100%); border-left: 5px solid {color}; margin: 10px 0;">
            <h2 style="color: {color}; margin: 0 0 15px 0; font-size: 24px;">{status}</h2>
            <div style="background: white; padding: 20px; border-radius: 10px; margin: 15px 0;">
                <h3 style="margin: 0 0 10px 0; color: #333;">📊 Prediction Details</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0;">
                    <div style="padding: 15px; background: #f8f9fa; border-radius: 8px;">
                        <p style="margin: 0; color: #666; font-size: 13px;">Probability to Leave</p>
                        <p style="margin: 5px 0 0 0; font-size: 28px; font-weight: bold; color: #ff4444;">{leave_probability}</p>
                    </div>
                    <div style="padding: 15px; background: #f8f9fa; border-radius: 8px;">
                        <p style="margin: 0; color: #666; font-size: 13px;">Probability to Stay</p>
                        <p style="margin: 5px 0 0 0; font-size: 28px; font-weight: bold; color: #00C851;">{stay_probability}</p>
                    </div>
                </div>
                <div style="margin-top: 15px; padding: 15px; background: #fff3cd; border-radius: 8px; border-left: 4px solid #ffc107;">
                    <p style="margin: 0; color: #856404; line-height: 1.6;"><strong>💡 Recommendation:</strong><br/>{recommendation}</p>
                </div>
            </div>
        </div>
        """

        return result_html

    except Exception as e:
        error_html = f"""
        <div style="padding: 20px; border-radius: 10px; background: #ffebee; border-left: 5px solid #f44336;">
            <h3 style="color: #c62828; margin: 0 0 10px 0;">❌ Error</h3>
            <p style="margin: 0; color: #666;">Failed to get prediction. Please check if the API is running.</p>
            <p style="margin: 10px 0 0 0; color: #999; font-size: 12px;">Error: {str(e)}</p>
        </div>
        """
        return error_html


# -----------------------------
# Custom CSS for Premium Look
# -----------------------------
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
    font-family: 'Inter', sans-serif !important;
}

.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}

.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 40px;
    border-radius: 20px;
    margin-bottom: 30px;
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
}

.main-header h1 {
    color: white !important;
    font-size: 42px !important;
    font-weight: 700 !important;
    margin: 0 0 10px 0 !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.main-header p {
    color: rgba(255,255,255,0.95) !important;
    font-size: 16px !important;
    margin: 0 !important;
}

.input-section {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.section-title {
    color: #667eea;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #667eea;
}

button.primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    padding: 15px 40px !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    transition: all 0.3s ease !important;
}

button.primary:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
}

.info-box {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 20px;
    border-radius: 12px;
    margin: 20px 0;
    border-left: 4px solid #667eea;
}
"""

# -----------------------------
# Gradio UI with Premium Design
# -----------------------------
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:

    # Header
    gr.HTML(
        """
        <div class="main-header">
            <h1>🎯 Customer Retention Predictor</h1>
            <p>AI-Powered Analysis to Predict Customer Loyalty | Built with Random Forest ML Model</p>
        </div>
    """
    )

    # Info Section
    gr.Markdown(
        """
        <div class="info-box">
            <h3 style="margin: 0 0 10px 0; color: #667eea;">📋 How It Works</h3>
            <p style="margin: 0; color: #555; line-height: 1.8;">
                Enter customer information below to predict whether they will <strong>continue using your service</strong> or <strong>leave</strong>. 
                Our AI model analyzes patterns like usage behavior, payment history, and engagement to provide accurate predictions.
            </p>
        </div>
    """
    )

    # Input Section
    with gr.Row():
        with gr.Column(scale=1):
            gr.HTML('<div class="section-title">👤 Customer Profile</div>')
            Age = gr.Slider(
                minimum=18,
                maximum=100,
                value=30,
                step=1,
                label="Age",
                info="Customer's age in years",
            )
            Gender = gr.Radio(
                choices=["Male", "Female"],
                label="Gender",
                value="Male",
                info="Customer's gender",
            )
            Tenure = gr.Slider(
                minimum=0,
                maximum=120,
                value=12,
                step=1,
                label="Tenure (Months)",
                info="How long has the customer been with you?",
            )
            Total_Spend = gr.Number(
                label="Total Spend ($)",
                value=500,
                info="Total amount spent by customer",
            )

        with gr.Column(scale=1):
            gr.HTML('<div class="section-title">📊 Usage & Engagement</div>')
            Usage_Frequency = gr.Slider(
                minimum=0,
                maximum=50,
                value=10,
                step=1,
                label="Usage Frequency (per month)",
                info="How often does the customer use your service?",
            )
            Last_Interaction = gr.Slider(
                minimum=0,
                maximum=365,
                value=5,
                step=1,
                label="Last Interaction (Days Ago)",
                info="When did the customer last engage with you?",
            )
            Support_Calls = gr.Slider(
                minimum=0,
                maximum=20,
                value=1,
                step=1,
                label="Support Calls",
                info="Number of customer support interactions",
            )
            Payment_Delay = gr.Slider(
                minimum=0,
                maximum=90,
                value=0,
                step=1,
                label="Payment Delay (Days)",
                info="Average payment delay in days",
            )

        with gr.Column(scale=1):
            gr.HTML('<div class="section-title">💳 Subscription Details</div>')
            Subscription_Type = gr.Radio(
                choices=["Basic", "Standard", "Premium"],
                label="Subscription Type",
                value="Standard",
                info="Current subscription plan",
            )
            Contract_Length = gr.Radio(
                choices=["Monthly", "Quarterly", "Annual"],
                label="Contract Length",
                value="Monthly",
                info="Contract commitment period",
            )

    # Predict Button
    predict_btn = gr.Button(
        "🔮 Predict Customer Retention", elem_classes=["primary"], size="lg"
    )

    # Output Section
    gr.Markdown("### 📈 Prediction Results")
    output = gr.HTML(label="Results")

    # Examples Section
    gr.Markdown("### 💡 Try These Examples")
    gr.Examples(
        examples=[
            [35, "Male", 24, 15, 3, 10, "Premium", "Annual", 1200, 5],  # Likely to stay
            [45, "Female", 6, 2, 8, 25, "Basic", "Monthly", 150, 45],  # Likely to leave
            [28, "Male", 36, 20, 1, 0, "Premium", "Annual", 2500, 2],  # Likely to stay
        ],
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
        label="Click to load example data",
    )

    # Connect the button
    predict_btn.click(
        fn=predict_customer_retention,
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

    # Footer
    gr.Markdown(
        """
        ---
        <div style="text-align: center; color: #666; padding: 20px;">
            <p>🚀 Powered by FastAPI + Random Forest ML + Hugging Face + Docker</p>
            <p style="font-size: 12px;">Built with ❤️ for better customer retention insights</p>
        </div>
    """
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
