import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import json

def load_passwords():
    try:
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}
    return passwords

def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)

def update_password():
    user = user_entry.get().lower()
    password = pass_entry.get()
    
    if user == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password")
    else:
        passwords = load_passwords()
        if user in passwords:
            with open("key.txt", "r") as key_file:
                key = Fernet(key_file.read().encode())
            encrypted_password = key.encrypt(password.encode()).decode()
            passwords[user] = encrypted_password
            save_passwords(passwords)
            user_entry.delete(0, tk.END)
            pass_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Password updated successfully")
        else:
            messagebox.showerror("Error", "Username not found")


root = tk.Tk()
root.title("Password Manager")
width = 350
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')  
root.resizable(False, False)  
root.config(bg="#7091E6")

head = tk.Label(root, text="Update Passwords", font=("Arial", 24), relief="raised", background="#7091E6")
head.grid(row=0, column=0, columnspan=4, pady=25)

image = Image.open("add2.png")
resized_image = image.resize((170, 170))  
photo = ImageTk.PhotoImage(resized_image)
label = tk.Label(root, image=photo, borderwidth=0, highlightthickness=0)
label.image = photo  
label.grid(row=1, column=0, padx=80, columnspan=2, pady=20)

user = tk.Label(root, text="Username/Website", anchor="w", font=("Arial", 15), background="#7091E6")
user.grid(row=2, column=0, padx=20, pady=15, sticky="w")

user_entry = tk.Entry(root, width=40, highlightthickness=1, background="#7091E6", foreground="black")
user_entry.grid(row=3, column=0, padx=0, pady=2)

pass1 = tk.Label(root, text="Password", anchor="w", font=("Arial", 15), background="#7091E6")
pass1.grid(row=4, column=0, padx=20, pady=15, sticky="w")

pass_entry = tk.Entry(root, width=40, highlightthickness=1, background="#7091E6", foreground="black")
pass_entry.grid(row=5, column=0, padx=0, pady=2)

update_btn = tk.Button(root, text="Update", width=15, background="blue", foreground="white", font=("Arial", 15), command=update_password)
update_btn.place(relx=0.48, rely=0.85, anchor="center")


root.mainloop()
