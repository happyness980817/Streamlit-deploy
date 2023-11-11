import streamlit as st

st.title('Welcome to my CounsellingGPT pretotype webpage!')

# Initialize session state for storing chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to display the chat history
def display_chat_history():
    st.write("Chat History:")
    for name, message in st.session_state['chat_history']:
        st.text(f"{name}: {message}")

# Function to handle message sending
def send_message(username, user_message):
    if user_message:  # Only send non-empty messages
        st.session_state['chat_history'].append((username, user_message))

# User input for Counselor
counselor_message = st.text_input("Counselor, type your message here:", key="counselor_message")
if st.button('Send (Counselor)', key="send_counselor"):
    send_message("Counselor", counselor_message)

# User input for Client
client_message = st.text_input("Client, type your message here:", key="client_message")
if st.button('Send (Client)', key="send_client"):
    send_message("Client", client_message)

# Display the chat history
display_chat_history()
