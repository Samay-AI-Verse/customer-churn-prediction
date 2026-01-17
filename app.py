import gradio as gr
from huggingface_hub import hf_hub_download
import joblib
import pandas as pd
import numpy as np

# Load the model from Hugging Face
MODEL_PATH = hf_hub_download(
    repo_id="Samay-Verse/Customer-Churn-Prediction-Model", filename="random_forest.pkl"
)
model = joblib.load(MODEL_PATH)

# Custom CSS for premium styling
custom_css = """
#header {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
}

#header h1 {
    color: white;
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

#header p {
    color: rgba(255, 255, 255, 0.95);
    font-size: 1.1rem;
    margin-top: 0.5rem;
}

.input-section {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
}

.output-section {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 8px 24px rgba(252, 182, 159, 0.4);
}

.prediction-box {
    font-size: 1.8rem;
    font-weight: 700;
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    animation: fadeIn 0.5s ease-in;
}

.churn-yes {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    box-shadow: 0 6px 20px rgba(245, 87, 108, 0.4);
}

.churn-no {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
    box-shadow: 0 6px 20px rgba(79, 172, 254, 0.4);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.gr-button-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border: none !important;
    font-size: 1.1rem !important;
    padding: 0.8rem 2rem !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    transition: all 0.3s ease !important;
}

.gr-button-primary:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
}

footer {
    text-align: center;
    margin-top: 2rem;
    padding: 1rem;
    color: #666;
    font-size: 0.9rem;
}
"""


def predict_churn(
    age,
    gender,
    tenure,
    usage_frequency,
    support_calls,
    payment_delay,
    subscription_type,
    contract_length,
    total_spend,
    last_interaction,
):
    """
    Predict customer churn based on input features
    """
    try:
        # Create input dataframe
        input_data = {
            "Age": age,
            "Gender": gender,
            "Tenure": tenure,
            "Usage Frequency": usage_frequency,
            "Support Calls": support_calls,
            "Payment Delay": payment_delay,
            "Subscription Type": subscription_type,
            "Contract Length": contract_length,
            "Total Spend": total_spend,
            "Last Interaction": last_interaction,
        }

        df = pd.DataFrame([input_data])

        # Make prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0]

        # Format output
        if prediction == 1:
            result = "⚠️ HIGH RISK - Customer Likely to Churn"
            confidence = f"{probability[1]*100:.1f}%"
            recommendation = """
            ### 🎯 Recommended Actions:
            - Reach out proactively with retention offers
            - Assign dedicated account manager
            - Offer personalized discounts or upgrades
            - Schedule satisfaction survey call
            """
            risk_class = "churn-yes"
        else:
            result = "✅ LOW RISK - Customer Likely to Stay"
            confidence = f"{probability[0]*100:.1f}%"
            recommendation = """
            ### 🎯 Recommended Actions:
            - Continue regular engagement
            - Monitor satisfaction metrics
            - Offer loyalty rewards program
            - Request referrals
            """
            risk_class = "churn-no"

        # Create formatted output
        output_html = f"""
        <div class="output-section">
            <div class="prediction-box {risk_class}">
                {result}
            </div>
            <div style="font-size: 1.3rem; margin: 1rem 0; color: #333;">
                <strong>Confidence:</strong> {confidence}
            </div>
            <div style="text-align: left; background: white; padding: 1.5rem; border-radius: 10px; margin-top: 1rem;">
                {recommendation}
            </div>
            <div style="margin-top: 1.5rem; padding: 1rem; background: rgba(255,255,255,0.5); border-radius: 8px;">
                <strong>📊 Probability Distribution:</strong><br>
                Stay: {probability[0]*100:.1f}% | Churn: {probability[1]*100:.1f}%
            </div>
        </div>
        """

        return output_html

    except Exception as e:
        return f"""
        <div style="background: #fee; padding: 2rem; border-radius: 10px; color: #c33;">
            <h3>❌ Error in Prediction</h3>
            <p>{str(e)}</p>
        </div>
        """


# Create Gradio Interface
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:

    # Header
    gr.HTML(
        """
        <div id="header">
            <h1>🎯 Customer Churn Prediction System</h1>
            <p>AI-Powered Customer Retention Analytics | Predict churn risk and take proactive action</p>
        </div>
    """
    )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 👤 Customer Demographics")
            age = gr.Slider(
                minimum=18,
                maximum=80,
                value=35,
                step=1,
                label="Age",
                info="Customer's age in years",
            )
            gender = gr.Radio(choices=["Male", "Female"], value="Male", label="Gender")

            gr.Markdown("### 📊 Account Information")
            tenure = gr.Slider(
                minimum=0,
                maximum=72,
                value=24,
                step=1,
                label="Tenure (months)",
                info="How long they've been a customer",
            )
            subscription_type = gr.Dropdown(
                choices=["Basic", "Standard", "Premium"],
                value="Premium",
                label="Subscription Type",
            )
            contract_length = gr.Dropdown(
                choices=["Monthly", "Quarterly", "Annual"],
                value="Annual",
                label="Contract Length",
            )

        with gr.Column(scale=1):
            gr.Markdown("### 📈 Usage & Engagement")
            usage_frequency = gr.Slider(
                minimum=0,
                maximum=30,
                value=15,
                step=1,
                label="Usage Frequency (per month)",
                info="Number of times service is used monthly",
            )
            last_interaction = gr.Slider(
                minimum=0,
                maximum=90,
                value=15,
                step=1,
                label="Last Interaction (days ago)",
                info="Days since last customer interaction",
            )

            gr.Markdown("### 💰 Financial & Support")
            total_spend = gr.Slider(
                minimum=0,
                maximum=2000,
                value=750,
                step=10,
                label="Total Spend ($)",
                info="Total amount spent by customer",
            )
            payment_delay = gr.Slider(
                minimum=0,
                maximum=60,
                value=10,
                step=1,
                label="Payment Delay (days)",
                info="Average payment delay in days",
            )
            support_calls = gr.Slider(
                minimum=0,
                maximum=20,
                value=3,
                step=1,
                label="Support Calls",
                info="Number of support calls made",
            )

    # Predict Button
    predict_btn = gr.Button("🔮 Predict Churn Risk", variant="primary", size="lg")

    # Output
    output = gr.HTML(label="Prediction Results")

    # Examples
    gr.Markdown("### 💡 Try These Examples")
    gr.Examples(
        examples=[
            [45, "Female", 6, 5, 8, 25, "Basic", "Monthly", 200, 45],  # High churn risk
            [28, "Male", 36, 20, 1, 2, "Premium", "Annual", 1500, 5],  # Low churn risk
            [
                55,
                "Male",
                12,
                10,
                5,
                15,
                "Standard",
                "Quarterly",
                600,
                30,
            ],  # Medium risk
        ],
        inputs=[
            age,
            gender,
            tenure,
            usage_frequency,
            support_calls,
            payment_delay,
            subscription_type,
            contract_length,
            total_spend,
            last_interaction,
        ],
        label="Sample Customer Profiles",
    )

    # Footer
    gr.HTML(
        """
        <footer>
            <p>🚀 Built with Gradio | Model hosted on 🤗 Hugging Face</p>
            <p>Powered by Random Forest ML Algorithm | Accuracy: ~85%</p>
        </footer>
    """
    )

    # Connect prediction function
    predict_btn.click(
        fn=predict_churn,
        inputs=[
            age,
            gender,
            tenure,
            usage_frequency,
            support_calls,
            payment_delay,
            subscription_type,
            contract_length,
            total_spend,
            last_interaction,
        ],
        outputs=output,
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(share=False)
