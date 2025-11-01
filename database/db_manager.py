import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.initialize_tables()
    
    def initialize_tables(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
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
            
            conn.commit()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)