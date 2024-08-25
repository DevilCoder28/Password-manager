import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess

def add_password():
    e1.delete(0, tk.END)
    e1.insert(0, "Add Password")

def search_password():
    e1.delete(0, tk.END)
    e1.insert(0, "Search Password")

def update_password():
    e1.delete(0, tk.END)
    e1.insert(0, "Update Password")

def delete_password():
    e1.delete(0, tk.END)
    e1.insert(0, "Delete Password")

def generate_password():
    e1.delete(0, tk.END)
    e1.insert(0, "Generate Password")

def show_password():
    e1.delete(0, tk.END)
    e1.insert(0, "Show Password")

def done():
    ans = e1.get()
    if ans == "Add Password":
        try:
            subprocess.Popen(["python", "Add.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "Add.py not found.")
    elif ans == "Search Password":
        try:
            subprocess.Popen(["python", "Search.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "Add.py not found.")
    elif ans == "Delete Password":
        try:
            subprocess.Popen(["python", "Delete.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "Add.py not found.")
    elif ans == "Update Password":
        try:
            subprocess.Popen(["python", "Update.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "Add.py not found.")
    elif ans == "Generate Password":
        try:
            subprocess.Popen(["python", "generate.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "Add.py not found.")
    elif ans == "Show Password":
        try:
            subprocess.Popen(["python", "showall.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "Add.py not found.")
    else:
        messagebox.showerror("Error", "Please select an option")

def close():
    root.quit()

root = tk.Tk()

width = 350
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
root.title("Password Manager")
root.configure(bg="#f2f2f2")
try:
    logo = tk.PhotoImage(file="logo.png")
    root.iconphoto(False, logo)
except tk.TclError:
    pass
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", background="#f2f2f2", foreground="black", font=("Helvetica", 12))
style.configure("TButton", background="#f2f2f2", foreground="blue", font=("Helvetica", 12, "bold"))
style.configure("TEntry", background="white", foreground="black", font=("Helvetica", 12))

try:
    image = Image.open("label.jpg")
    image = image.resize((250, 100))
    photo = ImageTk.PhotoImage(image)
    title_label = ttk.Label(root, image=photo, background="#f2f2f2")
    title_label.image = photo
    title_label.pack(pady=20)
except FileNotFoundError:
    title_label = ttk.Label(root, text="Image not found", background="#AC8968", foreground="white", font=("Helvetica", 12))
    title_label.pack(pady=20)

e1 = tk.Entry(root, width=16, borderwidth=4, font=('Arial', 24),
              highlightbackground="gold", highlightcolor="gold", highlightthickness=2, background='#5f9989')
e1.pack(pady=10)

# Frame for buttons row 1 (Add and Search)
button_frame1 = tk.Frame(root, bg="#f2f2f2")
button_frame1.pack(pady=10)

button1 = ttk.Button(button_frame1, text="Add", width=15, style="TButton", command=add_password)
button1.pack(side="left", padx=5)

button2 = ttk.Button(button_frame1, text="Search", width=15, style="TButton", command=search_password)
button2.pack(side="left", padx=5)

# Frame for buttons row 2 (Update, Delete)
button_frame2 = tk.Frame(root, bg="#f2f2f2")
button_frame2.pack(pady=10)

button3 = ttk.Button(button_frame2, text="Update", width=15, style="TButton", command=update_password)
button3.pack(side="left", padx=5)

button4 = ttk.Button(button_frame2, text="Delete", width=15, style="TButton", command=delete_password)
button4.pack(side="left", padx=5)

# Frame for buttons row 3 (Generate, Show All)
button_frame3 = tk.Frame(root, bg="#f2f2f2")
button_frame3.pack(pady=10)

button5 = ttk.Button(button_frame3, text="Generate", width=15, style="TButton", command=generate_password)
button5.pack(side="left", padx=5)

button6 = ttk.Button(button_frame3, text="Show All", width=15, style="TButton", command=show_password)
button6.pack(side="left", padx=5)

# Frame for buttons row 4 (Ok and Close)
button_frame4 = tk.Frame(root, bg="#f2f2f2")
button_frame4.pack(pady=100)

ok_button = ttk.Button(button_frame4, text="Ok", width=15, style="TButton", command=done)
ok_button.pack(side="left", padx=5)

close_button = ttk.Button(button_frame4, text="Close", width=15, style="TButton", command=close)
close_button.pack(side="left", padx=5)

root.mainloop()
