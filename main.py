

def main():
    while True:
        print("""
            (1) Add a new contact
            (2) View all contacts
            (3) Search for a contact by name
            (4) Update contact details
            (5) Delete a contact
            (0) Exit
            """)
        selection = input("What would you like to do? ")

        if selection == '1':
            print("'Add a new contact' selected")
        elif selection == '2':
            print("'View all contacts' selected")
        elif selection == '3':
            print("'Search for a contact by name' selected")
        elif selection == '4':
            print("'Update contact details' selected")
        elif selection == '5':
            print("'Delete a contact' selected")
        elif selection == '0':
            print("'Exit' selected")
            break
        else:
            print("Please enter a valid selection")
          
                

if __name__ == "__main__":
    main()
