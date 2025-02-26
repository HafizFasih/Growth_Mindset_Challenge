import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import os
# Configure API key (Replace with your actual key)
_: bool = load_dotenv(find_dotenv())

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def chat_with_gemini(prompt):
    """Generates a response from the Gemini AI model."""
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# Initialize session state for chat history
if "chat_sessions" not in st.session_state:
    st.session_state["chat_sessions"] = []
if "current_chat" not in st.session_state:
    st.session_state["current_chat"] = []

def new_chat():
    """Starts a new chat session and adds the first user prompt as a label."""
    if st.session_state["current_chat"]:
        first_message = st.session_state["current_chat"][0]["content"] if st.session_state["current_chat"] else "New Chat"
        st.session_state["chat_sessions"].append({"label": first_message, "messages": st.session_state["current_chat"]})
    st.session_state["current_chat"] = []

# Sidebar for chat history and new chat button
with st.sidebar:
    st.title("🤖 AI Chatbot")
    if st.button("➕ New Chat"):
        new_chat()
    st.subheader("🗂 Chat History")
    for i, session in enumerate(st.session_state["chat_sessions"]):
        if session:
            if st.button(f"🔹 {session['label']}", key=f"chat_{i}"):
                st.session_state["current_chat"] = session["messages"]
    st.divider()
    st.caption("Made by Muhammad Fasih ❤️")

# Main chat interface
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>AI Chatbot</h1>", unsafe_allow_html=True)

# Display chat history
for message in st.session_state["current_chat"]:
    with st.chat_message(message["role"]):
        st.markdown(f"**{message['role'].capitalize()}:** {message['content']}")

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Display user message
    st.session_state["current_chat"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(f"**User:** {user_input}")

    # Generate AI response
    with st.spinner("Thinking..."):
        bot_response = chat_with_gemini(user_input)
    
    st.session_state["current_chat"].append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(f"**Assistant:** {bot_response}")