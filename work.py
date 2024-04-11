class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, last_name, first_name, middle_name, phone_number):
        self.contacts.append({
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'phone_number': phone_number
        })

    def search_contact(self, key, value):
        found_contacts = []
        for contact in self.contacts:
            if contact.get(key) == value:
                found_contacts.append(contact)
        return found_contacts

    def export_to_txt(self, file_name):
        with open(file_name, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact['last_name']} {contact['first_name']} {contact['middle_name']} {contact['phone_number']}\n")

    def import_from_txt(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                data = line.split()
                self.add_contact(data[0], data[1], data[2], data[3])

    def copy_contact(self, source_file_name, dest_file_name, line_number):
        with open(source_file_name, 'r') as source_file:
            lines = source_file.readlines()
            if 0 < line_number <= len(lines):
                with open(dest_file_name, 'a') as dest_file:
                    dest_file.write(lines[line_number - 1])

# Пример использования
phone_book = PhoneBook()
phone_book.add_contact("Иванов", "Иван", "Иванович", "+79123456789")
phone_book.export_to_txt("phonebook.txt")
phone_book.import_from_txt("phonebook.txt")
search_result = phone_book.search_contact('last_name', 'Иванов')
print(search_result)

# Копирование данных из одного файла в другой
phone_book.copy_contact("phonebook.txt", "new_phonebook.txt", 1)