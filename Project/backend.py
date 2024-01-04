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

@eel.expose
def load_contacts():
    try:
        with open(contacts_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

@eel.expose
def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent = 4)

@eel.expose
def search_contacts(search_query):
    contacts = load_contacts()
    return [contact for contact in contacts if search_query.lower() in contact['name'].lower()]

@eel.expose
def sort_contacts(contacts,sort_key = 'name'):
    return sorted(contacts, key = lambda contact: contact.get(sort_key, '').lower())

@eel.expose
def add_contact(name, phone, email, address):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone,  "email": email, "address": address})
    save_contacts(contacts)


eel.init('frontend')

if __name__ == "__main__":
    eel.start('main.html')
