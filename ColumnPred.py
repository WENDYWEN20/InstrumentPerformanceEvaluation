import streamlit as st
header=st.container()
dataset=st.container()
features=st.container()
modelTraining=st.container()
with header:
    st.title("Waters Column Performance Web App")
# Create a page dropdown
#page = st.sidebar.selectbox(“Please select model”, [ “Linear Regressor”, “XGB Regressor”, “LGBM Regressor”,  “Compare Models”])


import numpy as np
import pickle  
Columninput=st.container()
with Columninput:
    st.text("Enter the value of Column Performance")
    Area=st.number_input("Area Count")
    Area_P=st.number_input("%Area")
    Height=st.number_input("Height")
    Width=st.number_input("Width")
    USP_Resolution=st.number_input("USP Resolution")
    Asym_10=st.number_input(" Asym@10")
    Asym=st.number_input("Asym")
    USP_Tailing=st.number_input("USP_Tailing")
    USP_Plate_Count=st.number_input("USP_Plate_Count")
    Width_Baseline=st.number_input("Width@Baseline")
    Width_Tang=st.number_input("Width@Tangent")
    Width_5=st.number_input("Width@5")
    Width_50=st.number_input("Width@50")
    load_model = pickle.load(open('uplc_column_performance_score.pkl', 'rb'))
    X=[[Area,Area_P,Height,Width,USP_Resolution,Asym_10,Asym,USP_Tailing,USP_Plate_Count,Width_Baseline,Width_Tang,Width_5,Width_50]]
    load_model = pickle.load(open('uplc_column_performance_score.pkl', 'rb'))
    prediction=load_model.predict(X)
    prediction_proba=load_model.predict_proba(X)
    
    st.header("Predicted Standard")
    prediction
    prediction_proba
