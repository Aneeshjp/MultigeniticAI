import sqlite3
import os

def init_users_table():
    # Get the absolute path to the database
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sustainable_farming.db'))
    
    # Create the database directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to the database and create the users table
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        # Drop the existing users table if it exists
        cursor.execute('DROP TABLE IF EXISTS users')
        
        # Create the users table with the correct schema
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                farm_name TEXT,
                profile_picture TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Commit the changes
        conn.commit()
        
        print("Users table has been initialized successfully!")

if __name__ == "__main__":
    init_users_table()