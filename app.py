import streamlit as st
import requests

user_input = st.text_input("Enter your text here")
submit = st.button('Submit')

if submit:
    url = 'http://sentimentreview.eastus.azurecontainer.io:8001/predict_probability'
    response = requests.post(url, json={"review": user_input})
    prediction = response.json()
    st.write(f'The prediction is: {prediction}')

