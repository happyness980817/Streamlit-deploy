import streamlit as st

st.title('Welcome to my CounsellingGPT pretotype webpage!')

# Initialize session state for storing chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User identification
user_name = st.text_input("Enter your username:", key="username")

# Chat input
user_message = st.text_input("Type your message here:", key="message")

# Button to send message
if st.button('Send'):
    # Append the username along with the message
    st.session_state['chat_history'].append((user_name, user_message))

# Display chat history
st.write("Chat History:")
for name, message in st.session_state['chat_history']:
    st.text(f"{name}: {message}")



    