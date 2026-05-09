import streamlit as st
import random

st.set_page_config(page_title="ChatGPT-like App")

st.title("🤖 ChatGPT-like App")
st.write("Simple chatbot using Streamlit without any LLM or API.")

if "messages" not in st.session_state:
    st.session_state.messages = []

def generate_response(user_message):
    user_message = user_message.lower()

    if "hello" in user_message:
        return "Hi there! 👋"

    elif "how are you" in user_message:
        return "I'm just a local Python function, but I'm doing great!"

    elif "your name" in user_message:
        return "I'm a Streamlit chatbot."

    elif "bye" in user_message:
        return "Goodbye! Have a nice day."

    else:
        random_replies = [
            "Interesting question!",
            "Tell me more.",
            "I understand.",
            "That's cool!",
            "Can you explain further?"
        ]

        return random.choice(random_replies)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    response = generate_response(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)