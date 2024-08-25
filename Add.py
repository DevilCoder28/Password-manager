import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import json
import os

def load_passwords():
    try:
        if os.path.getsize("passwords.json") == 0:
            passwords = {}
        else:
            with open("passwords.json", "r") as f:
                passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}
    return passwords

def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)

def get_key():
    key_file = "key.txt"
    if not os.path.exists(key_file):
        # Generate a new key if key file doesn't exist
        key = Fernet.generate_key()
        with open(key_file, "wb") as key_file:
            key_file.write(key)
    else:
        # Read the key from the key file
        with open(key_file, "rb") as key_file:
            key = key_file.read()
    return key


def add_password(user_entry, pass_entry, passwords):
    user = user_entry.get().lower()
    pass1 = pass_entry.get()
    if user == "" or pass1 == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        if user in passwords:
            messagebox.showerror("Error", "Username already exists. Please choose another one.")
            return
        key = get_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(pass1.encode())
        passwords[user] = cipher_text.decode()
        save_passwords(passwords)
        user_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Password added successfully")


def create_widgets(root, passwords):
    head = tk.Label(root, text="Password Manager", font=("Arial", 24), relief="raised", background="#7091E6")
    head.grid(row=0, column=0, columnspan=2, pady=25)

    image = Image.open("add2.png")
    resized_image = image.resize((180, 160))
    photo = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root, image=photo, borderwidth=0, highlightthickness=0)
    label.image = photo
    label.grid(row=1, column=0, padx=80, columnspan=2, pady=20)

    user = tk.Label(root, text="Username/Website", anchor="w", font=("Arial", 15), background="#7091E6")
    user.grid(row=2, column=0, padx=20, pady=15, sticky="w")

    user_entry = tk.Entry(root, width=40, highlightthickness=1, background="#7091E6", foreground="black")
    user_entry.grid(row=3, column=0, padx=0, pady=2, columnspan=2)

    pass1 = tk.Label(root, text="Password", anchor="w", font=("Arial", 15), background="#7091E6")
    pass1.grid(row=4, column=0, padx=20, pady=15, sticky="w")

    pass_entry = tk.Entry(root, width=40, highlightthickness=1, background="#7091E6", foreground="white", show="*")
    pass_entry.grid(row=5, column=0, padx=0, pady=2, columnspan=2)

    add = tk.Button(root, text="ADD", width=15, background="blue", foreground="white", font=("Arial", 15), command=lambda: add_password(user_entry, pass_entry, passwords))
    add.place(relx=0.48, rely=0.85, anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry("350x600")
    root.resizable(False, False)
    root.config(bg="#7091E6")

    passwords = load_passwords()

    create_widgets(root, passwords)

    width = 350
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    # Set the position of the window
    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    root.mainloop()