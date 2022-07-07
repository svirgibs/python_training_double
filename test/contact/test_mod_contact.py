from model.contact import Contact


def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.modify_first(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))


def test_mod_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.modify_first(Contact(middlename="Ivanovich"))