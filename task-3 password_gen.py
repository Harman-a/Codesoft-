
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return

        chars = ""
        if var_upper.get():
            chars += string.ascii_uppercase
        if var_lower.get():
            chars += string.ascii_lowercase
        if var_digits.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("Warning", "Select at least one character type.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Character type options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=var_upper).pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=var_lower).pack(anchor='w')
tk.Checkbutton(root, text="Include Digits (0-9)", variable=var_digits).pack(anchor='w')
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=var_symbols).pack(anchor='w')

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

password_var = tk.StringVar()
tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, textvariable=password_var, width=30, state='readonly')
password_entry.pack(pady=5)

root.mainloop()
