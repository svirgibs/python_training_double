# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Denis", middlename="Timurovich", lastname="Iavorskii"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname=""))

