import tkinter as tk
from tkinter import messagebox
from database import Database

db = Database()

# ---------- Login Function ----------
def login():
    username = entry_username.get()
    password = entry_password.get()

    if db.validate_user(username, password):
        messagebox.showinfo("Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# ---------- Register Function ----------
def register():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    if db.register_user(username, password):
        messagebox.showinfo("Success", "Registration successful! You can now log in.")
    else:
        messagebox.showerror("Error", "Username already exists!")

# ---------- GUI ----------
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="Login System", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

tk.Label(frame, text="Username:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, pady=5, sticky="e")
entry_username = tk.Entry(frame, width=25)
entry_username.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Password:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, pady=5, sticky="e")
entry_password = tk.Entry(frame, show="*", width=25)
entry_password.grid(row=1, column=1, pady=5)

login_btn = tk.Button(root, text="Login", width=12, bg="#4CAF50", fg="white", command=login)
login_btn.pack(pady=5)

register_btn = tk.Button(root, text="Register", width=12, bg="#2196F3", fg="white", command=register)
register_btn.pack(pady=5)

root.mainloop()
