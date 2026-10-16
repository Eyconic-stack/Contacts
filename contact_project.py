import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Enter your email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Saved!")

def show_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts yet")
    for contact in contacts:
        print(contact["name"], "-", contact["phone"], "-", contact["email"])

def search_contact(contacts):
    search = input("Search name: ").lower()
    found = False
    for contact in contacts:
        if search in contact["name"].lower():
            print(contact["name"], "-", contact["phone"], "-", contact["email"])
            found = True
    if not found:
        print("Not found")

def delete_contact(contacts):
    name = input("Name to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Deleted")
            return
    print("Not found")

def edit_contact(contacts):
    edit = input("Name to edit: ").lower()
    for contact in contacts:
        if contact["name"].lower() == edit:
            contacts.remove(contact)
            contact["name"] = input("Enter your name: ")
            contact["phone"] = input("Enter your phone: ")
            contact["email"] = input("Enter your email: ")
            contacts.append({"name": contact["name"], "phone": contact["phone"], "email": contact["email"]})
            save_contacts(contacts)
            print("Contacts edited successfully")
            return
    print("Not found")
contacts = load_contacts()

while True:
    print("\n1. Add  2. Show all  3. Search  4. Delete  5. Edit  6. Quit")
    choice = input("Choose: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        show_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        delete_contact(contacts)
    elif choice == "5":
        edit_contact(contacts)
    elif choice == "6":
        break
    else:
        print("Invalid choice")