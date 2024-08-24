import streamlit as st
import requests
import json
from carbon.estimate import estimation_to_string
from carbon.schemas import Estimation


url = st.secrets["api_url"]
st.title("Carbonada")

# Text input field
user_input = st.text_input("What would you like to estimate the carbon footprint of?")

# Button to submit the text
if st.button("Estimate!"):
    if user_input:
        payload = json.dumps({
            "product": user_input
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = json.loads(response.text)
        # Print or display the response
        estimation = Estimation(**response_data)
        st.markdown(estimation_to_string(estimation))
    else:
        st.warning("Please enter a product to estimate the carbon footprint.")
