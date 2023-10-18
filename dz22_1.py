from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        self.value = value

    def is_phone_number (self, value):
        self.value = value
        digits = re.findall(r"\d+", self.value)
        number = ''
        for digit in digits:
            number += digit
        if len(number) == len(self.value) and len(number) == 10:
            return True
        else:
            return False
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phone = Phone(number)
        if self.phone.is_phone_number:
            self.phones.append(self.phone)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return number
#                print(f"{self.name} phone #{number} was found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):
        self.book = UserDict()

    def add_record(self, record):
        self.book[record.name] = record.phones
    
    def find_record(self, name):
        record = Record(name)
        for key, val in self.book.items():
            if record.name.value == key.value:
                record.phones = val
        return record
    
    def delete_record(self, name):
        record = Record(name)
        for key in self.book:
            if record.name.value == key.value:
                store = key
        self.book.pop(store)

    def __str__(self):
        s = ''
        for key in self.book:
            name = key
            phones = self.book[key]
            s += f"Contact name: {name.value}, phones: {'; '.join(p.value for p in phones)}\n"
        return s



book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
jane_record = Record("Jane")
jane_record.add_phone("2222222222")
jane_record.add_phone("2222223333")
print(john_record)
print(jane_record)

book.add_record(john_record)
book.add_record(jane_record)


john = book.find_record('John')
#print(john)
john.edit_phone("1234567890", "1112223333")
#print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

print(book)
for name, record in book.book.items():
       print(record)
book.delete_record("Jane")
print(book)


# new_r = Record('Alex')
# new_r.add_phone('1111111111')
# new_r.add_phone('2222222222')
# new_r.add_phone('3333333333')
# print(new_r)
# new_r.remove_phone('2222222222')
# print(new_r)
# new_r.edit_phone('3333333333', '7777777777')
# print(new_r)
# new_r.find_phone('7777777777')
