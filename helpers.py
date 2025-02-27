#import database_manager as dm

# Functions to help database_manager functions and main.py

def print_menu():
    """Print the user menu. Used in main.py"""
    print("""
(1) Add a new contact
(2) View all contacts
(3) Search for a contact by name
(4) Update contact details
(5) Delete a contact
(0) Exit
    """)


def get_first_name():
    """Get the first name of the contact. Used in helpers.py"""
    f_name = None
    while not f_name:
        f_name = input("\nFirst Name (required): ").strip()
    return f_name.title()


def get_last_name():
    """Get the last name of the contact. Used in helpers.py"""
    l_name = None
    while not l_name:
        l_name = input("Last Name (required): ").strip()
    return l_name.title()


def get_phone_number():
    """Get the phone number of the contact. Used in helpers.py"""
    phone_number = None
    while not phone_number:
        phone_number = input("Phone Number (required): ").strip()
    return phone_number


def get_email():
    """Get the email of the contact. Used in helpers.py"""
    email = None
    email = input("Email (optional): ").strip()
    email = email if email else None
    return email


def get_contact_info():
    """
    Get all contact info for the contact and return it in a tuple. 
    Used in main.py
    """
    f_name = get_first_name()
    l_name = get_last_name()
    phone_number = get_phone_number()
    email = get_email()

    return (f_name, l_name, phone_number, email)
    

def update_first_name(f_name):
    """Update the contact's first name. Used in helpers.py"""
    while True:
        f_name = input("\nWhat is the updated first name of the contact? ").strip()
        confirm = input(f"Is {f_name} correct? Enter 'y' if correct. Enter anything else to reenter: ").strip()
        if confirm.lower() == 'y':
            break
    return f_name


def update_last_name(l_name):
    """Update contact's last name. Used in helpers.py"""
    while True:
        l_name = input("\nWhat is the updated last name of the contact? ").strip()
        confirm = input(f"Is {l_name} correct? Enter 'y' if correct. Enter anything else to reenter: ").strip()
        if confirm.lower() == 'y':
            break
    return l_name


def update_phone_number(phone_number):
    """Update contact's phone number. Used in helpers.py"""
    while True:
        phone_number = input("\nWhat is the updated phone number of the contact? ").strip()
        confirm = input(f"Is {phone_number} correct? Enter 'y' if correct. Enter anything else to reenter: ").strip()
        if confirm.lower() == 'y':
            break
    return phone_number


def update_email(email):
    """Update contact's email. Used in helpers.py"""
    while True:
        email = input("\nWhat is the updated email of the contact? ").strip()
        confirm = input(f"Is {email} correct? Enter 'y' if correct. Enter anything else to reenter: ").strip()
        if confirm.lower() == 'y':
            break
    return email


def get_contact_updates(f_name, l_name, phone_number, email):
    """Update applicable contact details. Used in database_manager.py"""

    # Update first name
    update = input(f"\nDo you want to update the contact's first name from {f_name}? "
    "Enter 'y' to update. Enter anything else to skip: ").strip()

    if update.lower() == 'y':
        f_name = update_first_name(f_name)

    # Update last name
    update = input(f"\nDo you want to update the contact's last name from {l_name}? "
    "Enter 'y' to update. Enter anything else to skip: ").strip()

    if update.lower() == 'y':
        l_name = update_last_name(l_name)

    # Update phone number
    update = input(f"\nDo you want to update the contact's phone number from {phone_number}? "
    "Enter 'y' to update. Enter anything else to skip: ").strip()

    if update.lower() == 'y':
        phone_number = update_phone_number(phone_number)

    # Update email
    update = input(f"\nDo you want to update the contact's email from {email}? "
    "Enter 'y' to update. Enter anything else to skip: ").strip()

    if update.lower() == 'y':
        email = update_email(email)

    return (f_name, l_name, phone_number, email)


def get_valid_id(cur):
    """Get a valid contact ID from the user, or cancel"""
    while True:
        #dm.print_contacts(cur)
        user_input = input("\nEnter the ID of the contact or 'q' to cancel: ").strip()
        try:
            contact_id = int(user_input)
        except ValueError:
            if user_input.lower() == 'q':
                return user_input
            else:
                print("\nPlease enter the ID of the contact. Must be a valid integer.")
        else:
            res = cur.execute("SELECT id FROM contacts WHERE id = ?", (contact_id,))
            if res.fetchone():
                break
            else:
                print("\nThe ID you entered does not exist. Please enter a valid ID.")

    return contact_id

    
