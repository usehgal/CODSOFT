import tkinter as tk
import string
import random
from tkinter import messagebox

def generate_password():
    try:
        username = username_entry.get()
        password_length = int(length_entry.get())
        if password_length < 4:
            messagebox.showwarning("Invalid Length", "Password length should be at least 4 characters.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, generated_password)
        accept_button.config(state=tk.NORMAL)  # Enable the Accept button after generating the password
    except ValueError:
        messagebox.showwarning("Invalid Length", "Please enter a valid password length.")
        return

def accept_password():
    messagebox.showinfo("Accepted", "Password has been accepted!")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    accept_button.config(state=tk.DISABLED)  # Disable the Accept button when fields are reset

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Title label
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

# Label and entry widgets for username
username_label = tk.Label(root, text="Enter username:")
username_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=5, pady=5)

# Label and entry widgets for password length
length_label = tk.Label(root, text="Enter password length:")
length_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1, padx=5, pady=5)

# Label and entry widgets to display generated password
password_label = tk.Label(root, text="Generated password:")
password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(root)
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons for actions
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

accept_button = tk.Button(root, text="Accept", command=accept_password, state=tk.DISABLED)  # Start with Accept button disabled
accept_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()
