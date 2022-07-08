from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.init_add_contact()
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("middlename", contact.middlename)
        self.app.change_field_value("lastname", contact.lastname)
        self.submit_create()
        self.return_to_homepage()

    def modify_first(self, contact):
        self.open_home()
        self.init_modify_first_contact()
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("middlename", contact.middlename)
        self.app.change_field_value("lastname", contact.lastname)
        self.submit_update()
        self.return_to_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home()
        self.select_first_contact()
        self.submit_deletion()
        self.delete_alert_accept()
        wd.find_element("css selector", "div.msgbox")
        self.open_home()

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements("name", "selected[]"))

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()

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

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home()
        contacts = []
        for element in wd.find_elements("name", "entry"):
            list_tds = element.find_elements("css selector", "td")
            contact_id = element.find_element("name", "selected[]").get_attribute("value")
            contacts.append(Contact(lastname=list_tds[1].text, firstname=list_tds[2].text, id=contact_id))
        return contacts
