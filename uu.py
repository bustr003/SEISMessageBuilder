#uu.py

# Functions to handle user interaction with menu options
def key_to_value(target, dict):
    for key, value in dict:
        if target == key:
            target = value
            return target
        
def print_dict(dict):
    for key, value in dict:
        print(f"{key}: {value}")

# Determine what type of uu it is
print("STATUS TYPE")
status_dict = [("1", "Unaffirmed"),
             ("2", "Unsigned")]
print_dict(status_dict)
status_type = input("Enter a number: ")

status_type = key_to_value(status_type, status_dict)

# Determine which type of meeting it is
print("\nMEETING TYPE")
meet_dict = [("1", "IEP"),
             ("2", "Amendment")]
print_dict(meet_dict)
meet_type = input("Enter a number: ")

meet_type = key_to_value(meet_type, meet_dict)

# Determine the email subject
today = input("\nToday's date: ")

subject = status_type + " " + meet_type + " Check-In"
print(f"{today} {subject.upper()}")

# Get the data as a long string
import uu_string as infile
data_long = infile.csv_string

# Separate the data into lines
data_list = data_long.split("\n")

# Print each line as an email
for i in range(1, len(data_list)-1):
    case = data_list[i]
    detail = case.split(",")
    seis_id = detail[0]
    L_name = detail[1]
    F_name = detail[2]
    cm = detail[3]
    date = detail[4]

    cm_split = cm.split(" ")

    print(f"\n{i}==========================")
    print(f"TO: {cm}")
    print(f"SUBJECT: {subject}")
    print(f"\nDear {cm_split[0]},\nYou are receiving this email because there is an {status_type} {meet_type} for a student on your caseload.")

    print(f"\nStudent Name: {F_name} {L_name}")
    print(f"SEIS ID: {seis_id}")

    action = status_type[2:(len(status_type))]
    print(f"\nCan you please check in to let me know if this {meet_type} is ready to be {action}?\nFeel free to contact me if you have any questions or concerns.")

    if (i>0) and ((i+1)%10 == 0):
        print(f"\n!*!*!*!*!*!*!*!*!*!*!\n{i+1} out of {len(data_list)-2} emails have been drafted. Load more emails?")
        more = input("Enter y or n: ")
        if more != "y":
            break

#EOF: uu.py