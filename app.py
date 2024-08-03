import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Heart Assistant",
                   layout="wide",
                   page_icon="🫀")

# Custom CSS for colorful UI and header styling
st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
    }
    .stApp {
        background: linear-gradient(to right, #74ebd5, #acb6e5);
        padding: 20px;
        border-radius: 10px;
    }
    .header-container {
        background-color: #1f77b4;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
    }
    .header-text {
        font-size: 36px;
        font-weight: bold;
    }
    .stButton button {
        background-color: #00cc96;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        margin-top: 20px;
    }
    .stTextInput > div > input {
        background-color: #e0f7fa;
        border-radius: 5px;
        padding: 10px;
    }
    .stSuccess {
        background-color: #3cff00; 
        color: red;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
heart_disease_model = pickle.load(open(f'{working_dir}/model/heart_disease_model.sav', 'rb'))

# Heart Disease Prediction Page
# Page header with different background
st.markdown("""
    <div class="header-container">
        <div class="header-text">🩺Welcome to Heart Disease Prediction Application!🫀</div>
    </div>
    <br>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex')

with col3:
    cp = st.text_input('Chest Pain types')

with col1:
    trestbps = st.text_input('Resting Blood Pressure')

with col2:
    chol = st.text_input('Serum Cholesterol in mg/dl')

with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
    restecg = st.text_input('Resting Electrocardiographic results')

with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')

with col3:
    exang = st.text_input('Exercise Induced Angina')

with col1:
    oldpeak = st.text_input('ST depression induced by exercise')

with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
    ca = st.text_input('Major vessels colored by fluoroscopy')

with col1:
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

# Code for Prediction
heart_diagnosis = ''

col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

# Display the result in the center column with custom styling
with col2:
    if heart_diagnosis:
        st.markdown(f"""
            <div class="stSuccess">
                {heart_diagnosis}
            </div>
        """, unsafe_allow_html=True)
