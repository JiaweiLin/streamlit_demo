from anthropic import Anthropic
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

def get_response(user_content): 
    client = Anthropic(api_key=my_api_key)
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system="Generate 5 Singaporean local food names based on user-provided keywords",
        messages=[{"role":"user", "content":user_content}],
    )
    return response.content[0].text

st.title("Singaporean food names")
user_content = st.text_input("Enter the keyword(s) for Singaporean food:")

if st.button("Generate Singaporean food names"):
    if not user_content:
        st.warning("Please enter a keyword before generating Singaporean food names.", icon = "⚠️")
    generated_titles = get_response(user_content)
    st.success("Singaporean food names generated successfully!")
    st.text_area("", value=generated_titles, height=500)