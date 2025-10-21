import sqlite3
from datetime import datetime

# Create database connection
conn = sqlite3.connect('data/users.db')
cursor = conn.cursor()

# --- TABLE OPERATING SYSTEMS ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS OS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birthday DATE,
    phone TEXT,
    location TEXT NOT NULL,
    "Oper.sys" TEXT NOT NULL
)
''')

# --- TABLE USERS ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS USERS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    "Oper.sys" TEXT NOT NULL
)
''')

# --- MAIN FUNCTION ---
def main():
    print('=== Welcome ===\n=== Auth ===')
    first_name = input('Your name: ')
    last_name = input('Your last name: ')
    birthday = input('Your birthday: ')
    phone = input('Your phone number: ')
    location = input('Your location: ')
    oper_sys = input('Your OS: ')

    try:
        cursor.execute('''INSERT INTO OS 
                       (first_name, last_name, birthday, phone, location, "Oper.sys") 
                       VALUES (?, ?, ?, ?, ?, ?)''', 
                       (first_name, last_name, birthday, phone, location, oper_sys))

        cursor.execute('''INSERT INTO USERS 
                       (first_name, last_name, phone, "Oper.sys") 
                       VALUES (?, ?, ?, ?)''', 
                       (first_name, last_name, phone, oper_sys))
        
        conn.commit()
        print("Registration successful!")
        print("\n--- All Users in OS Table ---")
        cursor.execute('SELECT * FROM OS')
        for row in cursor.fetchall():
            print(row)
            
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        
main()
