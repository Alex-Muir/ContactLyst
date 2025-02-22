# Functions to help data

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
    """Get the first name of the contact. Used in database_manager.py"""
    f_name = None
    while not f_name:
        f_name = input("First Name (required): ")
    return f_name.title()

def get_last_name():
    """Get the last name of the contact. Used in database_manager.py"""
    l_name = None
    while not l_name:
        l_name = input("Last Name (required): ")
    return l_name.title()

def get_phone_number():
    """Get the phone number of the contact. Used in database_manager.py"""
    phone_number = None
    while not phone_number:
        phone_number = input("Phone Number (required): ")
    return phone_number

def get_email():
    """Get the email of the contact"""
    email = None
    while not email:
        email = input("Email (optional): ")
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

    contact_info = (f_name, l_name, phone_number, email)
    return contact_info