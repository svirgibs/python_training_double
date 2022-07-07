from model.group import Group


def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="123123123", header="123123", footer="123123"))
    app.session.logout()