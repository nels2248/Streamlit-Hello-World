import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name: dude")
if st.button("Submit"):
    st.write(f"Hello, {name}!")