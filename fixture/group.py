from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element("link text", "group page").click()

    def create(self, group):
        self.open_groups_page()
        self.init_group_creation()
        self.fill_group_form(group)
        self.submit_group_creation()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        self.open_groups_page()
        self.select_first_group()
        self.open_modification_form()
        self.fill_group_form(new_group_data)
        self.submit_update()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.open_groups_page()
        self.select_first_group()
        self.submit_deletion()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements("name", "new")) > 0):
            wd.find_element("link text", "groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements("name", "selected[]"))

    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element("name", "new").click()

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element("name", "submit").click()

    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element("name", "edit").click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element("name", "update").click()

    def submit_deletion(self):
        wd = self.app.wd
        wd.find_element("name", "delete").click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements("css selector", "span.group"):
                text = element.text
                id = element.find_element("name", "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
