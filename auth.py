import sqlite3
from database import get_db_connection, hash_password
from user import User
from admin import Admin

class Auth:
    @staticmethod
    def register(username: str, password: str, role: str):
        if role not in ["user", "admin"]:
            print("Invalid role! Must be 'user' or 'admin'.")
            return
        
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                        (username, hash_password(password), role))
            conn.commit()
            print(f"User {username} registered successfully as {role}.")
        except sqlite3.IntegrityError:
            print("Username already exists!")
        
        conn.close()

    @staticmethod
    def login(username: str, password: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT role FROM users WHERE username=? AND password=?", 
                    (username, hash_password(password)))
        user = cursor.fetchone()
        
        conn.close()
        
        if user:
            print(f"Login successful! Welcome, {username}. Role: {user[0]}")
            return Admin(username) if user[0] == "admin" else User(username)
        else:
            print("Invalid credentials!")
            return None
