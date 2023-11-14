import sqlite3

def read_from_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM messages")
    data = c.fetchall()
    
    for row in data:
        print(row)

    conn.close()

read_from_db()
