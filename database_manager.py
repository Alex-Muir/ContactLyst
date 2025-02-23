import sqlite3
import helpers as h

# functions for interfacing with the database


def create_table(cur, con):
    """Create the table to hold contacts"""
    try:
        with open('schema.sql') as f:
            contacts_schema = f.read()
    except FileNotFoundError:
        print("'schema.sql' does not exist")
    else:
        cur.execute(contacts_schema)
        con.commit()


def add_contact(con, cur, contact_info):
    """Add the contact to the database"""
    cur.execute("INSERT INTO contacts (fname, lname, phone_number, email) VALUES (?, ?, ?, ?)", contact_info)
    con.commit()


def print_contacts(cur):
    """Print all the contacts in the database"""
    res = cur.execute("SELECT * FROM contacts")
    contacts = res.fetchall()
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Phone Number':<15} {'Email'}")
    print('-' * 85)
    for contact in contacts:
        print(f"{contact[0]:<5} {contact[1]:<15} {contact[2]:<15} {contact[3]:<15} {contact[4]}")


def delete_contact(cur, con):
    """Delete a contact from the database"""
    keep_going = True
    contact_id = ""

    while keep_going:
        print_contacts(cur)
        user_input = input("Enter the ID of the contact to be deleted or 'q' to cancel: ")
        try:
            contact_id = int(user_input)
        except ValueError:
            if user_input.lower() == 'q':
                return
            else:
                print("Please enter the ID of the contact. Must be a valid integer.")
        else:
            res = cur.execute("SELECT id FROM contacts")
            contact_id_list = res.fetchall()
            # Check whether the id entered by the user is actually 
            # found in the list of tuples returned by res.fetchall()
            valid_id = any(contact_id in contact for contact in contact_id_list)
            if valid_id:
                keep_going = False
            else:
                print("The ID you entered does not exist. Please enter a valid ID.")
    
    cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    con.commit()

        
def update_contact(cur, con):
    """Update a contacts details"""
    keep_going = True
    contact_id = ""

    while keep_going:
        print_contacts(cur)
        user_input = input("Enter the ID of the contact to be updated or 'q' to cancel: ")
        try:
            contact_id = int(user_input)
        except ValueError:
            if user_input.lower() == 'q':
                return
            else:
                print("Please enter the ID of the contact. Must be a valid integer.")
        else:
            res = cur.execute("SELECT id FROM contacts")
            contact_id_list = res.fetchall()
            # Check whether the id entered by the user is actually 
            # found in the list of tuples returned by res.fetchall()
            valid_id = any(contact_id in contact for contact in contact_id_list)
            if valid_id:
                keep_going = False
            else:
                print("The ID you entered does not exist. Please enter a ")

    # Next add section to prompt user for changes to be made to fname, lname, phone_number, or email.
    res = cur.execute("SELECT fname, lname, phone_number, email FROM contacts WHERE id = ?", (contact_id,))
    contact_list = res.fetchall()
    contact = contact_list[0]

    f_name = contact[0]
    l_name = contact[1]
    phone_number = contact[2]
    email = contact[3]

    confirm = ''

    # Update first name
    update = input(f"Do you want to update the contact's first name from {f_name}? "
    "Enter 'y' to update. Enter anything else to skip: ")

    if update.lower() == 'y':
        while True:
            f_name = input("What is the updated first name of the contact? ")
            confirm = input(f"Is {f_name} correct? Enter 'y' if correct. Enter anything else to reenter")
            if confirm.lower() == 'y':
                break

    # Update last name
    update = input(f"Do you want to update the contact's last name from {l_name}? "
    "Enter 'y' to update. Enter anything else to skip: ")

    if update.lower() == 'y':
        while True:
            l_name = input("What is the updated last name of the contact? ")
            confirm = input(f"Is {l_name} correct? Enter 'y' if correct. Enter anything else to reenter")
            if confirm.lower() == 'y':
                break

    # Update phone number
    update = input(f"Do you want to update the contact's phone number from {phone_number}? "
    "Enter 'y' to update. Enter anything else to skip: ")

    if update.lower() == 'y':
        while True:
            phone_number = input("What is the updated phone number of the contact? ")
            confirm = input(f"Is {phone_number} correct? Enter 'y' if correct. Enter anything else to reenter")
            if confirm.lower() == 'y':
                break

    # Update email
    update = input(f"Do you want to update the contact's email from {email}? "
    "Enter 'y' to update. Enter anything else to skip: ")

    if update.lower() == 'y':
        while True:
            email = input("What is the updated email of the contact? ")
            confirm = input(f"Is {email} correct? Enter 'y' if correct. Enter anything else to reenter")
            if confirm.lower() == 'y':
                break

    updated_contact = (f_name, l_name, phone_number, email, contact_id)
    cur.execute("UPDATE contacts SET fname = ?, lname = ?, phone_number = ?, email = ? WHERE id = ?",updated_contact)
    con.commit()
            

