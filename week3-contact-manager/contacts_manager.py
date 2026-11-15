
import json
import re
import csv
import os
from datetime import datetime, timedelta

DATA_FILE = "contacts_data.json"


def validate_phone(phone):
    digits = re.sub(r"\D", "", phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None


def validate_email(email):
    if not email:
        return True
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def load_from_file():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, OSError):
            print("Error loading contacts. Starting fresh.")
    return {}


def save_to_file(contacts):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(contacts, file, indent=4)
        print("Contacts saved successfully!")
    except OSError:
        print("Error saving contacts!")


def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")

    name = input("Enter contact name: ").strip().title()

    if not name:
        print("Name cannot be empty!")
        return

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    valid, cleaned_phone = validate_phone(phone)

    if not valid:
        print("Invalid phone number! Enter 10-15 digits.")
        return

    email = input("Enter email (optional): ").strip().lower()

    if not validate_email(email):
        print("Invalid email format!")
        return

    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Work/Family/Other): ").strip().title()

    contacts[name] = {
        "phone": cleaned_phone,
        "email": email,
        "address": address,
        "group": group or "Other",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    print(f"Contact '{name}' added successfully!")
    save_to_file(contacts)


def search_contacts(contacts, search_term):
    search_term = search_term.strip().lower()

    return {
        name: info for name, info in contacts.items()
        if search_term in name.lower()
        or search_term in info.get("phone", "")
    }


def display_contacts(results):
    if not results:
        print("No contacts found.")
        return

    print("\n--- CONTACT DETAILS ---")

    for name, info in results.items():
        print("-" * 40)
        print("Name:", name)
        print("Phone:", info.get("phone", ""))
        print("Email:", info.get("email") or "Not provided")
        print("Address:", info.get("address") or "Not provided")
        print("Group:", info.get("group", "Other"))
        print("-" * 40)


def update_contact(contacts):
    name = input("Enter contact name to update: ").strip().title()

    if name not in contacts:
        print("Contact not found!")
        return

    info = contacts[name]

    print("Press Enter to keep the existing value.")

    phone = input(f"New phone [{info['phone']}]: ").strip()

    if phone:
        valid, cleaned_phone = validate_phone(phone)
        if not valid:
            print("Invalid phone number!")
            return
        info["phone"] = cleaned_phone

    email = input(f"New email [{info.get('email', '')}]: ").strip().lower()

    if email:
        if not validate_email(email):
            print("Invalid email!")
            return
        info["email"] = email

    address = input(f"New address [{info.get('address', '')}]: ").strip()
    if address:
        info["address"] = address

    group = input(f"New group [{info.get('group', 'Other')}]: ").strip()
    if group:
        info["group"] = group.title()

    info["updated_at"] = datetime.now().isoformat()

    print("Contact updated successfully!")
    save_to_file(contacts)


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip().title()

    if name not in contacts:
        print("Contact not found!")
        return

    confirm = input(f"Delete {name}? (y/n): ").strip().lower()

    if confirm == "y":
        del contacts[name]
        print("Contact deleted successfully!")
        save_to_file(contacts)
    else:
        print("Delete cancelled.")


def display_all(contacts):
    display_contacts(contacts)


def export_to_csv(contacts):
    try:
        with open("contacts_export.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Address", "Group"])

            for name, info in contacts.items():
                writer.writerow([
                    name,
                    info.get("phone", ""),
                    info.get("email", ""),
                    info.get("address", ""),
                    info.get("group", "Other")
                ])

        print("Contacts exported to contacts_export.csv!")
    except OSError:
        print("Error exporting contacts!")


def show_statistics(contacts):
    print("\n--- CONTACT STATISTICS ---")
    print("Total Contacts:", len(contacts))

    groups = {}

    for info in contacts.values():
        group = info.get("group", "Other")
        groups[group] = groups.get(group, 0) + 1

    print("\nContacts by Group:")
    for group, count in groups.items():
        print(f"{group}: {count} contact(s)")

    recent = 0
    cutoff = datetime.now() - timedelta(days=7)

    for info in contacts.values():
        try:
            updated = datetime.fromisoformat(info["updated_at"])
            if updated >= cutoff:
                recent += 1
        except (KeyError, ValueError, TypeError):
            pass

    print("Recently Updated (last 7 days):", recent)


def main():
    contacts = load_from_file()

    print("=" * 50)
    print("       CONTACT MANAGEMENT SYSTEM")
    print("=" * 50)

    if contacts:
        print(f"Loaded {len(contacts)} existing contacts.")
    else:
        print("No existing contacts found. Starting fresh.")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            term = input("Enter name or phone to search: ")
            results = search_contacts(contacts, term)
            display_contacts(results)

        elif choice == "3":
            update_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            display_all(contacts)

        elif choice == "6":
            export_to_csv(contacts)

        elif choice == "7":
            show_statistics(contacts)

        elif choice == "8":
            save_to_file(contacts)
            print("Thank you for using Contact Management System!")
            break

        else:
            print("Invalid choice! Please enter 1-8.")


if __name__ == "__main__":
    main()
