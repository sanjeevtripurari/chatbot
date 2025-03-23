import os
import streamlit as st
import openai
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

#load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(user_input):
    """
    Sends user input to OpenAI's Chat API and returns the model's response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the model suited for chat applications
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        # Extract the text from the last response in the chat
        return response.choices[0].message['content'].strip() if response.choices else "No response from the model."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app layout
st.title("Your Advanced Streamlit Chatbot")
user_input = st.text_input("What would you like to ask?")
if st.button("Submit"):
    chatbot_response = get_openai_response(user_input) if user_input else "Please enter a question or message to get a response."
    st.write(f"Chatbot: {chatbot_response}")
