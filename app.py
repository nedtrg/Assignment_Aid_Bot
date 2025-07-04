import streamlit as st
import time
import os
import openai
from spacy.matcher import Matcher
import spacy
from helper import homework_helper_bot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set Streamlit page configuration
st.set_page_config(page_title="Interactive type Chatbot", page_icon="🤖", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main container to handle layout */
    body {
        margin: 0;
        height: 100vh;
        display: flex;
        flex-direction: column;
    }
    .main-content {
        flex: 1;
        overflow-y: auto;
        padding: 20px;
        box-sizing: border-box;
    }
    .user-input {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: black;
        z-index: 1000;
        display: flex;
        justify-content: center;
        padding: 10px;
        box-sizing: border-box;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        width: 700px;
    }
    .title-container {
        text-align: center;
        position: fixed;
        width: 100%;
        background-color: black;
        z-index: 10;
        top: 0;
        padding: 50px 0px 0px 0px;
        box-sizing: border-box;
    }
    .title {
        text-align: center;
        font-family: Copperplate, Papyrus;
        font-weight: bold;
        color: cyan;
        font-size: 60px;
    }
    .subtitle {
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
        color: #a6a6a6;
    }
    .stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton > button:hover {
        background-color: black;
        border: 2px solid #4CAF50;
        color:white;
    }
    .stButton > button:nth-child(2) {
        background-color: red;
        color: yellow;
        border: none;
        padding: 10px 24px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton > button:nth-child(2):hover {
        background-color: black;
        border: 2px solid red;
        color:white;
    }
    .message-container {
        border: 1px solid #e0e0e0;
        padding: 15px;
        border-radius: 10px;
        background-color: #ffffff;
        margin: 10px;
        width:90%;
    }
    .message-container-user {
        border: 1px solid gray;
        padding: 15px;
        border-radius: 10px;
        background-color: #a6a6a6;
        margin: 20px 150px;
        width:90%;
    }
    .message-user {
        color: black;
        background-color: #a6a6a6;
        text-decoration-thickness: 4px;
    }
    .message-bot {
        color: #3C3C3C;
        text-decoration-thickness: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='title-container'><div><h1 class='title'>CYD Bot</h1></div><div><h3 class='subtitle'>Your Personal Homework Helper</h3></div></div>", unsafe_allow_html=True)

# Initialize session state to store chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

def handle_message(user_message):
    bot_response = homework_helper_bot(user_message)
    st.session_state.messages.append({"role": "user", "content": user_message})
    # Simulate typing effect
    with st.spinner("Bot is typing..."):
        time.sleep(1)
    st.session_state.messages.append({"role": "bot", "content": bot_response})

st.markdown("<div class='main-content'>", unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.markdown(f'<div class="message-container"><div class="message-bot"><strong>Bot :</strong> Hello!! How can I help you today? </div></div>', unsafe_allow_html=True)

# Display chat messages with improved styling
for message_data in st.session_state.messages:
    if message_data["role"] == "user":
        st.markdown(f'<div class="message-container-user"><div class="message-user"><strong>You  :</strong>{message_data["content"]}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message-container"><div class="message-bot"><strong>Bot  :</strong>{message_data["content"]}</div></div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='user-input'>", unsafe_allow_html=True)
user_input = st.text_input("You: ", key="input_text", placeholder="Type your message here...")

if st.button("Send", key="send_button"):
    if user_input:
        handle_message(user_input)
        st.experimental_rerun()      
if st.button("Clear", key="clear_button"):
    st.session_state.messages=[]
    st.experimental_rerun()      
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
