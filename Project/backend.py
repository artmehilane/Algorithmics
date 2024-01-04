import json
import eel

@eel.expose
def passContacts():
    return contacts


@eel.expose
def searchContact():
    print('ran')


eel.init('frontend')
eel.start('main.html')



contacts_file = 'contacts.json'

def load_contacts():
    try:
        with open(contacts_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent = 4)

def search_contacts(contacts, search_query):
    return [contact for contact in contacts if search_query.lower() in contact['name'].lower()]

def sort_contacts(contacts,sort_key = 'name'):
    return sorted(contacts, key = lambda contact: contact.get(sort_key, '').lower())

def add_contact(contacts, name, phone, email, address):
    contacts.append({"name": name, "phone": phone,  "email": email, "address": address})
    save_contacts(contacts)


def main():
    contacts = load_contacts()

    add_contact(contacts,  "Mart Herilane", "74065663", "mart.herilane@outlook.com", "Vase 22")

    print("Search Results for 'Mart':")
    print(search_contacts(contacts, "Mart"))

    print("Contacts sorted by name:")
    print(sort_contacts(contacts))

if __name__ == "__main__":
    main()
