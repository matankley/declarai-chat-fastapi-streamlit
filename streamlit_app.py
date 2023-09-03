import json
import os

import streamlit as st
import requests

BACKEND_URL = os.environ.get("BACKEND_URL") or "http://localhost:8000"

st.write("# Welcome to SQLChat Assistant! 👋")

st.write(
    "Greetings! I'm your sql assistant.\n Together we can craft any sql query you want.")
session_name = st.text_input("Provide a name for your chat session")

streaming = st.sidebar.selectbox("Streaming", [True, False])

if session_name:
    messages = requests.get(f"{BACKEND_URL}/api/v1/chat/history/{session_name}").json()
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["message"])

    prompt = st.chat_input("Type a message...")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        if streaming:
            res = requests.post(f"{BACKEND_URL}/api/v1/chat/submit/{session_name}/streaming",
                                params={"request": prompt},
                                stream=True)
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                buffer = ""
                for chunk in res:
                    decoded_chunk = chunk.decode('utf-8')
                    buffer += decoded_chunk

                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        parsed_chunk = json.loads(line.strip())
                        try:
                            full_response += parsed_chunk["raw_response"]["choices"][0]["delta"]["content"]
                            message_placeholder.markdown(full_response + "▌")
                        except KeyError:
                            pass

                message_placeholder.markdown(full_response)
        else:
            with st.spinner("..."):
                res = requests.post(f"{BACKEND_URL}/api/v1/chat/submit/{session_name}",
                                    params={"request": prompt}).json()
                with st.chat_message("assistant"):
                    st.markdown(res)

        messages = requests.get(
            f"{BACKEND_URL}/api/v1/chat/history/{session_name}").json()
