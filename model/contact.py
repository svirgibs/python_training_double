from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, address=None, email=None, email2=None, email3=None,
                 all_emails_from_home_page=None,
                 homephone=None, workphone=None,
                 mobilephone=None, secondaryphone=None, all_phones_from_home_page=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "{}:'{} {}'".format(self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

