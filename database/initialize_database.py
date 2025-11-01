import sqlite3
import os

def initialize_database():
    """Initialize all database tables required for the application."""
    # Get the absolute path to the database
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sustainable_farming.db'))
    
    # Create the database directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to the database and create all tables
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        # Create recommendations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS recommendations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                crop TEXT,
                score REAL,
                rationale TEXT,
                carbon_score REAL,
                water_score REAL,
                erosion_score REAL,
                timestamp TEXT
            )
        ''')
        
        # Create sustainability_scores table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sustainability_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                water_score REAL,
                fertilizer_use REAL,
                rotation INTEGER,
                score REAL
            )
        ''')
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                farm_name TEXT,
                profile_picture TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Commit all changes
        conn.commit()
        
        print("All database tables have been initialized successfully!")

if __name__ == "__main__":
    initialize_database()