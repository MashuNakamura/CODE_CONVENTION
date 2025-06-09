from typing import List, Dict

def display_contacts_ascending(contacts: List[Dict]) -> None:
    """Display contacts sorted by name in ascending order."""
    contacts.sort(key=lambda x: x['name'])
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']}")

def display_contacts_descending(contacts: List[Dict]) -> None:
    """Display contacts sorted by name in descending order."""
    contacts.sort(key=lambda x: x['name'], reverse=True)
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']}")

def display_contact_names(contacts: List[Dict]) -> None:
    """Display list of contact names with option to return."""
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']}")
    print("===========================")

def display_contact_details(contacts: List[Dict], index: int) -> None:
    """Display details of a specific contact."""
    if 0 <= index < len(contacts):
        selected = contacts[index]
        print("===========================")
        print(f"Name    : {selected['name']}")
        print(f"Email   : {selected['email']}")
        print(f"Phone   : {selected['phone']}")
        print("===========================")
    else:
        print("===========================")
        print("Contact not found!")
        print("===========================")

def add_new_contact() -> Dict:
    """Add a new contact and return the contact dictionary."""
    print("===========================")
    print("Add New Contact")
    print("===========================")
    
    name = input("Enter Name (0 to cancel): ").strip()
    if name == "0":
        print("Add contact cancelled.")
        return None
    
    email = input("Enter Email (0 to cancel): ").strip()
    if email == "0":
        print("Add contact cancelled.")
        return None
    
    phone = input("Enter Phone (0 to cancel): ").strip()
    if phone == "0":
        print("Add contact cancelled.")
        return None
    
    new_contact = {
        "name": name,
        "email": email,
        "phone": phone
    }
    print(f"{name} has been added successfully")
    return new_contact

def delete_contact(contacts: List[Dict]) -> None:
    """Delete a contact from the list."""
    print("===========================")
    print("Delete Contact")
    print("===========================")
    
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']}")
    print("0. Back")
    print("===========================")
    
    user_choice_input = input("Which number do you want to delete (0 to cancel): ")
    
    if user_choice_input == "0":
        print("Delete cancelled.")
        return
        
    if not user_choice_input.isdigit():
        print("Invalid input!")
        return
        
    user_choice = int(user_choice_input)

    if 1 <= user_choice <= len(contacts):
        deleted = contacts.pop(user_choice - 1)
        print("===========================")
        print(f"{deleted['name']} has been deleted.")
    else:
        print("===========================")
        print("Contact not found!")

def search_contact(contacts: List[Dict]) -> None:
    """Search for a contact by name or phone number."""
    while True:
        print("===========================")
        print("1. Search by Name")
        print("2. Search by Number")
        print("===========================")
        try:
            search_mode = int(input("Search mode (0 to cancel): "))
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        if search_mode not in [0, 1, 2]:
            print("Invalid choice. Please enter 0, 1, or 2.")
            continue
            
        found = False
        
        if search_mode == 1:
            search_term = input("Search contact by name (0 to cancel): ").lower()
            if search_term == "0":
                continue
            for contact in contacts:
                if search_term in contact['name'].lower():
                    print_contact_details(contact)
                    found = True
            
        elif search_mode == 2:
            search_term = input("Search contact by number (0 to cancel): ")
            if search_term == "0":
                continue
            for contact in contacts:
                if search_term in contact['phone']:
                    print_contact_details(contact)
                    found = True
                    
        elif search_mode == 0:
            break
            
        if not found and search_mode != 0:
            print("===========================")
            print("Contact not found")
            print("===========================")

def edit_contact(contacts: List[Dict]) -> None:
    """Edit the selected contact's name, email, or phone number."""
    print("===========================")
    print("Choose a contact to edit")
    print("===========================")

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']}")
    print("0. Back")
    print("===========================")
     
    user_input = input("Which contact do you want to edit (enter name or number, 0 to cancel): ").lower()
    
    if user_input == "0":
        print("Edit cancelled.")
        return
    
    for idx, contact in enumerate(contacts, start=1):
        if user_input == contact["name"].lower() or (user_input.isdigit() and int(user_input) == idx):

            old_name = contact["name"]
            old_email = contact["email"]
            old_phone = contact["phone"]
            
            print("\nPress Enter to skip and keep current value, or type 0 to cancel edit")
            print("===========================")
            
            print(f"Current Name: {old_name}")
            new_name = input("Enter New Name: ").strip()
            if new_name == "0":
                print("Edit cancelled.")
                return
            if new_name:
                contact["name"] = new_name
            
            print(f"Current Email: {old_email}")
            new_email = input("Enter New Email: ").strip()
            if new_email == "0":
                print("Edit cancelled.")
                return
            if new_email:
                contact["email"] = new_email
            
            print(f"Current Phone: {old_phone}")
            new_phone = input("Enter New Phone: ").strip()
            if new_phone == "0":
                print("Edit cancelled.")
                return
            if new_phone:
                contact["phone"] = new_phone
            
            print("\nContact updated successfully:")
            print(f"Name  : {contact['name']}")
            print(f"Email : {contact['email']}")
            print(f"Phone : {contact['phone']}")
            return
            
    print("Contact not found.")

def print_contact_details(contact: Dict) -> None:
    """Helper function to print contact details."""
    print("===========================")
    print(f"Name    : {contact['name']}")
    print(f"Email   : {contact['email']}")
    print(f"Phone   : {contact['phone']}")
    print("===========================")