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


def add_contact(cur, con, contact_info):
    """Add the contact to the database"""
    try:
        cur.execute("INSERT INTO contacts (fname, lname, phone_number, email) VALUES (?, ?, ?, ?)", contact_info)
    except sqlite3.IntegrityError:
        print("\nThe phone number or email you entered is already used by another contact.")
    else:
        con.commit()
        print(f"\n{contact_info[0]} {contact_info[1]} has been added to your contact list.")


def print_contacts(cur):
    """Print all the contacts in the database"""
    res = cur.execute("SELECT * FROM contacts ORDER BY lname ASC")
    contacts = res.fetchall()
    print(f"\n{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Phone Number':<15} {'Email'}")
    print('-' * 85)
    for contact in contacts:
        print(f"{contact[0]:<5} {contact[1]:<15} {contact[2]:<15} {contact[3]:<15} {contact[4]}")


def delete_contact(cur, con):
    """Delete a contact from the database"""
    print_contacts(cur)
    contact_id = h.get_valid_id(cur)
    if contact_id == 'q':
        return
    cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    con.commit()
    print("\nContact has been deleted.")

        
def update_contact(cur, con):
    """Update a contacts details"""
    print_contacts(cur)
    contact_id = h.get_valid_id(cur)
    if contact_id == 'q':
        return

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
    try:
        cur.execute("UPDATE contacts SET fname = ?, lname = ?, phone_number = ?, email = ? WHERE id = ?", updated_contact)
    except sqlite3.IntegrityError:
        print("\nThe phone number or email you entered is already used by another contact.")
    else:
        con.commit()
        print(f"Contact has been updated.")


def search_by_name(cur, con):
    """Search for a contact by name in the database"""
    search_params = ""
    while True:
        search_params = input("\nEnter a first, last, or partial name: ").strip()
        if not search_params:
            print("\nInput cannot be empty.")
        else:
            break

    search_params = '%' + search_params + '%'
    search_tuple = (search_params, search_params)

    res = cur.execute("SELECT * FROM contacts WHERE fname LIKE ? OR lname LIKE ? ORDER BY lname ASC", search_tuple)
    if not res:
        print("\nNo matches found.")
        return

    matched_contacts = res.fetchall()

    print(f"\n{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Phone Number':<15} {'Email'}")
    print('-' * 85)
    for contact in matched_contacts:
        print(f"{contact[0]:<5} {contact[1]:<15} {contact[2]:<15} {contact[3]:<15} {contact[4]}")



            

