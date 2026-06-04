Video's link: https://drive.google.com/file/d/1Dk3SJwMojLWcsl0JtHaPXY1H-n9ZeTUW/view?usp=sharing

#  Cardiovascular Disease Prediction System using Machine Learning

This repository contains an end-to-end Machine Learning pipeline designed to explore, preprocess, model, and deploy a predictive system for cardiovascular diseases. The project is fully aligned with academic requirements and leverages data-driven approaches to assist clinical decision-making.

##  Dataset Overview
The project utilizes a clinical dataset containing comprehensive cardiovascular health metrics. 
- **Initial Dimensions:** ~70,000 patient records and 13 structural columns.
- **Key Features Analyzed:** Age, Blood Pressure (Systolic/Diastolic), Cholesterol, Glucose levels, Smoking status, Alcohol consumption, Physical activity, and calculated **BMI**.

##  Machine Learning Pipeline Implemented

1. **Exploratory Data Analysis (EDA):** Analyzed data distributions, identified outliers in blood pressure readings, and mapped correlation matrices.
2. **Data Preprocessing & Cleansing:** Handled missing/corrupted values, corrected blood pressure physiological anomalies, and performed feature scaling (StandardScaler) for linear models.
3. **Feature Engineering:** Strategically introduced a new engineered feature combining clinical attributes to capture interactive biological risks.
4. **Predictive Modeling:** Evaluated three distinct algorithms to ensure optimal performance bounds:
   - **Logistic Regression**
   - **Decision Tree Classifier**
   - **Random Forest Classifier (The Winning Model)**

##  Model Performance Results
The models achieved high evaluation metrics, with the **Random Forest Classifier** selected as the optimal model for final deployment due to its superior generalization capabilities and high accuracy score.

##  Web Application Interface (Gradio Deployment)
The winning model has been serialized into a `heart_disease_rf_model.pkl` file and deployed via a dynamic **Gradio** web interface (`app.py`). The interface allows medical professionals to interactively slide and enter a patient's vital metrics to obtain real-time cardiovascular risk assessments.

##  Repository Structure
- `heart_disease_project.ipynb` : The full data science workflow notebook.
- `app.py` : Script running the interactive Gradio web deployment.
- `heart_disease_rf_model.pkl` : The serialized, production-ready Random Forest model.
- `requirements.txt` : The list of software packages and dependencies.
- `README.md` : Project documentation guide (This file).

##  How to Run the App Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Launch the application: `python app.py`
