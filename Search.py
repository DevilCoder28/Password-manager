import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import json
import os

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.resizable(False, False)
        self.root.config(bg="#7091E6")

        self.load_passwords()

        self.create_widgets()

        # Center the window on the screen
        self.center_window()

    def load_passwords(self):
        try:
            if os.path.getsize("passwords.json") == 0:
                self.passwords = {}
            else:
                with open("passwords.json", "r") as f:
                    self.passwords = json.load(f)
        except FileNotFoundError:
            self.passwords = {}

    def save_passwords(self):
        with open("passwords.json", "w") as f:
            json.dump(self.passwords, f)

    def get_key(self):
        if not os.path.exists("key.txt"):
            key = Fernet.generate_key()
            with open("key.txt", "wb") as key_file:
                key_file.write(key)
        else:
            with open("key.txt", "rb") as key_file:
                key = key_file.read()
        return key

    def search_password(self):
        user = self.user_entry.get().strip().lower()
        
        if user == "":
            messagebox.showerror("Error", "Please enter a username")
        else:
            passwords = self.passwords
            if user in passwords:
                try:
                    key = self.get_key()
                    cipher_suite = Fernet(key)
                    encrypted_password = passwords[user].encode()
                    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
                    self.pass_entry.delete(0, tk.END)
                    self.pass_entry.insert(0, decrypted_password)
                except Exception as e:
                    messagebox.showerror("Error", f"Decryption failed: {str(e)}")
            else:
                messagebox.showerror("Error", "Username not found")
        
        self.user_entry.delete(0, tk.END)

    def create_widgets(self):
        head = tk.Label(self.root, text="Password Manager", font=("Arial", 24), relief="raised", background="#7091E6")
        head.grid(row=0, column=0, columnspan=2, pady=25)

        image = Image.open("add2.png")
        resized_image = image.resize((180, 160))
        photo = ImageTk.PhotoImage(resized_image)
        label = tk.Label(self.root, image=photo, borderwidth=0, highlightthickness=0)
        label.image = photo
        label.grid(row=1, column=0, padx=80, columnspan=2, pady=20)

        user_label = tk.Label(self.root, text="Username/Website", anchor="w", font=("Arial", 15), background="#7091E6")
        user_label.grid(row=2, column=0, padx=20, pady=15, sticky="w")

        self.user_entry = tk.Entry(self.root, width=40, highlightthickness=1, background="#7091E6", foreground="black")
        self.user_entry.grid(row=3, column=0, padx=20, pady=2, columnspan=2)

        pass_label = tk.Label(self.root, text="Password", anchor="w", font=("Arial", 15), background="#7091E6")
        pass_label.grid(row=4, column=0, padx=20, pady=15, sticky="w")

        self.pass_entry = tk.Entry(self.root, width=40, highlightthickness=1, background="#7091E6", foreground="white", show="*")
        self.pass_entry.grid(row=5, column=0, padx=20, pady=2, columnspan=2)

        search_button = tk.Button(self.root, text="SEARCH", width=15, background="green", foreground="white", font=("Arial", 15), command=self.search_password)
        search_button.place(relx=0.48, rely=0.85, anchor="center")

    def center_window(self):
        width = 350
        height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()
