"""
Program Requirements

Write a program to prompt the user for the following:

    First name

    Last name

    Email Address

    Phone Number

    Job Title

    ID Number

Then you should display the information back in this format:

Note that the square brackets [] indicate a value coming from the user and should not be displayed.


----------------------------------------
[LAST NAME], [first name]
[Job title]
ID: [id number]

[email address]
[phone number]
----------------------------------------

In addition to the spacing and punctuation shown above, you must implement the following requirements:

    The last name should be converted from whatever the user types to be displayed in ALL CAPS.

    The job title should be displayed so that the first letter is capitalized.

    The email address should be displayed in all lowercase.

An example of the program running is shown:


Please enter the following information:

First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234
----------------------------------------

"""

print()
exit()

#input
first_name = input("What is your first name? ") #sample - Jane
last_name  = input("What is your last name? ") #sample - Doe
email_address = input("What is your email adress? ") #sample - JaneDoe@email.com
phone_number  = input("What is your phone number? ") #sample - (208) 555-1234
job_title = input("What is your job title? ") #sample - chief software architect
id_number = input("What is your ID Number? ") #sample - 83-23821

#format
last_name_upper = last_name.upper()
job_title_tit = job_title.title()
email_address_lower = email_address.lower()

#show
print("\n\n")
print("The ID Card is:")
print("----------------------------------------")
print(f"{last_name_upper}, {first_name}")
print(f"{job_title_tit}")
print(f"ID: {id_number}")
print("")
print(f"{email_address_lower}")
print(f"{phone_number}")
print("----------------------------------------")