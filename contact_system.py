import re
import os

def contactManagement():
    print("Welcome to the Contact Management System! \nmenu:")
    menu = "1: Add a new Contact\n2: Edit an existing contact\n3: Delete a contact\n4: Search for a contact\n5: Display all contacts\n6: Export contacts to a text file\n7: Import contacts from a text file\n8: Quit "
    
    contact_info = {}
    
    while True:
        print(menu)
        try:
            menuOption = int(input("Choose a menu option: 1-8 "))
            if menuOption == 8:
                print("Thank you for your service!")
                break
            if menuOption not in range(1,8):
                print("Invalid Response: choice needs to be number between 1 - 8")
            
            if menuOption == 1:
                unique_identifier = input("Enter Phone or Email for Identifier: ")
                phone_match = r"\b\d{1,10}\b"
                phone_match_res = re.findall(phone_match, unique_identifier)
                email_match = r"[a-zA-Z0-9._$]+@[a-zA-Z]\.[a-zA-Z]{2,}"
                email_match_res = re.findall(email_match, unique_identifier)
                
                for number in phone_match_res:
                    for email in email_match_res:
                        print(f"email:\n{email}")
                
            else:
                pass
        except ValueError:
            print("response needs to be a integer between")
            












contactManagement()