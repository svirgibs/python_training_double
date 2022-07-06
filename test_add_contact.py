# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_add_contact(wd)
        self.create_contact(wd, firstname="Denis", middlename="Timurovich", lastname="Iavorskii")
        self.go_to_homepage(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_add_contact(wd)
        self.create_contact(wd, firstname="", middlename="", lastname="")
        self.go_to_homepage(wd)
        self.logout(wd)

    def go_to_homepage(self, wd):
        wd.find_element("link text", "home page").click()

    def create_contact(self, wd, firstname, middlename, lastname):
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(firstname)
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys(middlename)
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(lastname)
        wd.find_element("name", "nickname").click()
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()

    def init_add_contact(self, wd):
        wd.find_element("link text", "add new").click()

    def login(self, wd, username, password):
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def logout(self, wd):
        wd.find_element("link text", "Logout").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

