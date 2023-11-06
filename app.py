import streamlit as st

# Title
st.title("My First Streamlit App")

# Button
button = st.button("Click me")

if button:
    st.write("Button clicked!")
