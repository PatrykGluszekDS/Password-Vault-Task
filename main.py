from password_manager import PasswordManager

pm = PasswordManager()
pm.add_credential("gmail.com", "user@gmail.com", "my_secure_pass", "Personal email")
print(pm.get_credentials())
pm.close()
