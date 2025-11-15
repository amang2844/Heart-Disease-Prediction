import streamlit as st
import pandas as pd 
import joblib 

model=joblib.load("KNN_heart.pkl") 
scaler=joblib.load("scaler.pkl")
expected_columns=joblib.load("columns.pkl")

st.title("Heart Disease Prediction By Aman Goswami💖")
st.markdown("Provide the following details")

age=st.slider("Age",18,100,40)
sex=st.selectbox("Sex",["M","F"])
chest_pain=st.selectbox("Chest Pain Type",["Typical Angina","Atypical Angina","Non-Anginal Pain","Asymptomatic"])
resting_bp=st.number_input("Resting Blood Pressure(mm Hg)",80,200,120)
cholesterol=st.number_input("Cholesterol(mg/dl)",100,600,200)
fasting_bs=st.selectbox("Fasting Blood Sugar > 120 mg/dl",[0,1])
resting_ecg=st.selectbox("Resting ECG",["Normal","ST-T Abnormality","LV Hypertrophy"])
max_hr=st.slider("Max Heart Rate Achieved",60,220,150)
exercise_angina=st.selectbox("Exercise Induced Angina",["Yes","No"])
oldpeak=st.slider("Oldpeak",0.0,6.0,1.0)
st_slope=st.selectbox("ST Slope",["Up","Flat","Down"])

if st.button("Predict"):
    raw_input={
        "Age":age,
        "Sex_"+sex:1,
        "Chest Pain Type_"+chest_pain:1,
        "Resting Blood Pressure":resting_bp,
        "Cholesterol":cholesterol,
        "Fasting Blood Sugar":fasting_bs,
        "Resting ECG_"+resting_ecg:1,
        "Max Heart Rate Achieved":max_hr,
        "Exercise Induced Angina_"+exercise_angina:1,
        "Oldpeak":oldpeak,
        "ST Slope_"+st_slope:1,
    }
    input_df=pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col]=0
    input_df=input_df[expected_columns]

    scaled_input=scaler.transform(input_df)
    prediction=model.predict(scaled_input)[0]

    if prediction==1:
        st.error("⚠️ High Chance of Heart Disease")
    else:
        st.success("💖 Low Chance of Heart Disease")