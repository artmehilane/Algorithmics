import eel

contacts = ['Teet', 'Taat', 'Andrus', 'Janne', 'Jakob', 'Uudo']

@eel.expose
def passContacts():
    return contacts
    

@eel.expose
def searchContact():
    print('ran')
    
    
eel.init('frontend')
eel.start('main.html')