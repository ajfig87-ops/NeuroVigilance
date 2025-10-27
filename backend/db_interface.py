import sqlite3
from datetime import datetime
import os

class DatabaseInterface:
    def __init__(self, db_path='neurosentinel.db'):
        self.db_path(self) = db_path
        self._initialize_database()

    def _initialize_database(self):
        conn = sqlite3.connect(self.db_pth)
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS redacted_texts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_text TEXT NOT NULL,
                redacted_text TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def save_redacted_entry(self, original, redacted):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        timestamp = datetime.utcnow().isoformat()
        cursor.execute("""
            INSERT INTO redacted_texts (original_text, redacted_text, timestamp)
            VALUES (?, ?, ?)
        """, (original, redacted, timestamp))

        conn.commit()
        conn.close()

    def get_all_entries(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, original_text, redacted_text, timestamp FROM redacted_texts")
        rows = cursor.fetchall()

        conn.close()
        return rows
    
    def delete_entry(self, entry_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM redacted_texts WHERE id = ?", (entry_id))

        conn.commit()
        conn.close()

        