from phonebook_example.protos import addressbook_pb2


def get_a_person(id, name, email, phone_number):
    person = addressbook_pb2.Person()
    person.id = id
    person.name = name
    person.email = email

    phone = person.phones.add()
    phone.number = phone_number
    phone.type = addressbook_pb2.Person.HOME

    return person


address_book = addressbook_pb2.AddressBook()
address_book.people.append(get_a_person(1001, 'Name1', 'email@gmail.com', '9876541212'))
address_book.people.append(get_a_person(1002, 'Name2', 'email2@gmail.com', '9876541213'))

FILEPATH = 'phonebook.bin'
with open(FILEPATH, "wb") as f:
    bytesAsString = address_book.SerializeToString()
    f.write(bytesAsString)
    print(f"Wrote to {FILEPATH}.")
