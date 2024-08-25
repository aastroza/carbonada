import streamlit as st
import requests
import json

url = st.secrets["api_url"]
st.title("Carbonada")

# Text input field
user_input = st.text_input("¿De qué te gustaría estimar la huella de carbono?")

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
        st.markdown(response_data["explanation"])
    else:
        st.warning("Please enter a product to estimate the carbon footprint.")
