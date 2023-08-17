import streamlit as st
import requests

st.write("# Welcome to SQLChat Assistant! 👋")

st.write(
    "Greetings! I'm your sql assistant.\n Together we can craft any sql query you want.")
session_name = st.text_input("Provide a name for your chat session")

if session_name:
    messages = requests.get(f"http://localhost:8000/api/v1/chat/history/{session_name}").json()
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["message"])

    prompt = st.chat_input("Type a message...")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.spinner("..."):
            res = requests.post(f"http://localhost:8000/api/v1/chat/submit/{session_name}",
                                params={"request": prompt}).json()
            with st.chat_message("assistant"):
                st.markdown(res)

        messages = requests.get(
            f"http://localhost:8000/api/v1/chat/history/{session_name}").json()
