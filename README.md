Heart Assistant
Heart Assistant is a Streamlit web application designed for predicting the likelihood of heart disease based on user inputs. The application leverages a machine learning model to analyze various health metrics and provide a prediction on whether an individual might be suffering from heart disease.

Features
User Input Fields: Enter various health parameters such as age, sex, chest pain types, blood pressure, cholesterol levels, and more.
Prediction Model: Uses a pre-trained heart disease prediction model to analyze the inputs.
User-Friendly Interface: Provides a clean and interactive interface with custom styling for an enhanced user experience.
Project Description
The Heart Assistant project is built using Python and Streamlit, with the main functionality being driven by a machine learning model. The application allows users to input various health metrics and receive a prediction on their heart disease status. The model used for prediction is a serialized object that has been trained on relevant data.

Installation
To run the Heart Assistant web application, follow these steps:

Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/heart-assistant.git
Navigate to the Project Directory

bash
Copy code
cd heart-assistant
Install the Required Packages

You can install the required packages using pip. It's recommended to use a virtual environment.

bash
Copy code
pip install -r requirements.txt
Run the Application

Ensure you have the model/heart_disease_model.sav file in the specified directory. Then run the Streamlit app.

bash
Copy code
streamlit run main.py
Usage
Open the Heart Assistant application in your browser.
Enter the required health metrics in the input fields.
Click on the Heart Disease Test Result button to get the prediction.
The result will be displayed indicating whether the user might have heart disease or not.
Files
main.py: The main application file that contains the Streamlit code for the web app.
model/heart_disease_model.sav: The serialized machine learning model used for prediction.
requirements.txt: A file listing the required Python packages for the project.
