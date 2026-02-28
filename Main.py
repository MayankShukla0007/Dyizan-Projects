import tkinter as tk
from tkinter import messagebox
import csv
import os

CONTACT_FILE = "contacts.csv"
USER_FILE = "users.csv"

# ==================== Utility Functions ====================
def init_files():
    if not os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Phone", "Email"])
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Username", "Password"])
            # default user
            writer.writerow(["admin", "admin123"])


def generate_id():
    with open(CONTACT_FILE, "r") as f:
        reader = list(csv.reader(f))
        if len(reader) <= 1:
            return "1001"
        last_id = int(reader[-1][0])
        return str(last_id + 1)


# ==================== Contact Functions ====================
def load_contacts():
    listbox.delete(0, tk.END)
    with open(CONTACT_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    if not name or not phone or not email:
        messagebox.showwarning("Warning", "Fill all fields")
        return
    uid = generate_id()
    with open(CONTACT_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([uid, name, phone, email])
    messagebox.showinfo("Success", f"Contact added with ID {uid}")
    clear_fields()
    load_contacts()


def update_contact():
    uid = id_entry.get().strip()
    if not uid:
        messagebox.showwarning("Warning", "Enter ID to update")
        return
    rows = []
    updated = False
    with open(CONTACT_FILE, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[0] == uid:
                name = name_entry.get().strip()
                phone = phone_entry.get().strip()
                email = email_entry.get().strip()
                rows.append([uid, name, phone, email])
                updated = True
            else:
                rows.append(row)
    with open(CONTACT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    if updated:
        messagebox.showinfo("Success", "Contact updated")
    else:
        messagebox.showerror("Error", "ID not found")
    clear_fields()
    load_contacts()


def delete_contact():
    uid = id_entry.get().strip()
    if not uid:
        messagebox.showwarning("Warning", "Enter ID to delete")
        return
    rows = []
    deleted = False
    with open(CONTACT_FILE, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[0] != uid:
                rows.append(row)
            else:
                deleted = True
    with open(CONTACT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    if deleted:
        messagebox.showinfo("Success", "Contact deleted")
    else:
        messagebox.showerror("Error", "ID not found")
    clear_fields()
    load_contacts()


def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


def select_contact(event):
    selected = listbox.curselection()
    if selected:
        text = listbox.get(selected[0])
        uid, name, phone, email = [x.strip() for x in text.split("|")]
        id_entry.delete(0, tk.END)
        id_entry.insert(0, uid)
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, phone)
        email_entry.delete(0, tk.END)
        email_entry.insert(0, email)


# ==================== Login Functions ====================
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    with open(USER_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == username and row[1] == password:
                messagebox.showinfo("Success", "Login Successful")
                login_window.destroy()
                open_main_window()
                return
    messagebox.showerror("Error", "Invalid Username or Password")


# ==================== GUI ====================
def open_main_window():
    global root, id_entry, name_entry, phone_entry, email_entry, listbox
    root = tk.Tk()
    root.title("Advanced Contact Manager")
    root.geometry("600x500")

    # Input fields
    tk.Label(root, text="ID").pack()
    id_entry = tk.Entry(root, width=40)
    id_entry.pack()

    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root, width=40)
    name_entry.pack()

    tk.Label(root, text="Phone").pack()
    phone_entry = tk.Entry(root, width=40)
    phone_entry.pack()

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root, width=40)
    email_entry.pack()

    # Buttons
    tk.Button(root, text="Add Contact", width=20, command=add_contact).pack(pady=5)
    tk.Button(root, text="Update Contact", width=20, command=update_contact).pack(pady=5)
    tk.Button(root, text="Delete Contact", width=20, command=delete_contact).pack(pady=5)
    tk.Button(root, text="Clear Fields", width=20, command=clear_fields).pack(pady=5)
    tk.Button(root, text="Refresh List", width=20, command=load_contacts).pack(pady=5)

    # Listbox + scrollbar
    frame = tk.Frame(root)
    frame.pack(pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, width=70, height=15)
    listbox.pack(side=tk.LEFT)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.bind("<<ListboxSelect>>", select_contact)

    load_contacts()
    root.mainloop()


# ==================== Login Window ====================
init_files()
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Username").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", width=15, command=login).pack(pady=10)

login_window.mainloop()