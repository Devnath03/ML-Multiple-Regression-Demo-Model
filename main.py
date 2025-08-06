import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pickel","rb"))

# Main application file for Streamlit
st.title("Startup Profit Prediction")


RD = st.text_input("R&D Spend", key="1")
Administration = st.text_input("Administration", key="2")
Marketing = st.text_input("Marketing", key="3")

state = st.selectbox("Do You State:", ["California","Florida"])
state_value = 1 if state == "California" else 0

if st.button("Predict"):
    inp = np.array([[float(RD), float(Administration), float(Marketing), float(state_value)]])
    prediction = model.predict(inp)
    st.success(f"profit: Rs. {prediction[0]:,.2f} ")