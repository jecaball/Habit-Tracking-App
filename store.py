from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2

# stores the information in a DBMS
# imports module "psycopg2" to help with communication with the DBMS
# creates the class "store" which is used to saved information in a database managment system


class store:
    '''
    Store class.
    It is in charge of the communication between the modules and the database management system.
    It imports psycopg2 for the connection with the database "Habits"
    '''
    ##
    # DBMS
    # name: HabitsProject
    # Group: Group
    # Connect TImeout: 5000
    # Host: 127.0.0.1
    # Port: 5432
    # username: postgres
    # password: hpdeskjetd1460
    # Database: Habits##
    conn = None
    cursor = None
    autocommit = ISOLATION_LEVEL_AUTOCOMMIT

    def __init__(self):
        self.createSession()
        self.obtainCursor()
        self.isolationLevelAuto()
        self.tableCreate()

    # connects to the postgreSQL database

    def createSession(self):
        '''creates a session to connect to the database,
        it does not require an input
        '''
        try:
            self.conn = psycopg2.connect(
                database="Habits",
                user="postgres",
                host="127.0.0.1",
                password="hpdeskjetd1460",
                port="5432"
            )

        except Exception as err:
            print(f'Unexcpected {err}, {type(err)=}')
            raise

    # obtains the cursor
    def obtainCursor(self):
        '''It connects to the cursor, this is used to executed commands.
        It does not require an input'''

        try:
            self.cursor = self.conn.cursor()

        except Exception as err:
            print(f'Unexcpected {err}, {type(err)=}')
            raise

    # isolation level autocommit
    def isolationLevelAuto(self):
        '''Establishes zhe isolation level to autocommit.
        It does not require an input'''
        try:
            self.conn.set_isolation_level(self.autocommit)
        except Exception as err:
            print(f'Unexcpected {err}, {type(err)=}')
            raise

    # creates database for the application, if this does not exist already
    def databaseCreate(self):
        '''Creates the database "HabitsProject" where all the information is to be stored.
        It does not require an input'''
        createDatabe = 'CREATE DATABASE "HabitsProject";'

        try:
            self.cursor.execute(createDatabe)

        except Exception as err:
            print(f'Unexcpected {err}, {type(err)=}')
            raise

    # executes the commandas send to the DBMS included in the variable text
    def execute(self, text: str) -> None:
        '''It executes commands and requires the parameter text as string with the text command 
        to be executed by the DBMS'''

        try:
            self.cursor.execute(text)
        except Exception as err:
            print(f'Unexcpected {err}, {type(err)=}')
            raise

    # creates tables in the database
    def tableCreate(self) -> None:
        '''
        Creates the tables of the DBMS's model. A total of 5 tables are created.
        This function does not require an input\n
        Returns nothing
        '''

        # creates table to store period categories: daily, weekly, monthly
        createTable = 'CREATE TABLE IF NOT EXISTS categories (\
            idcategories SERIAL,\
            categories VARCHAR(50) UNIQUE,\
            PRIMARY KEY (idcategories)\
            );'

        # executes command in createTable
        self.execute(createTable)

        # creates table for periocidity related topics
        createTable = 'CREATE TABLE IF NOT EXISTS periocidity (\
            idperiocidity SERIAL,\
            start DATE,\
            finish  DATE,\
            periods INTEGER,\
            categories INTEGER REFERENCES categories (idcategories),\
            PRIMARY KEY (idperiocidity)\
            );'

        # executes command in createTable
        self.execute(createTable)

        # creates table to store user information for accessing the software
        createTable = 'CREATE TABLE IF NOT EXISTS users (\
            iduser SERIAL,\
            name VARCHAR(100),\
            lastname  VARCHAR(100),\
            email VARCHAR(200),\
            password VARCHAR(200),\
            PRIMARY KEY (iduser)\
            );'

        # executes command in createTable
        self.execute(createTable)

        # creates table for habits
        createTable = 'CREATE TABLE IF NOT EXISTS habits (\
            idhabits SERIAL,\
            name VARCHAR(100),\
            description VARCHAR(500),\
            periocidity INTEGER REFERENCES periocidity (idperiocidity) ON DELETE CASCADE,\
            iduser INTEGER REFERENCES users (iduser),\
            PRIMARY KEY (idhabits)\
            );'

        self.execute(createTable)

        # creates table to store when a habit was checked
        createTable = 'CREATE TABLE IF NOT EXISTS checked (\
            idchecked SERIAL,\
            checkeddate DATE,\
            checked BOOLEAN,\
            idhabits INTEGER REFERENCES habits (idhabits),\
            PRIMARY KEY (idchecked)\
            );'

        # executes command in createTable
        self.execute(createTable)

     # adds record to table categories
    def addRecordsCategories(self, categories: str) -> None:
        '''Adds records to table of categories. The variable categories is mandatory and has to be a string type'''

        record = "INSERT INTO {} (categories) VALUES ('{}');".format(
            'categories', categories)
        self.execute(record)

     # adds record to table checked
    def addRecordsChecked(self, checkeddate: str, checked: bool, idhabits: int) -> int:
        '''
        Adds a record in the table checked of the DBMS.\n
        checkeddate as string is the date when the habit was checked. Format dd.MM.YYYY.\n
        checked as bool indicates if the record was checked.Format dd.MM.YYYY\n
        idhabits is the ID of the table habits.\n
        Returns the id of the added record.
        '''

        record = "INSERT INTO {} (checkeddate, checked, idhabits) VALUES('{}',{},{}) RETURNING idchecked;".format(
            'checked', checkeddate, checked, idhabits)
        self.execute(record)
        return self.cursor.fetchone()[0]

     # adds record to table periocidity
    def addRecordsPeriocidity(self, start: str, end: str, periods: int, categories: int) -> int:
        '''
        Adds a record in the table periocidity of the DBMS.\n
        start as string is the start date of the habit to be tracked. Format dd.MM.YYYY.\n
        end as string is the end date of the habit to be tracked.Format dd.MM.YYYY\n
        period is an integer value that indicates the quantity of days, weeks, or months when the habit will be tracked.\n
        categories is an integer between 1 and 3 that indicates if the period when the habit is to be tracked is daily, weekly, or monthly respectively.\n
        Returns the id of the added record.
        '''
        record = "INSERT INTO {} (start, finish, periods, categories) VALUES ('{}','{}',{},{}) RETURNING idperiocidity;".format(
            'periocidity', start, end, periods, categories)
        self.execute(record)
        return self.cursor.fetchone()[0]

    # adds record to table habits
    def addRecordsHabits(self, name: str, description: str, idperiocidity: int, iduser: int) -> int:
        '''
        Adds a record in the table habits of the DBMS.\
        name as string is the name of the habit to be tracked.\
        description as string is a description of the habit to be tracked.\
        idperiocidity is an integer value that links with the information of the table periocidity.\
        Returns the id of the added record.
        '''
        record = "INSERT INTO {} (name, description, periocidity, iduser) VALUES ('{}','{}',{},{}) RETURNING idhabits;".format(
            'habits', name, description, idperiocidity, iduser)
        self.execute(record)
        return self.cursor.fetchone()[0]

     # adds record to table users
    def addRecordsUsers(self, name: str, lastname: str, email: str, password: str) -> int:
        '''
        Adds a record in the table users of the DBMS.\
        name as string is the name of the user.\
        lastname as string is the last name of the user.\
        email as string is the e-mail of the user.\
        password as string is the password selected by the user to get access to the info .\
        Returns the id of the added record.
        '''
        record = "INSERT INTO {} (name, lastname, email, password) VALUES ('{}','{}','{}','{}') RETURNING iduser;".format(
            'users', name, lastname, email, password)
        self.execute(record)
        return self.cursor.fetchone()[0]

    # deletes records of table by ID number
    def deleteRecord(self, table: str, id: str, idnumber: int) -> None:
        '''It deletes a record in a defined table by selecting an id-number from the column of id-numbers.\
        It requires table as a string which is tha name of the table where the record is to be deleted;\
        the name of the column which contains the id-numbers as a string in the parameter id; and the idnumber which\
        is the id-number of the record to be deleted.\n It has not return value.
        '''
        delete = 'DELETE FROM {} WHERE {}={};'.format(table, id, idnumber)
        self.execute(delete)

    # loads the information of the defined table into the app
    def load(self, table: str) -> list:
        '''Gets all the registers of the table indicated in "table". The parameter "table" is a string that corresponds to the name of the table.\
        Returns a list of tuples with the records.
        '''
        select = 'SELECT * FROM {}'.format(table)
        self.execute(select)

        return self.cursor.fetchall()

    # loads the password and email of the user's table into the app
    def loadPass(self) -> list:
        '''
        Gets all records from the table "users" and returns them as a list of tuples.\
        It has not requirements but self.
        '''
        select = 'SELECT * FROM users;'.format()
        self.execute(select)

        return self.cursor.fetchall()

    # loads information from the database, this is a more general function
    def loadSpecific(self, table: str, list: list, col: str, value) -> list:
        '''
        Returns a list of tuples with the requested information. It requires four parameters "table"\
        as a string and corresponds to the name of the table; "list" as a list of strings which corresponds\
        to the name of the columns to be recovered; "col" as a string which corresponds to the name of the colunm\
        to be used for the selection of the records; and "value" which corresponds to a value used to filter the information to be shown.\n\
         select = 'SELECT {} FROM {} WHERE {}={};'.format(', '.join(list), table, col, value)
        '''
        select = 'SELECT {} FROM {} WHERE {}={};'.format(
            ', '.join(list), table, col, value)
        self.execute(select)

        return self.cursor.fetchall()

    # adds exemplary records to the database to be use to show the user
    def exemplaryRecords(self) -> None:
        '''Creates a set of exemplary records to give an example of the possibilities of the app.
        It requires self. Returns nothing.
        '''

        # set the parameters to be stored as example
        examplehabitname = ['read', 'study', 'clean', 'trash', 'wash']
        examplehabitdescription = ['The habit of reading is the practice of engaging with written material, such as books, articles, or online content, on a regular basis. It involves devoting time and attention to reading as a form of entertainment, education, or personal growth.',
                                   'The habit of studying refers to the regular and intentional practice of acquiring knowledge, understanding concepts, and mastering skills through dedicated learning efforts. It involves setting aside specific time and engaging in focused activities aimed at gaining new information or improving existing abilities.',
                                   'The habit of cleanliness encompasses regularly maintaining tidiness and hygiene in one´s surroundings. It involves keeping living spaces, work areas, and personal belongings clean and organized.',
                                   'This habit involves being mindful of the waste we generate and taking responsible actions to minimize its impact on the environment. It includes activities such as reducing, reusing, recycling, and properly disposing of waste materials.',
                                   'Sorting, Pre-Treating, Selecting the right cycle and temperature, Adding detergent, Loading the washing machine, Starting the wash cycle, Drying, Folding and storing']
        exampleperiocidity = ['daily', 'monthly', 'weekly', 'daily', 'weekly']

        # exemplary start and end dates
        exampletstartdate = ['2020-05-31',
                             '2020-05-31', '2020-05-31', '2020-05-31', '2021-06-25']
        exampleenddate = ['2022-09-25',
                          '2022-07-25', '2022-10-25', '2022-07-25', '2023-10-25']

        # converts datatype from string to datetime
        exampletstartdate = self.strtpdatetime(exampletstartdate)
        exampleenddate = self.strtpdatetime(exampleenddate)

        # adds records to tables
        for i, j, k, l, m in zip(exampletstartdate, exampleenddate, exampleperiocidity, examplehabitname, examplehabitdescription):
            # gets the periods.
            periods = self.calPeriods(i, j, k)

            # changes periocidity from string to integer
            k = self.conPeriocityInt(k)

            # adds the records to periocidity table and gets the id generated from the record
            periocidityid = self.addRecordsPeriocidity(i, j, periods, k)

            # adds record to habits´ table
            habitid = self.addRecordsHabits(l, m, periocidityid, self.iduser)

            # checks randomly some dates between for the period in question.
            tocheck = self.randomDates(periods, k, i)

            # adds records
            for x in tocheck:
                self.addRecordsChecked(x, True, habitid)
