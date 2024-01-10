
var sortedAlphabet = true;

async function getContacts(){

    var contacts = await eel.passContacts()();

    if (sortedAlphabet){
        contacts = contacts.sort();
    } else {
        contacts = contacts.sort().reverse();
    }

    for (var i = 0; i < contacts.length; i++){

        const button1 = document.createElement('div');

        button1.addEventListener("click", function (e) {
            if (e.target.className){
                removeContact(e.target.parentNode.children[0].innerHTML);
            } else {
                removeContact(e.target.parentNode.parentNode.children[0].innerHTML);
            }
        });

        const button1Text = document.createElement('span');
        button1Text.innerHTML = 'X';
        button1.appendChild(button1Text)
        button1.className = 'book-action';

        const parent = document.getElementsByClassName('book-contacts')[0];

        const container = document.createElement('div');
        container.className = 'book-contact';

        var name = document.createElement('span');
        name.innerHTML = contacts[i];

        container.appendChild(name)
        container.appendChild(button1);

        parent.appendChild(container);
    }
}

function setListener(){
    const input = document.getElementsByClassName("book-input")[0];
    input.addEventListener("keydown", function (e) {
        if (e.code === "Enter") {
            search(input.value);
        }
    });
    const addButton = document.getElementsByClassName("book-add-container")[0];
    addButton.addEventListener("click", function () {
        document.getElementsByClassName("modal-container")[0].style.display = 'grid';
    });
    const sortButton = document.getElementsByClassName("book-sort-container")[0];
    sortButton.addEventListener("click", function () {
        sort();
    });
    const closeButton = document.getElementsByClassName("modal-title")[0].children[1];
    closeButton.addEventListener("click", function () {
        document.getElementsByClassName("modal-container")[0].style.display = 'none';
    });
    const modalSubmitButton = document.getElementsByClassName("modal-button")[0];
    modalSubmitButton.addEventListener("click", function () {
        addContact(document.getElementsByClassName("modal-input")[0].value);
    });
    const inputModal = document.getElementsByClassName("modal-input")[0];
    inputModal.addEventListener("keydown", function (e) {
        if (e.code === "Enter") {
            addContact(inputModal.value);
        }
    });
}

async function addContact(name){
    await eel.addContact(name)();
    const parent = document.getElementsByClassName('book-contact');
    const contacts = [...parent];
    for (var i = 0; i < contacts.length; i++){
        contacts[i].remove();
    }
    getContacts();
}

async function removeContact(name){
    await eel.removeContact(name)();
    const parent = document.getElementsByClassName('book-contact');
    const contacts = [...parent];
    for (var i = 0; i < contacts.length; i++){
        contacts[i].remove();
    }
    getContacts();
}

async function search(text){
    const foundContact = await eel.searchContact(text)();
    if (foundContact){
        const parent = document.getElementsByClassName('book-contact');
        const contacts = [...parent];
        for (var i = 0; i < contacts.length; i++){
            const name = contacts[i].children[0].innerHTML;
            if (name !== foundContact){
                contacts[i].remove();
            }
        }
    } else {
        const parent = document.getElementsByClassName('book-contact');
        const contacts = [...parent];
        for (var i = 0; i < contacts.length; i++){
            contacts[i].remove();
        }
        getContacts();
    }
}

function sort(){
    if (sortedAlphabet){
        sortedAlphabet = false;
    } else {
        sortedAlphabet = true;
    }
    const parent = document.getElementsByClassName('book-contact');
        const contacts = [...parent];
        for (var i = 0; i < contacts.length; i++){
            contacts[i].remove();
        }
        getContacts();
}

window.onload = () => {
    getContacts();
    setListener();
};