import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")
st.title("🏠 House Price Prediction using Machine Learning")
st.write("Enter property and area details to estimate the house value.")

model = joblib.load("house_price_model.pkl")

fields = [
    ("MedInc","Median Income",0.0,20.0,5.0),
    ("HouseAge","House Age",1.0,100.0,20.0),
    ("AveRooms","Average Rooms",1.0,20.0,5.0),
    ("AveBedrms","Average Bedrooms",0.1,10.0,1.0),
    ("Population","Population",1.0,50000.0,1000.0),
    ("AveOccup","Average Occupancy",0.1,20.0,3.0),
    ("Latitude","Latitude",32.0,42.0,34.0),
    ("Longitude","Longitude",-125.0,-114.0,-118.0),
]
values={}
for key,label,lo,hi,default in fields:
    values[key]=st.number_input(label, min_value=lo, max_value=hi, value=default)

if st.button("Predict Price"):
    prediction=model.predict(pd.DataFrame([values]))[0]
    st.success(f"Estimated House Value: ${prediction*100000:,.0f}")
