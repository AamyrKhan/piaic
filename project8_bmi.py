import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter your height in cm: ", 50,250,170)
weight = st.slider("Enter your weight in kg: ", 20,220,48)
bmi = weight/((height/100)**2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("***** BMI Categories *****")
st.write("1- Under weight : BMI < 18.5")
st.write("2- Normal : BMI > 18.5 and < 24.9")
st.write("3- Over weight : BMI > 25.0 and < 29.9")
st.write("4- Obese : BMI > 29.9")