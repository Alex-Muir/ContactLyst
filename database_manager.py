import sqlite3
import helpers as h

# functions to aid in interfacing with the database


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