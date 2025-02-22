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
    con.commit