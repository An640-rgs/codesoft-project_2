import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = password_length.get()

    if not length.isdigit() or int(length) < 4:
        messagebox.showerror("Invalid Input", "Please enter a valid number (4 or more).")
        return

    length = int(length)
    
    # Character sets
    all_chars = ""
    if var_upper.get():
        all_chars += string.ascii_uppercase
    if var_lower.get():
        all_chars += string.ascii_lowercase
    if var_digits.get():
        all_chars += string.digits
    if var_symbols.get():
        all_chars += string.punctuation

    if not all_chars:
        messagebox.showwarning("Select Options", "Select at least one character set!")
        return

    password = ''.join(random.choice(all_chars) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Password length input
tk.Label(root, text="Password Length:").pack(pady=5)
password_length = tk.Entry(root, width=10, justify='center')
password_length.pack()

# Options for character sets
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor='w', padx=20)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="lightblue").pack(pady=10)

# Entry to show generated password
entry_password = tk.Entry(root, width=30, font=("Arial", 14), justify="center")
entry_password.pack(pady=10)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="lightgreen").pack(pady=5)

# Start GUI loop
root.mainloop()
