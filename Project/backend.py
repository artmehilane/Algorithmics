import eel
import json

def get_data():
    with open('contacts.json', 'r') as openfile:
        return json.load(openfile)

contacts = get_data()

@eel.expose
def passContacts():
    return contacts
    
@eel.expose
def searchContact(text):
    for contact in contacts:
        if contact.lower() == text.lower():
            #Contact found
            return contact


@eel.expose
def addContact(name):
    contacts.append(name.capitalize())
    with open('contacts.json', 'w') as openfile:
        return json.dump(contacts, openfile)
 
@eel.expose
def removeContact(name):
    contacts.remove(name.capitalize())
    with open('contacts.json', 'w') as openfile:
        return json.dump(contacts, openfile)   

eel.init('frontend')
eel.start('main.html')