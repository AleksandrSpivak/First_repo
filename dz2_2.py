#errors are handled as a class

import re


class ContactAlreadyExistsError(Exception):
    pass

class ContactDoesNotExistError(Exception):
    pass

class NotPhoneNumberError(Exception):
    pass

class ContactListIsEmptyError(Exception):
    pass


def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except ValueError:
        return "Invalid command."


def is_in_dictionary(string, contacts):
    if string in contacts:
        return True
    else:
        return False


def is_phone_number(string):
    number = re.findall(r"\d+", string)
    if len(number[0]) == len(string):
        return True
    else:
        return False


def input_error(func):
    def inner(*args, **kwargs):
        try:
            [name, phone], contacts = args
            if is_in_dictionary(name, contacts):
                raise ContactAlreadyExistsError
            if not is_phone_number(phone):
                raise NotPhoneNumberError
            return func(*args, **kwargs)
        except ContactAlreadyExistsError:
            return "Such contact already exists"
        except NotPhoneNumberError:
            return "Number should consist of digits"
        except (IndexError, ValueError):
            return "Give me name and phone please."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact_error(func):
    def inner(*args, **kwargs):
        try:
            [name, phone], contacts = args
            if not is_phone_number(phone):
                raise NotPhoneNumberError
            if name not in contacts:
                raise ContactDoesNotExistError
            return func(*args, **kwargs)
        except NotPhoneNumberError:
            return "Number should consist of digits"
        except ContactDoesNotExistError:
            return "No such contact"       
        except ValueError:
            return "Give me name and phone please."      
    return inner


@change_contact_error
def change_contact(args, contacts):
        name, phone = args
        contacts[name] = phone 
        return "Contact updated."


def show_phone_error(func):
    def inner(*args, **kwargs):
        try:
            [name], contacts = args
            if name not in contacts:
                raise ContactDoesNotExistError
            return func(*args, **kwargs)
        except ContactDoesNotExistError:
            return "No such contact"
        except ValueError:
            return "Give me name please."       
    return inner


@show_phone_error
def show_phone(args, contacts):
    [name] = args
    return contacts[name]


def show_all_error(func):
    def inner(*args, **kwargs):
        try:
            contacts, = args
            if len(contacts) == 0:
                raise ContactListIsEmptyError
            return func(*args, **kwargs)
        except ContactListIsEmptyError:
            return "Empty contact list"       
    return inner


@show_all_error
def show_all(contacts):
    all_contacts = ''
    for contact in contacts:
        all_contacts += f"{contact} {contacts[contact]}\n"
    return all_contacts[:-1]


def main():
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


if __name__ == "__main__":
    main()