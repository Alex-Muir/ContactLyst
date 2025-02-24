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
    contact_id = ""

    while True:
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
            res = cur.execute("SELECT id FROM contacts WHERE id = ?", (contact_id,))
            if res.fetchone():
                break
            else:
                print("The ID you entered does not exist. Please enter a valid ID.")
    
    cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    con.commit()

        
def update_contact(cur, con):
    """Update a contacts details"""
    contact_id = ""

    # Get a valid contact id
    while True:
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
            res = cur.execute("SELECT id FROM contacts WHERE id = ?", (contact_id,))
            if res.fetchone():
                break
            else:
                print("The ID you entered does not exist. Please enter a ")

    # Move the result to a tuple
    res = cur.execute("SELECT fname, lname, phone_number, email FROM contacts WHERE id = ?", (contact_id,))
    contact = res.fetchone()

    # Set respective contact details to a clearly identifiable variable
    f_name = contact[0]
    l_name = contact[1]
    phone_number = contact[2]
    email = contact[3]

    # Update and commit
    updated_contact = h.get_contact_updates(f_name, l_name, phone_number, email) + (contact_id,)
    cur.execute("UPDATE contacts SET fname = ?, lname = ?, phone_number = ?, email = ? WHERE id = ?", updated_contact)
    con.commit()
            

