import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        result.config(text=password)

        if length < 8:
            strength.config(text="🔴 Weak Password")
        elif length < 12:
            strength.config(text="🟡 Medium Password")
        else:
            strength.config(text="🟢 Strong Password")

    except:
        result.config(text="Enter a valid number")
        strength.config(text="")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result.cget("text"))
    copied.config(text="✅ Password Copied!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")
root.configure(bg="#E8F0FE")

title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 24, "bold"),
    bg="#E8F0FE"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial", 12),
    bg="#E8F0FE"
).pack()

length_entry = tk.Entry(root, font=("Arial", 14), width=20)
length_entry.pack(pady=10)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    command=generate_password
)
generate_btn.pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Courier", 16, "bold"),
    bg="#E8F0FE"
)
result.pack(pady=20)

strength = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#E8F0FE"
)
strength.pack()

copy_btn = tk.Button(
    root,
    text="📋 Copy Password",
    font=("Arial", 11),
    command=copy_password
)
copy_btn.pack(pady=15)

copied = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="#E8F0FE"
)
copied.pack()

root.mainloop()
