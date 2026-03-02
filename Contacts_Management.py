import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return{}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contacts
def add_contact(contacts):
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    email = input('Enter email: ')
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print("✅ Contact added successfully.")

#View contacts
def view_contacts(contacts):
    if not contacts:
        print('No Contacts found.')
    else:
        for name, info in contacts.items():
            print(f"{name} -> phone: {info['phone']}, Email: {info['email']}")

# Search contact
def search_contact(contacts):
    name = input('Enter name to search: ')
    if name in contacts:
        info = contacts[name]
        print(f"Found: Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("❌ Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input('Enter name to delete: ')
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑 Contact deleted.")
    else:
        print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Manager =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input('Enter choice: ')

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == '5':
            print('Goodbye 👋')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()