import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def sign_up():
    userw = user.get()
    passw = password_entry.get()
    cpass = cpassword_entry.get()
    
    if userw=="" or passw =="":
        messagebox.showerror("Error", "All fields are required")
    elif passw != cpass:
        messagebox.showerror("Error", "Password does not match")
        
    else:
        with open('login.txt','w') as file:
            file.write(f"{{'{userw}': '{passw}'}}\n")
            messagebox.showinfo("Success", "Account created successfully")
            root.destroy()
            import sign


def back():
    root.destroy()
    import functions       

root = tk.Tk()
root.title("Password Manager")
width = 350
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')  # Width x Height
root.resizable(False, False)
root.configure(bg="#344955")


style = ttk.Style()
style.configure("Card.TFrame", background="#344955")
style.configure("TLabel", background="#344955", foreground="#f2f2f2", font=("Helvetica", 12))  # updated
style.configure("TButton", background="#344955", foreground="blue", font=("Helvetica", 12))  # updated
style.configure("TEntry", background="#344955", foreground="black", font=("Helvetica", 12), fieldbackground='#f2f2f2')

back = ttk.Button(root,text="Back",width=5,command= back)
back.pack(padx=2,anchor=tk.W)

frame = ttk.Frame(root,style="Card.TFrame", padding="20 20 20 20")
frame.pack(fill="both", expand=True)

yantra_label = tk.Label(frame, text="Password Manager",relief=RAISED,background='#344955',highlightthickness=0,foreground='white', font=("Helvetica", 24, "bold"))
yantra_label.grid(row=0, column=0, columnspan=2, pady=20)

signup_label = ttk.Label(frame, text="Create your account", font=("Helvetica", 20))
signup_label.grid(row=1, column=0, columnspan=2, pady=10)

adventure_label = ttk.Label(frame, text="Your Privacy is in your hand", font=("Helvetica", 12))
adventure_label.grid(row=2, column=0, columnspan=2, pady=(0, 20))

username = ttk.Label(frame, text="Username:",font=("Aerial",15))
username.grid(row=3, column=0, sticky="w", pady=2)
user = tk.Entry(frame, width=20, borderwidth=4, relief=SUNKEN, font=('Arial', 12),
           highlightbackground="gold", highlightcolor="gold", highlightthickness=0,background='#344955',foreground='white')
user.grid(row=4, column=0, pady=10)

password_label = ttk.Label(frame, text="Password:",font=("Aerial",15))
password_label.grid(row=5, column=0, sticky="w", pady=2)
password_entry = tk.Entry(frame, width=20, borderwidth=4, relief=SUNKEN, font=('Arial', 12),
           highlightbackground="gold", highlightcolor="gold", highlightthickness=0,background='#344955',show="*",foreground='white')
password_entry.grid(row=6, column=0, pady=10)

cpassword_label = ttk.Label(frame, text="Confirm Password:",font=("Aerial",15))
cpassword_label.grid(row=7, column=0, sticky="w", pady=2)
cpassword_entry = tk.Entry(frame, width=20, borderwidth=4, relief=SUNKEN, font=('Arial', 12),
           highlightbackground="gold", highlightcolor="gold", highlightthickness=0,background='#344955',show="*",foreground='white')
cpassword_entry.grid(row=8, column=0, pady=10)

signup_button = ttk.Button(frame, text="Let's go",command=sign_up)
signup_button.grid(row=9, column=0, columnspan=2, pady=20)

root.mainloop()