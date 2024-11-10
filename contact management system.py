import json
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Define the file path for storing contacts
CONTACTS_FILE = "contacts.json"

# Function to load contacts from the JSON file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

# Function to save contacts to the JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    if not name:
        return
    contacts = load_contacts()
    if name in contacts:
        messagebox.showwarning("Warning", "Contact already exists.")
        return

    phone = simpledialog.askstring("Add Contact", "Enter phone number:")
    email = simpledialog.askstring("Add Contact", "Enter email address:")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
    display_contacts()

# Function to view all contacts
def display_contacts():
    contacts = load_contacts()
    contact_list.delete(0, tk.END)  # Clear existing list
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name}: {info['phone']} - {info['email']}")

# Function to update an existing contact
def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
    contacts = load_contacts()
    if name not in contacts:
        messagebox.showwarning("Warning", "Contact not found.")
        return

    phone = simpledialog.askstring("Update Contact", f"Enter new phone number (current: {contacts[name]['phone']}):") or contacts[name]['phone']
    email = simpledialog.askstring("Update Contact", f"Enter new email address (current: {contacts[name]['email']}):") or contacts[name]['email']

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    messagebox.showinfo("Success", f"Contact '{name}' updated successfully.")
    display_contacts()

# Function to delete a contact
def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
    contacts = load_contacts()
    if name not in contacts:
        messagebox.showwarning("Warning", "Contact not found.")
        return

    del contacts[name]
    save_contacts(contacts)
    messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
    display_contacts()

# Initialize the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x400")

# Define the UI components
title_label = tk.Label(root, text="Contact Management System", font=("Arial", 16))
title_label.pack(pady=10)

contact_list = tk.Listbox(root, width=50, height=15)
contact_list.pack(pady=10)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

view_button = tk.Button(root, text="Refresh Contacts", command=display_contacts)
view_button.pack(pady=5)

# Load and display contacts on startup
display_contacts()

# Run the main loop
root.mainloop()
