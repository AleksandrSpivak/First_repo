def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        return "Invalid command."

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
    except:
        return "Invalid contact."
    return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone 
            return "Contact updated."
        else:
            return "No such contact."
    except:
        return "No such contact."

def show_phone(args, contacts):
    try:
        name = args
        if name[0] in contacts:
            return contacts[name[0]]
    except:
        return "No such contact."
  
def show_all(contacts):
    all_contacts = ''
    if len(contacts) >0:
        for contact in contacts:
            all_contacts += f"{contact} {contacts[contact]}\n"
        return all_contacts[:-1]
    else:
        return "Empty contact list"
    

#def main():
contacts = {}
print("Welcome to the assistant bot!")
while True:
    user_input = input("Enter a command: ")
    command, *args = parse_input(user_input)

    if command in ["close", "exit"]:
        print("Good bye!")
        break
    elif command == "hello":
        print("How can I help you?")
    elif command == "add":
        print(add_contact(args, contacts))
    elif command == "change":
        print(change_contact(args, contacts))
    elif command == "phone":
        print(show_phone(args, contacts))
    elif command == "all":
        print(show_all(contacts))
    else:
        print("Invalid command.")


# if __name__ == "__main__":
#     main()