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
                while True:
                    unique_identifier = input("Enter Phone or Email for Identifier: (enter 'done' when finished) ")
                    phone_match = r"^\d{10}$"
                    phone_match_res = re.findall(phone_match, unique_identifier)
                    email_match = r"[a-zA-Z0-9._$%+-]+@[a-zA.-Z]+\.[a-zA-Z]{2,}"
                    email_match_res = re.findall(email_match, unique_identifier)
                    
                    if unique_identifier.lower() == 'done':
                        print(f"Contact Info: {contact_info}")
                        break
                        
                    if phone_match_res:
                        number = phone_match_res[0]
                        if number in contact_info:
                            print(f"Error: {number} already in system")
                            continue
                        else:
                            contact_info[number] = {}
                            print("Added Phone: ", number)

                    if email_match_res:
                        email = email_match_res[0]
                        if email in contact_info:
                            print(f"Error: {email} already in system")
                            continue
                        else:
                            contact_info[email] = {}
                            print("Added Email: ", email)

                    if not (phone_match_res or email_match_res) and unique_identifier.lower() != 'done':
                        print("Invalid Input: Enter Valid Email or Phone Number")
                        continue
                    
                    
                    while True:
                        try:    
                            additonal_info = input("type 'Name', 'Email' or 'Phone' to add more info: (enter 'done' when finished) ").lower()
                            
                            if additonal_info == 'done':
                                print(f"Contact Info: ', {contact_info}")
                                break
                            
                            if additonal_info == 'name':
                                enter_name = input("Enter Name: ")
                                name_match = r'[A-Za-z]+ [A-Za-z]+'
                                contact_name = re.findall(name_match, enter_name)

                                if contact_name:
                                    name = contact_name[0]
                                    for identifier, inner_information in contact_info.items():
                                        if "Name" not in inner_information:
                                            inner_information["Name"] = name
                                            print(contact_info)
                                        else:
                                            print("Name already exists for contact")
######################################################################################                    
                            if additonal_info == 'email':
                                enter_email = input("Enter Email: ")
                                additonal_email = re.findall(email_match, enter_email)

                                if additonal_email:
                                    email = additonal_email[0]
                                    for identifier, inner_information in contact_info.items():
                                        if "Email" not in inner_information:
                                            inner_information["Email"] = email
                                            print(contact_info)
                                        else:
                                            print("Email already exists")
                                else:
                                    print("Please check email.")
                                    continue
##################################################################################                                
                            if additonal_info == "phone":
                                enter_phone = input("Enter Phone: ")
                                additonal_phone = re.findall(phone_match, enter_phone)

                                if additonal_phone:
                                    phone_number = additonal_phone[0]
                                    for identifier, inner_information in contact_info.items():
                                        if "Phone" not in inner_information:
                                            inner_information["Phone"] = phone_number
                                        else:
                                            print("Phone number already exists")

                                else:
                                    print("make sure to enter a phone number")
                                    continue
                                            
                                
                            if additonal_info not in ["name", "email", 'phone']:
                                print("Invalid Response: enter 1 of the 3 options")
                            
                  
                        except Exception as e:
                            print(f"An error occured: {e} Please try again.")
           
##############################################################
        
            if menuOption == 2:

                phone_match = r"^\d{10}$"
                name_match = r'[A-Za-z]+ [A-Za-z]+'
                email_match = r"[a-zA-Z0-9._$%+-]+@[a-zA.-Z]+\.[a-zA-Z]{2,}"

                # email_match_res = re.findall(email_match, unique_identifier)
                # contact_name = re.findall(name_match, enter_name)

                while True:
                    print(contact_info)
                    which_identifier = input("Enter Identifier to edit: (enter 'done' when finished) ").lower()
                    
                    if which_identifier == 'done':
                        print(contact_info)
                        break

                    for identifier, inner_information in contact_info.items():
                        if which_identifier == identifier:
                            while True:
                                add_or_replace = input("\nenter 'add' or 'replace *information type*:\n(ex 'add phone, replace email):\n\n(enter 'done' when finished)\n").lower().strip()
                                if add_or_replace == 'done':
                                    break

                                if add_or_replace == 'add phone':
                                    if 'Phone' in inner_information:
                                        print(f"Phone: {inner_information['Phone']}")
                                        replace_information = input("information exists replace it?: ").lower()
                                        
                                        if replace_information == "yes":
                                            while True:
                                                enter_phone = input("Enter Phone: ")
                                                phone_match_res = re.fullmatch(phone_match, enter_phone)
                                                if phone_match_res:
                                                    phone_number = phone_match_res[0]
                                                    inner_information["Phone"] = phone_number
                                                    print(inner_information)
                                                    break
                            
                                                else:
                                                    print("Phone needs to be entered like: 0123456789\ntry again")
                                                    continue
                                    
                                    else:
                                        enter_phone = input("Enter Phone: ")
                                        phone_match_res = re.fullmatch(phone_match, enter_phone)
                                        if phone_match_res:
                                            phone_number = phone_match_res[0]
                                            inner_information["Phone"] = phone_number
                                            print(inner_information)
                                            break
##################################################################################
                                if add_or_replace == 'add email':
                                    if 'Email' in inner_information:
                                        print(f"Email: {inner_information['Email']}")
                                        replace_information = input("information exists replace it?: ").lower()
                                        
                                        if replace_information == "yes":
                                            while True:
                                                enter_email = input("Enter Email: ")
                                                email_match_res = re.fullmatch(email_match, enter_email)
                                                if email_match_res:
                                                    email = email_match_res[0]
                                                    inner_information["Email"] = email
                                                    print(inner_information)
                                                    break
                            
                                                else:
                                                    print(f"Invalid Email: {enter_email}\ntry again")
                                                    continue
                                    
                                    else:
                                        enter_email = input("Enter Email: ")
                                        email_match_res = re.fullmatch(email_match, enter_email)
                                        if email_match_res:
                                            email = email_match_res[0]
                                            inner_information["Email"] = email
                                            print(inner_information)
                                            break
                            
##############################################################################
                                if add_or_replace == 'add name':
                                    if 'Name' in inner_information:
                                        print(f"Name: {inner_information['Name']}")
                                        replace_information = input("information exists replace it?: ").lower()
                                        
                                        if replace_information == "yes":
                                            while True:
                                                enter_name = input("Enter Name: ")
                                                contact_name = re.fullmatch(name_match, enter_name)
                                                if contact_name:
                                                    name = contact_name[0]
                                                    inner_information["Name"] = name
                                                    print(inner_information)
                                                    break
                            
                                                else:
                                                    print(f"please enter a name")
                                                    continue
                                    
                                    else:
                                        enter_name = input("Enter Name: ")
                                        contact_name = re.fullmatch(name_match, enter_name)
                                        if contact_name:
                                            name = contact_name[0]
                                            inner_information["Name"] = name
                                            print(inner_information)
                                            break
                  ##################################################################
                                if add_or_replace == "replace email":
                                    if 'Email' in inner_information:
                                        print(f"Email: {inner_information['Email']}")
                                        while True:
                                            enter_email = input("Enter Email: ")
                                            email_match_res = re.fullmatch(email_match, enter_email)
                                            if email_match_res:
                                                email = email_match_res[0]
                                                inner_information["Email"] = email
                                                print(inner_information)
                                                break
                        
                                            else:
                                                print(f"Invalid Email: {enter_email}\ntry again")
                                                continue

                                    else:
                                        while True:
                                            no_email = input("No email present add one? ").lower()
                                            if no_email == 'no':
                                                print(contact_info)
                                                break

                                            if no_email == 'yes':
                                                enter_email = input("Enter Email: ")
                                                email_match_res = re.fullmatch(email_match, enter_email)
                                                if email_match_res:
                                                    email = email_match_res[0]
                                                    inner_information["Email"] = email
                                                    print(inner_information)
                                                    break
                                                else:
                                                        print(f"Invalid Email: {enter_email}\ntry again")
                                                        continue

                                            else:
                                                print("reply 'yes' or 'no'")
                                                continue
##################################################################################
                                
                                if add_or_replace == "replace name":
                                    if 'Name' in inner_information:
                                        print(f"Name: {inner_information['Name']}")
                                        while True:
                                            enter_name = input("Enter Name: ")
                                            contact_name = re.fullmatch(name_match, enter_name)
                                            if contact_name:
                                                name = contact_name[0]
                                                inner_information["Name"] = name
                                                print(inner_information)
                                                break
                        
                                            else:
                                                print(f"please enter a name")
                                                continue

                                    else:
                                        while True:
                                            no_name = input("No name present add one?: ")
                                            if no_name == "no":
                                                print(contact_info)
                                                break

                                            if no_name == 'yes':
                                                enter_name = input("Enter Name: ")
                                                contact_name = re.fullmatch(name_match, enter_name)
                                                if contact_name:
                                                    name = contact_name[0]
                                                    inner_information["Name"] = name
                                                    print(inner_information)
                                                    break
                        
                                                else:
                                                    print(f"please enter a name")
                                                    continue
                                            
                                            else:
                                                print("reply 'yes' or 'no' ")
                                                continue
###############################################################################################
                                    
                                if add_or_replace == 'replace phone':
                                    if 'Phone' in inner_information:
                                        print(f"Phone: {inner_information['Phone']}")
                                        while True:
                                            enter_phone = input("Enter Phone: ")
                                            phone_match_res = re.fullmatch(phone_match, enter_phone)
                                            if phone_match_res:
                                                phone_number = phone_match_res[0]
                                                inner_information["Phone"] = phone_number
                                                print(inner_information)
                                                break
                        
                                            else:
                                                print("Phone needs to be entered like: 0123456789\ntry again")
                                                continue
                                
                                    else:
                                        while True:
                                            no_phone = input("No phone present add one?: ")
                                            if no_phone == "no":
                                                print(contact_info)
                                                break
                                            if no_phone == "yes":
                                                enter_phone = input("Enter Phone: ")
                                                phone_match_res = re.fullmatch(phone_match, enter_phone)
                                                if phone_match_res:
                                                    phone_number = phone_match_res[0]
                                                    inner_information["Phone"] = phone_number
                                                    print(inner_information)
                                                    break

                                            else:
                                                print("Reply 'yes' or 'no'")
                                                continue
                        else:
                            print(f"Identifier:{which_identifier}\ndoesn't exist try again")
                            continue
#########################################################################################
                        
            if menuOption == 3:
                print(contact_info)
                while True:
                    delete_contact = input("enter identifier to delete: (enter 'done' when finished) \n").lower()
                    if delete_contact == 'done':
                        break

                    if delete_contact in contact_info:
                        confirm_delete = input("are you sure?: ")
                        if confirm_delete == 'yes':
                            del contact_info[delete_contact]
                            print(contact_info)
                        
                        if confirm_delete == 'no':
                            break

                        else:
                            print("Reply 'yes' or 'no' ")
                    else:
                        print(f"Contact {delete_contact} not found check identifier and try again")
                        continue
##################################################################################################

            if menuOption == 4:
                while True:
                    contact_search = input("Search by Identifier or Contact Information?: (enter 'done' when finished)\n").lower()
                    if contact_search == 'done':
                        break

                    if contact_search == "identifier":
                        while True:    
                            enter_identifier = input("Enter identifier: (enter 'done' when finished) ")

                            if enter_identifier == 'done':
                                break

                            if enter_identifier in contact_info:
                                print(contact_info[enter_identifier])
                                break
                            else:
                                print(f"{enter_identifier} is not found, check input and try again")
                                continue
                    
                    if contact_search == 'information':
                        while True:
                            try:
                                enter_information = input("Enter Email, Phone, or Name: ").lower()

                                if enter_information == 'done':
                                    break
                                
                                for identifier, value in contact_info.items():
                                    for contact_type, contact_information in value.items():
                                        if enter_information in contact_information:
                                            print(contact_info[identifier])
                                            break

                                        else:
                                            print("Information not found check spelling")
                                            continue
                            except Exception as e:
                                print("Something went wrong try again")
                                continue


#############################################################
                
            if menuOption == 5:
                while True:
                    view_sorted = input("view sorted?: ").lower()

                    if view_sorted == 'done':
                        break

                    if view_sorted == "yes":
                        contact_info_sorted = sorted(contact_info)
                        print(contact_info_sorted)
                        
                    if view_sorted == 'no':
                        print(contact_info)
                        

                    else:
                        print("Reply with 'yes' or 'no'")
                        continue
#################################################################

            if menuOption == 6:
                while True:
                    export_contacts = input("do you want to export contacts to .txt file?: (enter 'done' when finished) ").lower()
                    
                    if export_contacts == 'done':
                        break
                    
                    if export_contacts == 'no':
                        break

                    if export_contacts == "yes":
                        while True:
                            name_file = input("Name your file: (enter 'done' when finished) ")
                            
                            if name_file.lower() == 'done':
                                break

                            if not os.path.exists(f"{name_file}.txt"):
                                with open(f"{name_file}.txt", "a") as file:
                                    for identifier, inner_information in contact_info.items():
                                        file.write(f"Identifier: {identifier}\n")

                                        for key, value in inner_information.items():
                                            file.write(f"{key}: {value}\n")
                                        file.write("\n")
                            
                            else:
                                with open(f"{name_file}.txt", "w") as file:
                                    for identifier, inner_information in contact_info.items():
                                        file.write(f"Identifier: {identifier}\n")

                                        for key, value in inner_information.items():
                                            file.write(f"{key}: {value}\n")
                                        file.write("\n")


                    else:
                        print("Respond with 'yes' or 'no' ")

################################################################
            if menuOption == 7:
                while True:
                    import_contacts = input("Do you want to import contacts from a file?: (enter 'done' when finished) ")

                    if import_contacts == 'done':
                        break
                    
                    if import_contacts == 'no':
                        break

                    if import_contacts == 'yes':
                        while True:
                            file_name = input("Enter File Name: (enter 'done' when finished)")
                            
                            if file_name.lower() == 'done':
                                break
                            
                            if os.path.exists(f"{file_name}"):
                                with open (f"{file_name}", "r") as file:
                                    for line in file:
                                        print(f"{line}\n")


                            else:
                                print("File not found. try again")
                                continue




        except ValueError:
            print("response needs to be a integer between")
            



contactManagement()