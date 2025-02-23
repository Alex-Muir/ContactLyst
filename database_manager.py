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
            valid_id = any(contact_id in contact for contact in contact_id_list)
            if valid_id:
                keep_going = False
            else:
                print("The ID you entered does not exist. Please")
    
    cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    con.commit()

        


