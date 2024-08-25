import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def label_clicked(event):
    root.destroy()
    import sign

def get_started():
    root.destroy()
    import signup

# Create the main window
root = tk.Tk()
root.title("Password Manager")

# Set the window size to resemble a phone screen
width = 350
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')  # Width x Height
root.resizable(False, False)  # Make the window non-resizable

# Create a frame for the main content
main_content = tk.Frame(root, bg="white")
main_content.pack(fill=tk.BOTH, expand=True)

# Load the image using Pillow
image = Image.open("logo type.png")

# Resize the image (width, height)
resized_image = image.resize((150, 150))  # Change the size as needed

# Convert the resized image to a PhotoImage object
photo = ImageTk.PhotoImage(resized_image)

# Create a label and set the image without a border
label = tk.Label(main_content, image=photo, borderwidth=0, highlightthickness=0)
label.pack(pady=20)

# Configure the style for the text label
style = ttk.Style()
style.configure("show.TLabel", background="white", font=("Arial", 16, "bold"))
style.configure("inst.TLabel", background="white", font=("Arial", 10))
style.configure("butt.TButton", background="white", foreground="black", font=("Arial", 15),
                borderwidth=0, highlightthickness=0)  # Remove border and highlight
style.configure("alr.TLabel", background="white", font=("Arial", 10, "underline"), foreground="blue")

# Create text labels with the configured style
show1 = ttk.Label(main_content, text="Enhance Safety", style="show.TLabel")
show1.pack(pady=5)
show2 = ttk.Label(main_content, text="With", style="show.TLabel")
show2.pack(pady=1)
show3 = ttk.Label(main_content, text="Total Security", style="show.TLabel")
show3.pack(pady=5)

# Create a frame for instructions
inst_frame = tk.Frame(main_content, bg="white")
inst_frame.pack(pady=30)

# Add instruction labels
inst1 = ttk.Label(inst_frame, text="Stop using unsecure passwords for your online", style="inst.TLabel")
inst1.pack(pady=2)
inst2 = ttk.Label(inst_frame, text="accounts. Get the most secure and difficult-to-", style="inst.TLabel")
inst2.pack(pady=2)
inst3 = ttk.Label(inst_frame, text="crack passwords", style="inst.TLabel")
inst3.pack(pady=2)

# Create the button with the configured style (without border)
sign = tk.Button(main_content,width=15,font=("Arial",12) ,text="Get Started",background='blue',foreground='white', command=get_started)
sign.pack(pady=20)

# Create the already have an account label with the configured style
already = ttk.Label(main_content, text="Already have an account", style="alr.TLabel")
already.pack()

# Bind the label click event to the function
already.bind("<Button-1>", label_clicked)

# Run the application
root.mainloop()
