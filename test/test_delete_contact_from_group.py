from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app):
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contac.create(Contact(firstname="firstname_1"))
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))

    new_group_list = db.get_group_list()
    new_contact_list = db.get_contact_list()
    group = random.choice(new_group_list)
    old_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))

    if len(old_contacts_in_group) == 0:
        contact = random.choice(new_contact_list)
        app.contact.add_contact_into_group(id=contact.id, group_id=group.id)
    old_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    old_contacts_not_in_group = db.get_contacts_not_in_group(Group(id=group.id))

    contact_del = random.choice(old_contacts_in_group)
    app.contact.remove_contact_from_group(id=contact_del.id, gr_id=group.id)
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    new_contacts_not_in_group = db.get_contacts_not_in_group(Group(id=group.id))

    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
    assert len(old_contacts_not_in_group) + 1 == len(new_contacts_not_in_group)
    old_contacts_in_group.remove(contact_del)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)