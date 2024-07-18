from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def delete_phone(self, number):
        for num in self.phones:
            if num.value == number:
                self.phones.remove(num)
                break

    def edit_phone(self, old_number, new_number):
        for num in self.phones:
            if num.value == old_number:
                num.value = new_number
                break

    def find_phone(self, number):
        for num in self.phones:
            if num.value == number:
                return num.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            return self.data.pop(name)

    def __str__(self):
        records = []
        for record in self.values():
            records.append(str(record))
        return '\n'.join(records)