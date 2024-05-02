import re
import os

def contactManagement():
    print("Welcome to the Contact Management System! \nmenu:")
    menu = "1: Add a new Contact\n2: Edit an existing contact\n3: Delete a contact\n4: Search for a contact\n5: Display all contacts\n6: Export contacts to a text file\n7: Import contacts from a text file\n8: Quit "
    updates = {}
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
                while True:
                    unique_identifier = input("Enter Phone or Email for Identifier: (enter 'done' when finished) ")
                    phone_match = r"\b\d{1,10}\b"
                    phone_match_res = re.findall(phone_match, unique_identifier)
                    email_match = r"[a-zA-Z0-9._$%+-]+@[a-zA.-Z]+\.[a-zA-Z]{2,}"
                    email_match_res = re.findall(email_match, unique_identifier)
                    
                    if unique_identifier.lower() == 'done':
                        print(f"Contact Info: {contact_info}")
                        break

                    if phone_match_res:
                        number = phone_match_res[0]
                        contact_info[number] = []
                        print("Added Phone: ", number)

                    if email_match_res:
                        email = email_match_res[0]
                        contact_info[email] = []
                        print("Added Email: ", email)

                    if not (phone_match_res or email_match_res) and unique_identifier.lower() != 'done':
                        print("Invalid Input: Enter Valid Email or Phone Number")
    
                    while True:
                        try:    
                            additonal_info = input("add more info enter Name, Phone or Email: (enter 'done' when finished) ")
                            additonal_phone = re.findall(phone_match, additonal_info)
                            additonal_email = re.findall(email_match, additonal_info)
                            name_match = r'[A-Za-z]+ [A-Za-z]+'
                            contact_name = re.findall(name_match, additonal_info)
                            
                            if additonal_info.lower() == 'done':
                                print(f"Contact Info: ', {contact_info}")
                                break
                            
                            if contact_name:
                                name = contact_name[0]
                                for identifier, value in contact_info.items():
                                    if isinstance(contact_info[identifier],dict):
                                        updates.setdefault(identifier, {}).update({"Name": name})
                                    else:
                                        updates[identifier] = {"Name": name}
                            
                            elif additonal_email:
                                email = additonal_email[0]
                                for identifier, value in contact_info.items():
                                    if isinstance(contact_info[identifier],dict):
                                        updates.setdefault(identifier,{}).update({"Email": email})
                                    else:
                                       updates[identifier] = {"Email": email}

                            elif additonal_phone:
                                phone = additonal_phone[0]
                                for identifier, value in contact_info.items():
                                    if isinstance(contact_info[identifier], dict):
                                        updates.setdefault(identifier, {}).update({"Phone": phone})
                                    else:
                                        updates[identifier] = {"Phone": phone}
                            contact_info.update(updates)      
                        except Exception as e:
                            print(f"An error occured: {e} Please try again.")
           
           
            if menuOption == 2:
                while True:
                    to_edit = input("edit Phone, Email, or Name?: (enter 'done' when finished) ").lower().strip()
                    email_match = r"[a-zA-Z0-9._$%+-]+@[a-zA.-Z]+\.[a-zA-Z]{2,}"
                    name_match = r'[A-Za-z]+ [A-Za-z]+'

                    email_match_res = re.findall(email_match, to_edit)
                    name_match_res = re.findall(name_match, to_edit)
                    
                    if to_edit == 'phone':
                        
                            for identifier, inner_information in contact_info.items():
                                print("Key: ", identifier)
                                print("Value: ", inner_information)
                                
                                if "Phone" in inner_information:
                                    while True:
                                        phone_exists = input("Phone exists do you want to replace or add?: (enter 'no' ) ").lower()
                                        if phone_exists == "no":
                                            print(inner_information)
                                            break
                                        if phone_exists == "add":
                                            add_phone = input("enter phone ")
                                            phone_match = r"\b\d{1,10}\b"
                                            phone_match_res = re.findall(phone_match, add_phone)

                                            if phone_match_res:
                                                phone_number = phone_match_res[0]
                                                current_number = inner_information.values()
                                                inner_information = {"Phone": current_number, phone_number}

                                               
                                                    
                                        else:
                                            pass

                            


            # else:
            #     pass
        except ValueError:
            print("response needs to be a integer between")
            












contactManagement()