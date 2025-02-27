import sqlite3
import helpers as h
import database_manager as dm


# A simple contact book written in Python using sqlite
    
def main():

    print("\nWelcome to Contact Lyst. A simple Contact book written in python" 
          " using sqlite")

    con = sqlite3.connect("contacts.db")
    cur = con.cursor()

    dm.create_table(cur, con)

    while True:
        h.print_menu()
        selection = input("What would you like to do? ")

        if selection == '1':
            #print("'Add a new contact' selected")
            contact_info = h.get_contact_info()
            dm.add_contact(cur, con, contact_info)
        elif selection == '2':
            #print("'View all contacts' selected")
            dm.print_contacts(cur)
        elif selection == '3':
            #print("'Search for a contact by name' selected")
            dm.search_by_name(cur, con)
        elif selection == '4':
            #print("'Update contact details' selected")
            dm.update_contact(cur, con)
        elif selection == '5':
            #print("'Delete a contact' selected")
            dm.delete_contact(cur, con)
        elif selection == '0':
            #print("'Exit' selected")
            con.close()
            print("Good bye.")
            break
        else:
            print("Please enter a valid selection")
          
                
if __name__ == "__main__":
    main()
