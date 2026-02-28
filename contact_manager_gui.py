import tkinter as tk
from tkinter import messagebox
import csv
import os

FILE = "contacts.csv"


# create csv file if not exists
def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "Email"])


# load contacts into listbox
def load_contacts():
    listbox.delete(0, tk.END)

    with open(FILE, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]}")


# add contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not phone or not email:
        messagebox.showwarning("Warning", "Fill all fields")
        return

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])

    messagebox.showinfo("Success", "Contact added")

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    load_contacts()


# delete contact
def delete_by_name():
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Warning", "Enter name to delete")
        return

    with open(FILE, "r", newline="") as f:
        reader = list(csv.reader(f))

    header = reader[0]
    contacts = reader[1:]

    new_contacts = []
    found = False

    for row in contacts:
        if row[0].lower() != name.lower():
            new_contacts.append(row)
        else:
            found = True

    if not found:
        messagebox.showerror("Error", "Contact not found")
        return

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(new_contacts)

    messagebox.showinfo("Success", "Contact deleted")

    load_contacts()

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# fill entry when clicking contact
def select_contact(event):
    selected = listbox.curselection()

    if selected:
        text = listbox.get(selected[0])
        name, phone, email = text.split(" | ")

        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, phone)

        email_entry.delete(0, tk.END)
        email_entry.insert(0, email)


# GUI setup
init_file()

root = tk.Tk()
root.title("Contact Manager")
root.geometry("450x450")


tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()


tk.Button(root, text="Add Contact", width=20, command=add_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_by_name).pack()
tk.Button(root, text="Refresh", width=20, command=load_contacts).pack(pady=5)


# listbox + scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT)

scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

listbox.bind("<<ListboxSelect>>", select_contact)


load_contacts()

root.mainloop()