# imports classes
# store to be used for sending and retrieving information from the DBMS

from habits import habits
from check import time
from store import store
from analytics import analytics
from hashlib import sha256  # constructor method for the hash algorithm


# definition of user class
# user class inherits properties and functions from store,
class user(habits, time, store, analytics):
    '''User Class.
    This class is in charge to deal with the information of the user.
    It inherits habits, time, store, and analytics class; it imports hashlib for the hashing of the password'''

    # defines constructor
    def __init__(self, name: str = '', lastName: str = '', email: str = '', password: str = '', iduser: int = None):
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password
        self.iduser = iduser

        # initiates child store
        habits.__init__(self)

        # initiates child time
        time.__init__(self)

        # initiates store
        store.__init__(self)

    def checkPasswordEmail(self):
        '''
        Checks if the input password & email coincide with the ones stored in the database.
        Requires only the password & userName properties.
        password as string with not limitations whatosever.
        email as string with no limitations whatsoever.
        Only valid for users with an account.
        '''
        # looks up for the given values in the list and checks whether they coincede or not
        list = self.loadPass()
        password = self.hashString()
        for tup in list:

            if password in tup and self.email in tup:
                # informs that the password and the e-mail coincide
                print('The password and e-mail were correct')

                # fills up the missing properties
                self.iduser = tup[0]
                self.name = tup[1]
                self.lastName = tup[2]

                print('Welcome back {} {}'.format(self.name, self.lastName))
                return True

        print('Password or E-mail are not in the database, try again')
        return False

    def addNewUser(self) -> None:
        '''
        Adds a new user to the database. All properties are required.
        Takes the inputs and send them to the database.
        Only valid for user without account
        '''

        # gets the hashed password
        password = self.hashString()

        # sets user information in the DBMS
        self.iduser = self.addRecordsUsers(
            self.name, self.lastName, self.email, password)

        # informs that the action was succefully done
        print('New user has been added')

    # deletes an existing user from the database
    def deleteUser(self) -> None:
        '''deletes an user, it does not require inputs'''

        list = self.loadPass()
        password = self.hashString()
        for tup in list:

            if password in tup:
                self.deleteRecord('user', 'iduser', tup(0))
                print('user "{}" has been deleted'.format(self.name))
                return

    def hashString(self) -> str:
        '''Retrieves the hash string from the password'''
        # hashes the password to protect the user information in case of a breach
        passw = sha256()
        passw.update((self.password).encode('utf-8'))
        password = passw.hexdigest()  # gets the hash in the "hash" variable

        # returns hashed password
        return password
