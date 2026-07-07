import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# configure the gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Select the model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit page config
st.set_page_config(page_title="Ducat Chatbot", page_icon="🤖")
st.title("Chatbot_S 🤖")

# initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# chat input
if prompt := st.chat_input("Ask me anything!"):
    # add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # generate response from the model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)   # Fixed typo
                reply = response.text
                st.markdown(reply)
            except Exception as e:
                st.error(f"Error: {e}")
                reply = "Sorry, I encountered an error."

    # add assistant response to history
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

