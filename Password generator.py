import tkinter as tk
import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_var.set(password)
    except ValueError:
        password_var.set("Invalid input. Please enter a numeric value.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter the desired length of the password:").pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=5)

password_var = tk.StringVar()
tk.Label(root, textvariable=password_var).pack(pady=5)

root.mainloop()