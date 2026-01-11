# libraries
import sqlite3 # data base
import hashlib # hashing passwords

from datetime import datetime 

# variables
data_base_file = 'users.db' # file  data base
log_file = 'logging.txt' # file logging

# database connect
def init_db(): 
    conn = sqlite3.connect(data_base_file) # database connection
    cursor = conn.cursor() # cursor connection
    
    # create a table if he don't found
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    ''')
    conn.commit()
    return conn

# logging
def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {message}"
    
    # save in file
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')
    
    print(log_entry)  # print in console

# hashing password
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# new user registr
def register_user(conn, login, email, password):
    cursor = conn.cursor()
    try:
        password_hash = hash_password(password)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
        INSERT INTO users (login, email, password_hash, created_at)
        VALUES (?, ?, ?, ?)
        ''', (login, email, password_hash, created_at))
        
        conn.commit()
        log_action(f"Успешная регистрация: {login}")
        return True
    except sqlite3.IntegrityError as e:
        if 'UNIQUE constraint failed: users.login' in str(e):
            log_action(f"Ошибка регистрации: Логин {login} уже существует")
        elif 'UNIQUE constraint failed: users.email' in str(e):
            log_action(f"Ошибка регистрации: Email {email} уже используется")
        return False
    except Exception as e:
        log_action(f"Ошибка регистрации: {str(e)}")
        return False

# auth users
def login_user(conn, login, password):
    cursor = conn.cursor()
    try:
        password_hash = hash_password(password)
        
        cursor.execute('''
        SELECT login FROM users 
        WHERE login = ? AND password_hash = ?
        ''', (login, password_hash))
        
        result = cursor.fetchone()
        if result:
            log_action(f"Успешный вход: {login}")
            return True
        else:
            log_action(f"Неудачная попытка входа: {login}")
            return False
    except Exception as e:
        log_action(f"Ошибка авторизации: {str(e)}")
        return False

# main func
def main():
    conn = init_db()
    log_action("Система авторизации запущена")
    
    while True:
        print("\n1. Регистрация")
        print("2. Вход")
        print("3. Выход")
        print()
        choice = input("Выберите действие: ")
        
        if choice == '1':
            print()
            login = input("Введите логин: ")
            email = input("Введите email: ")
            password = input("Введите пароль: ")
            
            if register_user(conn, login, email, password):
                print("Регистрация успешна!")
            else:
                print("Ошибка регистрации")
        
        elif choice == '2':
            print()
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            
            if login_user(conn, login, password):
                print("Авторизация успешна!")
            else:
                print("Неверный логин или пароль")
        
        elif choice == '3':
            print()
            log_action("Завершение работы системы")
            conn.close()
            break

        elif choice == 'dead_inside':
            for i in range(1000, 0, -7): 
                print(i - 7)
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()