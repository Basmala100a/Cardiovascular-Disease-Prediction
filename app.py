import gradio as gr
import joblib

# Load the saved model
model = joblib.load('heart_disease_rf_model.pkl')

def predict_heart_disease(age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active):
    gender_code = 1 if gender == "Female" else 2
    chol_code = 1 if cholesterol == "Normal" else (2 if cholesterol == "Above Normal" else 3)
    gluc_code = 1 if gluc == "Normal" else (2 if gluc == "Above Normal" else 3)
    smoke_code = 1 if smoke == "Yes" else 0
    alco_code = 1 if alco == "Yes" else 0
    active_code = 1 if active == "Yes" else 0
    
    bmi = round(weight / ((height / 100) ** 2), 1)
    
    input_data = [[age, gender_code, height, weight, ap_hi, ap_lo, chol_code, gluc_code, smoke_code, alco_code, active_code, bmi]]
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        return f"⚠️ Warning: High Risk of Cardiovascular Disease! (Calculated BMI: {bmi})"
    else:
        return f"✅ Good News: Patient is Healthy and at Low Risk. (Calculated BMI: {bmi})"

interface = gr.Interface(
    fn=predict_heart_disease,
    inputs=[
        gr.Slider(30, 80, value=50, label="Age (Years)"),
        gr.Radio(["Female", "Male"], value="Female", label="Gender"),
        gr.Slider(100, 220, value=165, label="Height (cm)"),
        gr.Slider(30, 150, value=70, label="Weight (kg)"),
        gr.Slider(80, 200, value=120, label="Systolic BP (ap_hi)"),
        gr.Slider(40, 120, value=80, label="Diastolic BP (ap_lo)"),
        gr.Radio(["Normal", "Above Normal", "Well Above Normal"], value="Normal", label="Cholesterol Level"),
        gr.Radio(["Normal", "Above Normal", "Well Above Normal"], value="Normal", label="Glucose Level"),
        gr.Radio(["Yes", "No"], value="No", label="Smoker?"),
        gr.Radio(["Yes", "No"], value="No", label="Alcohol Consumer?"),
        gr.Radio(["Yes", "No"], value="Yes", label="Physically Active?")
    ],
    outputs=gr.Textbox(label="Prediction Result"),
    title="Real-Time Cardiovascular Disease Prediction System",
    description="Cardiovascular Disease Prediction using Random Forest Model."
)

if __name__ == "__main__":
    interface.launch()