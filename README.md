# contact_mangement
coding Temple's contact management mini project

Project Requirements
Your task is to develop a Contact Management System with the following features:

#done 
User Interface (UI):

Create a user-friendly command-line interface (CLI) for the Contact Management System.
Display a welcoming message and provide a menu with the following options:

Welcome to the Contact Management System! Menu:
Add a new contact
Edit an existing contact
Delete a contact
Search for a contact
Display all contacts
Export contacts to a text file
Import contacts from a text file
Quit
'>
#done ^

Contact Data Storage:
Use nested dictionaries as the main data structure for storing contact information.
Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
Store contact details within the inner dictionary, including:
Name
Phone number
Email address
Additional information (e.g., address, notes).



Menu Actions:
Implement the following actions in response to menu selections:
Adding a new contact with all relevant details.
Editing an existing contact's information (name, phone number, email, etc.).
Deleting a contact by searching for their unique identifier.
Searching for a contact by their unique identifier and displaying their details.
Displaying a list of all contacts with their unique identifiers.
Exporting contacts to a text file in a structured format.
Importing contacts from a text file and adding them to the system.



User Interaction:
Utilize input() to enable users to select menu options and provide contact details.
Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.



Error Handling:
Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.


GitHub Repository:
Create a GitHub repository for your project.
Commit your code to the repository regularly.
Create a clean and interactive README.md file in your GitHub repository.
Include clear instructions on how to run the application and explanations of its features.
Provide examples and screenshots, if possible, to enhance user understanding.
Include a link to your GitHub repository in your project documentation.
Optional Bonus Points


Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.
Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.
Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.
Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.
Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.



####################################################################

A couple days in as I write this, first steps I took were to do the menu options and get that situated. I then start to focus on the coding to make each option work, just now I believe I am completely finished with option 1 as I have a way to get input on unique identifier and add that as a key; and then ask input on name, email, or phone to add those as key, value pairs but, as values inside unique identifier. Next I will be doing option 2 edit which will let me change, add, or delete the inner key,value pairs.




two days later, I continued to do menu Option 2 but was running into error "An error occured: list indices must be integers or slices, not str Please try again." which led me into seeing the values are being treated as a list and not key-val pair I initialized them as 'contact_info[identifier][Email] = email thinking braket notation would do it but it needed to be done {"Email": email} after figuring that out, I came across an error "An error occured: dictionary changed size during iteration Please try again." which led me to find out about update and .setdefault()





since last entry i was rewriting code in menuOption 1 and 2 mainly 2 as that was completely broken after finding error in the 1:1 with Daniel? the main part of my fixing i enabled the user to add "phone, email, and name" if not present already and if it is present give them an option to replace them. That was done for both "add" *information type* and "replace" *information type*  fixed double printing of contact info I had a print statement after my unique_identifier input... completed menu option 3 and started option 4



completed assignment to the best of my knowledge.