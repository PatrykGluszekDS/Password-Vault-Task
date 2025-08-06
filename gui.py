import tkinter as tk
from tkinter import messagebox, simpledialog
from password_manager import PasswordManager
from auth import AuthManager
from password_generator import PasswordGenerator

class PasswordGUI:
    def __init__(self):
        self.auth = AuthManager()
        self.pm = PasswordManager()

        self.root = tk.Tk()
        self.root.title("Password Manager")
        self.root.geometry("600x400")

        self.login_screen()

    def login_screen(self):
        password = simpledialog.askstring("Master Password", "Enter master password:", show='*')
        if not self.auth.verify_master_password(password):
            messagebox.showerror("Access Denied", "Invalid master password")
            self.root.destroy()
            return

        self.build_main_ui()

    def build_main_ui(self):
        self.entries_frame = tk.Frame(self.root)
        self.entries_frame.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = tk.Button(self.root, text="Refresh", command=self.load_credentials)
        self.refresh_button.pack()

        self.add_button = tk.Button(self.root, text="Add New", command=self.add_credential)
        self.add_button.pack()

        self.load_credentials()

    def load_credentials(self):
        for widget in self.entries_frame.winfo_children():
            widget.destroy()

        records = self.pm.get_credentials()
        for record in records:
            label = tk.Label(self.entries_frame, text=f"{record['site']} | {record['username']} | {record['password']}")
            label.pack()

    def add_credential(self):
        site = simpledialog.askstring("Input", "Site:")
        username = simpledialog.askstring("Input", "Username:")
        password = simpledialog.askstring("Input", "Password (leave blank to generate):")

        if not password:
            generator = PasswordGenerator(length=16)
            password = generator.generate()
            messagebox.showinfo("Generated Password", password)

        self.pm.add_credential(site, username, password)
        self.load_credentials()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = PasswordGUI()
    gui.run()
