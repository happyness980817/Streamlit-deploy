import streamlit as st

st.title('Welcome to my CounsellingGPT pretotype webpage!')

# Initialize session state for storing chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to handle message sending
def send_message(username, key):
    user_message = st.session_state[key]
    if user_message:  # Only send non-empty messages
        st.session_state['chat_history'].append((username, user_message))
        st.session_state[key] = ""  # Clear the input box after sending

# Display the chat history
def display_chat_history():
    st.write("Chat History:")
    for name, message in st.session_state['chat_history']:
        st.text(f"{name}: {message}")

# User input for Counselor
st.text_input("Counselor, type your message here:", 
              key="counselor_message", 
              on_change=send_message, 
              args=("Counselor", "counselor_message"), 
              placeholder="Type here and press Enter to send")

# User input for Client
st.text_input("Client, type your message here:", 
              key="client_message", 
              on_change=send_message, 
              args=("Client", "client_message"), 
              placeholder="Type here and press Enter to send")

# Display the chat history
display_chat_history()