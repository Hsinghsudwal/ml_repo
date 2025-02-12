import shutil
import os

def deploy_streamlit(streamlit_dir):
    """Deploy the model and code to the Streamlit app directory."""
    app_source = "deployment/streamlit_app"
    
    if os.path.exists(app_source):
        if os.path.exists(streamlit_dir):
            shutil.rmtree(streamlit_dir)  # Clear old app
        shutil.copytree(app_source, streamlit_dir)
        print(f"Streamlit app deployed at {streamlit_dir}")
    else:
        raise FileNotFoundError("Streamlit app source folder not found.")

































import shutil
import os


def deploy_streamlit(streamlit_dir):
    # Assuming that the Streamlit app files are inside the 'deployment/streamlit_app' directory
    app_source = "ml_h/deployment/streamlit_app"

    # Copy Streamlit app files to the deployment folder
    if os.path.exists(app_source):
        if os.path.exists(streamlit_dir):
            shutil.rmtree(streamlit_dir)  # Remove old deployment folder if it exists
        shutil.copytree(app_source, streamlit_dir)  # Copy new Streamlit app files

        print(f"Streamlit app deployed to {streamlit_dir}")
    else:
        raise FileNotFoundError("Streamlit app files not found.")


# streamlit_app/app.py
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("data/models/model.pkl")

st.title("Iris Flower Prediction")
sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.write(f"Predicted class: {prediction}")


import shutil
import os


def deploy_streamlit(streamlit_dir):
    # Assumes a predefined Streamlit app folder
    app_source = "deployment/streamlit_app"

    if os.path.exists(app_source):
        if os.path.exists(streamlit_dir):
            shutil.rmtree(streamlit_dir)  # Clear old app
        shutil.copytree(app_source, streamlit_dir)
        print(f"Streamlit app deployed at {streamlit_dir}")
    else:
        raise FileNotFoundError("Streamlit app source folder not found.")
