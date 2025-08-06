from db_manager import DatabaseManager
from crypto_utils import CryptoUtils

class PasswordManager:
    def __init__(self):
        self.db = DatabaseManager()
        self.crypto = CryptoUtils()

    def add_credential(self, site, username, password, notes=""):
        encrypted_pw = self.crypto.encrypt(password)
        query = '''
        INSERT INTO credentials (site, username, password, notes)
        VALUES (?, ?, ?, ?)
        '''
        self.db.conn.execute(query, (site, username, encrypted_pw, notes))
        self.db.conn.commit()

    def get_credentials(self):
        query = 'SELECT id, site, username, password, notes FROM credentials'
        cursor = self.db.conn.execute(query)
        records = []
        for row in cursor.fetchall():
            decrypted_pw = self.crypto.decrypt(row[3])
            records.append({
                "id": row[0],
                "site": row[1],
                "username": row[2],
                "password": decrypted_pw,
                "notes": row[4]
            })
        return records

    def close(self):
        self.db.close()

    def update_credential(self, record_id, site, username, password, notes=""):
        if not all([site, username, password]):
            raise ValueError("Site, username, and password must not be empty.")
        
        encrypted_pw = self.crypto.encrypt(password)
        query = '''
        UPDATE credentials
        SET site = ?, username = ?, password = ?, notes = ?
        WHERE id = ?
        '''
        self.db.conn.execute(query, (site, username, encrypted_pw, notes, record_id))
        self.db.conn.commit()

    def delete_credential(self, record_id):
        query = 'DELETE FROM credentials WHERE id = ?'
        self.db.conn.execute(query, (record_id,))
        self.db.conn.commit()

    def export_backup(self, filename='backup.txt'):
        records = self.get_credentials()
        lines = []
        for r in records:
            line = f"Site: {r['site']}\nUsername: {r['username']}\nPassword: {r['password']}\nNotes: {r['notes']}\n---\n"
            lines.append(line)

        plaintext_backup = ''.join(lines)
        encrypted_backup = self.crypto.encrypt(plaintext_backup)

        with open(filename, 'w') as f:
            f.write(encrypted_backup)

        print(f"Encrypted backup saved to: {filename}")

    def add_credential(self, site, username, password, notes=""):
        if not all([site, username, password]):
            raise ValueError("Site, username, and password must be provided.")
        try:
            encrypted_pw = self.crypto.encrypt(password)
            query = '''
            INSERT INTO credentials (site, username, password, notes)
            VALUES (?, ?, ?, ?)
            '''
            self.db.conn.execute(query, (site, username, encrypted_pw, notes))
            self.db.conn.commit()
        except Exception as e:
            print("Error adding credential:", e)
