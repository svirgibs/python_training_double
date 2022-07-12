from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, homephone=None, workphone=None,
                 mobilephone=None, secondaryphone=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.id = id

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

