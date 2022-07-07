from model.contact import Contact


def test_mod_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))
    app.session.logout()