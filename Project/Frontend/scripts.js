async function getContacts(){
    const contacts = await eel.passContacts()();

    for (var i = 0; i < contacts.length; i++){
        //Loon helista nupu
        const button1 = document.createElement('div');
        const button1Text = document.createElement('span');
        button1Text.innerHTML = 'Helista';
        button1.appendChild(button1Text)
        button1.className = 'book-action';

        //Leian peamise konteineri
        const parent = document.getElementsByClassName('book-contacts')[0];

        //Loon kontakti konteineri
        const container = document.createElement('div');
        container.className = 'book-contact';

        //Loon kontatki nime
        var name = document.createElement('span');
        name.innerHTML = contacts[i];

        //Lisan kontatki andmed kontaki konteinerile
        container.appendChild(name)
        container.appendChild(button1);

        //Lisan kontatki peamisele konteinerile
        parent.appendChild(container);
    }
}

getContacts();

function submitSearch(){
    const input = document.getElementsByClassName("book-input")[0];
    input.addEventListener("keydown", function (e) {
        if (e.code === "Enter") {
            //Python otsimise funktsiooni kutsumine siia
        }
    });
}