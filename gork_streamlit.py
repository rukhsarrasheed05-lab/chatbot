import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key=os.getenv("GROK_KEY"))
MODEL = "llama-3.1-8b-instant"

st.title("Groq AI Chatbot")

user_input = st.text_input("Ask something:")

if user_input:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": user_input}]
    )

    st.write("🤖", response.choices[0].message.content)