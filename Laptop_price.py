import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import joblib
import pickle
from xgboost import XGBRegressor

a=st.title("Laptop Price Prediction Application")
st.write("Using this application, one can predict the prices of the laptops acccording to the brands & other features.")

# with open("model.pkl","rb") as f:
#     mod = joblib.load(f)

brand = st.selectbox("Enter Brand",['HP', 'Apple', 'Lenovo', 'ASUS', 'DELL', 'Acer', 'Other', 'MSI',
       'Infinix'])
processor = st.selectbox("Enter Processor",['Core i3', 'Other', 'Core i7', 'Core i5', 'Ryzen 5 Hexa Core',
       'Celeron Dual Core', 'Ryzen 7 Octa Core', 'Ryzen 3 Quad Core'])
os = st.selectbox("Enter Operating System",["Other","Chrome","DOS","Windows 10 Home","Windows 10",'Windows 11 Home'])
storage = st.selectbox("Enter Storage",['Other','Core i3','Core i5', 'Core i7','Celeron Dual Core', 'Ryzen 3 Quad Core', 'Ryzen 5 Hexa Core',
       'Ryzen 7 Octa Core'])
ram = st.selectbox("Enter RAM",[ 8.0, 16.0,  4.0, 12.0, 32.0, 64.0, 18.0])
screen_type = st.selectbox("Enter Screen Type",['Touch Screen","Not a Touch Screen'])
screen_size = st.selectbox("Enter Screen Size",[ 39.62,  33.78,  35.56,  96.52, 100.6 ,  40.89,  35.81,  40.64,
        39.01,  34.54,  34.29,  38.1 ,  38.  ,  29.46,  17.78,  43.94,
        26.67,  34.04,  33.02,  35.  ,  41.15,  90.32,  30.48,  38.86,
        36.07,  31.5])

OS_dic={'Other': 1,
 'Chrome': 2,
 'DOS': 3,
 'Windows 10 Home': 4,
 'Windows 10': 5,
 'Windows 11 Home': 6}

pro_dic={'Other': 1,
 'Core i3': 2,
 'Core i5': 3,
 'Core i7': 4,
 'Celeron Dual Core': 5,
 'Ryzen 3 Quad Core': 6,
 'Ryzen 5 Hexa Core': 7,
 'Ryzen 7 Octa Core': 8}

if st.button("Calculate your Laptop Price"):
    price=st.header(mod.predict([[brand,pro_dic[processor],OS_dic[os],storage,ram,screen_type,screen_size]]))
    st.header(f"Laptop Price: Rs.{price:.2f}")