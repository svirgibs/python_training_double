# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("firstname", 7),
            middlename=random_string("middlename", 7),
            lastname=random_string("lastname", 7),
            address=random_string("address", 20),
            homephone="+7" + random_digits(10),
            workphone="+7" + random_digits(10),
            mobilephone="+7" + random_digits(10),
            secondaryphone="+7" + random_digits(10),
            email=random_string("email", 9) + "@gmail.com",
            email2=random_string("email", 9) + "@yandex.com",
            email3=random_string("email", 9) + "@bk.com")
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
