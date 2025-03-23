import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

#api_key = os.environ['GOOGLE_API_KEY']
#print(api_key)

api_key=st.secrets['gemini']["GOOGLE_API_KEY"]
print(api_key)

genai.configure(api_key=st.secrets['gemini']["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-pro')

st.title("List 5 planets each with an interesting fact")
response = model.generate_content("List 5 planets each with an interesting fact")
st.write(f"{response.text}")

st.title("what are top 5 frequently used emojis?")
response = model.generate_content("what are top 5 frequently used emojis?")
st.write(f"Chatbot: {response.text}")