import re
from pprint import pprint
import csv


def read_file(file):
    with open(file, 'r', encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
    return contacts_list


#  +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;


def refactor_phone_numbers(contacts):
    final_contacts = []
    for contact in contacts:
        phone_pattern = re.compile(
            r'(8|\+7)\s*\(*(\d{3})\)*\-*\s*(\d{3})\-*(\d{2})\-*(\d{2})\s*\(*(\w{3}\.*)*\s*(\d{4})*\)*')
        new_phone = r'+7(\2)\3-\4-\5 \6\7'
        name = ' '.join(contact[:3]).split(' ')[:3]
        name.append(contact[3])
        name.append(contact[4])
        new_phone = phone_pattern.sub(new_phone, contact[5])
        name.append(new_phone.strip())
        name.append(contact[6])
        final_contacts.append(name)
    return final_contacts


def delete_dublicates(contact_book):
    contact_dict = {}
    for contact in contact_book:
        my_tuple = (contact[0], contact[1])
        my_contacts = [my_tuple, contact[2:]]
        if my_contacts[0] not in contact_dict:
            contact_dict[my_contacts[0]] = my_contacts[1]
        else:
            for i in range(len(contact_dict[my_contacts[0]])):
                if my_contacts[1][i] and my_contacts[1][i] != contact_dict[my_contacts[0]][i]:
                    contact_dict[my_contacts[0]][i] = my_contacts[1][i]
    new_contact_book = []
    for key, values in contact_dict.items():
        new_contact_book.append(list(key) + values)
    return new_contact_book


def write_in_file(contacts_list):
    with open("phonebook.csv", "w", encoding='UTF-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


book = read_file('phonebook_raw.csv')
contacts = refactor_phone_numbers(book)
new_book = delete_dublicates(contacts)
write_in_file(new_book)
