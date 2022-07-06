
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.init_add_contact()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys(contact.middlename)
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()

    def init_add_contact(self):
        wd = self.app.wd
        wd.find_element("link text", "add new").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element("link text", "home page").click()