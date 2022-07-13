import random
from model.contact import Contact


def test_mod_first_contact(app, db, check_ui):
    if list(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = db.get_contact_list()
    mod_contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov")
    contact = random.choice(old_contacts)
    mod_contact.id = contact.id
    old_contacts.remove(contact)
    app.contact.modify_contact_by_id(contact.id, mod_contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(mod_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(),
                                                                     key=Contact.id_or_max)
