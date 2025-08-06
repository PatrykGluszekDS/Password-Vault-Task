import sqlite3
import bcrypt

class AuthManager:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_auth_table()

    def create_auth_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS master_password (
            id INTEGER PRIMARY KEY,
            password_hash TEXT NOT NULL
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def set_master_password(self, password):
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.conn.execute('DELETE FROM master_password')  # ensure only one master password
        self.conn.execute('INSERT INTO master_password (id, password_hash) VALUES (?, ?)', (1, password_hash))
        self.conn.commit()

    def verify_master_password(self, password):
        cursor = self.conn.execute('SELECT password_hash FROM master_password WHERE id = 1')
        result = cursor.fetchone()
        if not result:
            return False
        return bcrypt.checkpw(password.encode(), result[0])

    def close(self):
        self.conn.close()
