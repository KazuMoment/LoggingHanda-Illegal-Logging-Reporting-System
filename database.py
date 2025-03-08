import sqlite3
import hashlib

DB_FILE = "logging_reports.db"

def get_db_connection():
    return sqlite3.connect(DB_FILE)

def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        username TEXT UNIQUE, 
                        password TEXT, 
                        role TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS reports (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        location TEXT, 
                        description TEXT, 
                        reporter TEXT,
                        status TEXT DEFAULT 'pending')''')
    
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()