import streamlit as st
import pickle
import numpy as np

# Model load karo
with open('sales_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Sales Prediction App", page_icon="📊")
st.title("📊 Sales Prediction App")

tv = st.number_input("TV Advertising Budget", min_value=0.0, value=100.0)
radio = st.number_input("Radio Advertising Budget", min_value=0.0, value=20.0)
newspaper = st.number_input("Newspaper Advertising Budget", min_value=0.0, value=10.0)

if st.button("Predict Sales"):
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)
    st.success(f"✅ Predicted Sales: {prediction[0]:.2f} units")