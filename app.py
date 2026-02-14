import streamlit as st

st.set_page_config(page_title="My First Streamlit App")

st.title("Hello Streamlit!")
st.write("This app is deployed using GitHub + Streamlit Cloud")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}")