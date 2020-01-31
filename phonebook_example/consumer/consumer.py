from phonebook_example.protos import addressbook_pb2


FILEPATH = 'phonebook.bin'


with open(FILEPATH, "rb") as f:
    print(f"Reading from {FILEPATH}.")
    address_book = addressbook_pb2.AddressBook().FromString(f.read())

print(address_book)
