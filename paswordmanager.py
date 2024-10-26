import tkinter as tk
from tkinter import messagebox

def add():
    username = entryName.get()
    password = entryPassword.get()
    if username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Success", "Password added successfully!")
        entryName.delete(0, tk.END)
        entryPassword.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter both fields.")

def get():
    username = entryName.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username.")
        return

    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for line in f:
                if line.strip():  # Ensure line is not empty
                    user, pwd = line.split(' ', 1)
                    passwords[user] = pwd.strip()
        
        if username in passwords:
            messagebox.showinfo("Password", f"Password for {username} is {passwords[username]}")
        else:
            messagebox.showinfo("Error", "No such username exists.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Password file not found.")

def getlist():
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for line in f:
                if line.strip():
                    user, pwd = line.split(' ', 1)
                    passwords[user] = pwd.strip()

        if passwords:
            mess = "List of passwords:\n"
            for name, password in passwords.items():
                mess += f"Password for {name} is {password}\n"
            messagebox.showinfo("Passwords", mess)
        else:
            messagebox.showinfo("Passwords", "No passwords found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Password file not found.")

def delete():
    username = entryName.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username to delete.")
        return

    temp_passwords = []
    try:
        with open("passwords.txt", 'r') as f:
            for line in f:
                if line.strip():
                    user, pwd = line.split(' ', 1)
                    if user != username:
                        temp_passwords.append(line.strip())

        with open("passwords.txt", 'w') as f:
            for line in temp_passwords:
                f.write(line + '\n')

        messagebox.showinfo("Success", f"User {username} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user {username}: {e}")

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("560x270")
    app.title("Password Manager")

    labelName = tk.Label(app, text="USERNAME:")
    labelName.grid(row=0, column=0, padx=15, pady=15)
    entryName = tk.Entry(app)
    entryName.grid(row=0, column=1, padx=15, pady=15)

    labelPassword = tk.Label(app, text="PASSWORD:")
    labelPassword.grid(row=1, column=0, padx=10, pady=5)
    entryPassword = tk.Entry(app, show='*')# Hide password by default
    entryPassword.grid(row=1, column=1, padx=10, pady=5)

    buttonAdd = tk.Button (app, text="Add", command=add)
    buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

    buttonGet = tk.Button (app, text="Get", command=get)
    buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

    buttonList = tk.Button (app, text="List", command=getlist)
    buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

    buttonDelete = tk.Button (app, text="Delete", command=delete)
    buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")

    app.mainloop()
