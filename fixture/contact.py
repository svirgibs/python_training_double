from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.init_add_contact()
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("middlename", contact.middlename)
        self.app.change_field_value("lastname", contact.lastname)
        self.app.change_field_value("home", contact.homephone)
        self.app.change_field_value("work", contact.workphone)
        self.app.change_field_value("mobile", contact.mobilephone)
        self.app.change_field_value("phone2", contact.secondaryphone)
        self.submit_create()
        self.return_to_homepage()
        self.contact_cache = None

    def modify_contact_by_index(self, index, contact):
        self.open_home()
        self.init_modify_contact_by_index(index)
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("middlename", contact.middlename)
        self.app.change_field_value("lastname", contact.lastname)
        self.submit_update()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        self.select_contact_by_index(index)
        self.submit_deletion()
        self.delete_alert_accept()
        wd.find_element("css selector", "div.msgbox")
        self.open_home()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_first(self, contact):
        self.modify_contact_by_index(0, contact)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name", "selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements("name", "selected[]"))

    def init_modify_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("xpath", "//img[@title='Edit']")[index].click()

    def init_modify_first_contact(self):
        wd = self.app.wd
        wd.find_element("xpath", "//img[@title='Edit']").click()

    def init_add_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements("name", "submit")) > 0):
            wd.find_element("link text", "add new").click()

    def open_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements("name", "searchstring")) > 0):
            wd.find_element("link text", "home").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element("link text", "home page").click()

    def submit_create(self):
        wd = self.app.wd
        wd.find_element("name", "submit").click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element("name", "update").click()

    def submit_deletion(self):
        wd = self.app.wd
        wd.find_element("xpath", "//input[@value='Delete']").click()

    def delete_alert_accept(self):
        wd = self.app.wd
        wd.switch_to.alert.accept()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        row = wd.find_elements("name", "entry")[index]
        cell = row.find_elements("tag name", "td")[7]
        cell.find_element("tag name", "a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        row = wd.find_elements("name", "entry")[index]
        cell = row.find_elements("tag name", "td")[6]
        cell.find_element("tag name", "a").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home()
            self.contact_cache = []
            for row in wd.find_elements("name", "entry"):
                tds_list = row.find_elements("css selector", "td")
                contact_id = row.find_element("name", "selected[]").get_attribute("value")
                all_phones = tds_list[5].text.splitlines()
                self.contact_cache.append(Contact(lastname=tds_list[1].text, firstname=tds_list[2].text, id=contact_id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element("name", "firstname").get_attribute("value")
        lastname = wd.find_element("name", "lastname").get_attribute("value")
        id = wd.find_element("name", "id").get_attribute("value")
        homephone = wd.find_element("name", "home").get_attribute("value")
        workphone = wd.find_element("name", "work").get_attribute("value")
        mobilephone = wd.find_element("name", "mobile").get_attribute("value")
        secondaryphone = wd.find_element("name", "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element("id", "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)