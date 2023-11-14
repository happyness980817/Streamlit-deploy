import streamlit as st

st.title('Welcome to CounsellingGPT!')
st.subheader('This is merely a pretoype version.')

# # Initialize session state for storing chat
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# # Function to handle message sending
# def send_message(username, key):
#     user_message = st.session_state[key]
#     if user_message:  # Only send non-empty messages
#         st.session_state['chat_history'].append((username, user_message))
#         st.session_state[key] = ""  # Clear the input box after sending

# # Display the chat history
# def display_chat_history():
#     st.write("Chat History:")
#     for name, message in st.session_state['chat_history']:
#         st.text(f"{name}: {message}")

# # User input for Counselor
# st.text_input("Counselor, type your message here:", 
#               key="counselor_message", 
#               on_change=send_message, 
#               args=("Counselor", "counselor_message"), 
#               placeholder="Type here and press Enter to send")

# # User input for Client
# st.text_input("Client, type your message here:", 
#               key="client_message", 
#               on_change=send_message, 
#               args=("Client", "client_message"), 
#               placeholder="Type here and press Enter to send")

# # Display the chat history
# display_chat_history()


import streamlit as st
import sqlite3

# Singleton Pattern for Database Management
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls.connection = sqlite3.connect('chat_history.db', check_same_thread=False)
            cls.cursor = cls.connection.cursor()
            cls.setup_database()
        return cls._instance

    @staticmethod
    def setup_database():
        Database._instance.cursor.execute('''CREATE TABLE IF NOT EXISTS messages 
                                             (username TEXT, message TEXT)''')
        Database._instance.connection.commit()

    @staticmethod
    def save_message(username, message):
        Database._instance.cursor.execute("INSERT INTO messages VALUES (?, ?)", (username, message))
        Database._instance.connection.commit()

    @staticmethod
    def load_messages():
        Database._instance.cursor.execute("SELECT username, message FROM messages")
        return Database._instance.cursor.fetchall()

# Function to handle message sending
def send_message(username, key):
    user_message = st.session_state[key]
    if user_message:  # Only send non-empty messages
        db.save_message(username, user_message)
        st.session_state['chat_history'].append((username, user_message))
        st.session_state[key] = ""  # Clear the input box after sending

# Display the chat history
def display_chat_history():
    st.write("Chat History:")
    for name, message in st.session_state['chat_history']:
        st.text(f"{name}: {message}")

# Initialize the database
db = Database()

# Initialize session state for storing chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = db.load_messages()

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
