# Password Vault

## Description
A secure password manager that uses encryption and a local database (`SQLite`) to store credentials securely with GUI. The program can be written in C++ if you're more comfortable working with it

## Getting Started
1. Clone this repository or download the files.
2. Install required packages if necessary.

Keep in mind that the code must be written in OOP.

## Tasks
- Research cryptography or fernet and SQLite. Plan database schema: site, username, password, notes.
- Implement database and function to add credentials. Encrypt passwords before storing.
- Create function to retrieve credentials (decrypt passwords).- Document the code.
- Add edit and delete features. Validate inputs.
- Add master password that unlocks access to vault.
- Add password generator (random strong passwords).
- Build a CLI or tkinter GUI: list entries, search, and view decrypted passwords.
- Add export to encrypted .txt file for backup.
- Add error handling, fix bugs, and test with mock data.
- Final testing. Create README with instructions and screenshots. Submit as Git repo.

## Step 1: Database Setup

Used SQLite for local data storage. The `credentials` table stores:

- `id`
- `site`
- `username`
- `password` (encrypted)
- `notes`

## Step 2: Encryption Utilities

Used `cryptography.fernet` for encrypting and decrypting passwords.

### Key Features:
- Secure symmetric encryption
- Keys are stored in `secret.key`
- Encapsulation in `CryptoUtils` class

### Usage Example:

```python
crypto = CryptoUtils()
encrypted = crypto.encrypt("mypassword")
decrypted = crypto.decrypt(encrypted)
```

---

## Step 3: Password Manager Class

The `PasswordManager` class ties everything together:
- Connects to SQLite DB
- Encrypts passwords before storing
- Decrypts passwords when retrieving

### Example:

```python
pm = PasswordManager()
pm.add_credential("gmail.com", "user", "mypassword", "notes")
records = pm.get_credentials()
print(records)
pm.close()
```

---

## Step 4: CRUD Operations

In addition to adding and viewing credentials, there is possibility of updating or deleting them.

### Update:

```python
pm.update_credential(1, "github.com", "user", "newpassword", "updated note")
```

---

## Step 5: Master Password System

Used `bcrypt` to hash and verify a master password.

### Key Features:
- Master password required before using the vault
- Stored securely in the `master_password` table

### Usage:

```python
auth = AuthManager()
auth.set_master_password("your_password")  # only once
auth.verify_master_password("your_password")  # returns True or False
```

---

## Step 6: Password Generator

Used `PasswordGenerator` class to create secure passwords.

### Features:
- Customizable length (default = 12)
- Optional digits and symbols

### Example:

```python
gen = PasswordGenerator(length=16)
secure_pw = gen.generate()
print(secure_pw)
```

---

## Step 7: Tkinter GUI

A basic graphical interface was implemented using Tkinter.

### Features:
- Master password login
- Display credentials
- Add new credentials
- Generate secure passwords

### Preview:

```bash
python gui.py
```

---

## Step 8: Encrypted Backup Export

It is possible to export all stored credentials to an encrypted `.txt` file.

### Usage:

```python
pm.export_backup("my_backup.txt")
```

---

## Step 9: Error Handling & Mock Testing

Added error handling and tested edge cases like:

- Missing required fields
- Decryption failure
- Invalid database operations

### Mock Tests (`test_mock.py`):
- Adds and updates sample data
- Deletes an entry
- Exports backup

---

## Files Overview

- `db_manager.py` – handles SQLite setup
- `crypto_utils.py` – encryption utilities
- `password_manager.py` – logic for managing credentials
- `auth.py` – master password management
- `password_generator.py` – password generator class
- `gui.py` – Tkinter GUI
- `test_mock.py` – testing script