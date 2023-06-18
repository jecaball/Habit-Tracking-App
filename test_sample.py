# imports modules
from user import user
from check import time
import datetime as dt
from habits import habits
from analytics import analytics
from store import store
import random


# class test for testing user class
class TestUser:

    User = user('Jorge', 'Caballero',
                'jorge_caballero@outlook.com', '123456789', 1)
    name = User.name
    lastName = User.lastName
    email = User.email
    password = User.password
    iduser = User.iduser
    convertedPassword = User.hashString()

    # testing that properties are being handled correctly
    # tests name property
    def test_Name(self):
        assert self.name == 'Jorge'

    # tests last name property
    def test_LastName(self):
        assert self.lastName == 'Caballero'

    # tests email property
    def test_Email(self):
        assert self.email == 'jorge_caballero@outlook.com'

    # tests password property
    def test_Password(self):
        assert self.password == '123456789'

    # tests password convertion
    def test_PasswordConvertion(self):
        self.convertedPassword == '15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225'

    # tests add user
    def test_AddUSer(self):
        User = user('Jorge', 'Caballero',
                    'jorge_caballero@outlook.com', '123456789')

        User.addNewUser()
        assert isinstance(User.iduser, int) == True

# test class for check class


class TestCheck:

    # tests periocityHabit module of time class (valid input)
    def test_PeriocityHabit1(self):
        # contains valid input
        testStr = 'daily'

        # initializes object
        User = time()

        # asserts
        assert User.periocityHabit(testStr) == True

    # tests periocityHabit module of time class (invalid input)
    def test_PeriocityHabit2(self):
        # contains valid input
        testStr = 'wk'

        # initializes object
        User = time()

        # asserts
        assert User.periocityHabit(testStr) == False

    # tests checkedHabit module of time class (chkTime==True)
    def test_CheckedHabit(self):
        # initializes object
        User = time()

        User.checkedHabit(True)

        # asserts
        assert User.check == True

    # tests checkedHabit module of time class (date)
    def test_CheckedHabit1(self):
        # initializes object
        User = time()

        User.checkedHabit(True)

        # asserts
        assert User.chkTime == dt.date.today()

    # tests startHabit module of time class
    def test_StartHabit(self):
        # initializes object
        User = time()

        User.startHabit()

        # asserts
        assert User.startTime == dt.datetime.today()

    # test finishHabit module of time class
    def test_FinishHabit(self):
        # Initializes object
        User = time()

        result = User.finishHabit('2023-02+20')

        # asserts
        assert result == False

    # test calPeriods module of time class
    def test_CalPeriods(self):
        # Initializes object
        User = time()

        # start date
        start = dt.date(2023, 10, 1)

        # end date
        end = dt.date(2023, 11, 1)

        # gets returned results from module
        results = User.calPeriods(start, end, 'weekly')

        # asserts
        assert results == 5

    # test conPeriocityInt of time class
    def test_ConPeriocityInt(self):
        # Initializes object
        User = time()

        # gets returned value from module
        results = User.conPeriocityInt('monthly')

        # asserts
        assert results == 3

    # test conPeriocityTex of time class
    def test_ConPeriocityTex(self):
        # Initializes object
        User = time()

        # gets returned value from module
        results = User.conPeriocityTex(1)

        # asserts
        assert results == 'daily'

    # test filtdate of time class
    def test_FiltDate(self):
        # Initializes object
        User = time()

        # creates an example list, element 5 will have the dates
        listhabits = [[0, 1, 2, 3, 4, dt.date(2023, 2, 3)],
                      [0, 1, 2, 3, 4, dt.date(2023, 3, 3)],
                      [0, 1, 2, 3, 4, dt.date(2023, 4, 3)],
                      [0, 1, 2, 3, 4, dt.date(2023, 5, 3)],
                      [0, 1, 2, 3, 4, dt.date(2023, 8, 3)]]

        # gets returned value from module
        results = User.filtdate(listhabits=listhabits)

        # asserts
        assert len(results) == 1

    # test strtpdatetime of time class
    def test_StrtpDatetime(self):
        # Initializes object
        User = time()

        # creates an example list of dates
        listofdates = ['2023-05-06',
                       '2023-06-06',
                       '2023-07-06',
                       '2023-08-06',
                       '2023-09-06']

        # gets returned value from module
        results = User.strtpdatetime(listofdates=listofdates)

        # randomly generates a number between 0-4
        randomNumber = random.randint(0, 4)

        # asserts
        assert isinstance(results[randomNumber], dt.datetime) == True

# test class for habits class


class Testhabits:

    # test addHabits of the habits class
    def test_AddHabits(self):
        # initializes object
        User = habits()

        # adds habit's name
        User.addHabits('Cleaning')

        # asserts
        assert User.habit == 'Cleaning'

    # test addHabitSpecification of the habits class
    def test_AddHabitSpecification(self):
        # initializes object
        User = habits()

        # adds habit's specification
        User.addHabitSpecification('Cleaning the house')

        # asserts
        assert User.specification == None

    # test joindb of the habit class
    def test_Joindb(self):
        # initializes object
        User = habits()

        # creates an example list
        listofdates = [['2023-05-06'],
                       ['2023-06-06'],
                       ['2023-07-06'],
                       ['2023-08-06'],
                       ['2023-09-06']]

        # creates a second example list
        list2 = [[1], [2], [3], [4], [5]]

        # gets the returned value from the module
        results = User.joindb(listofdates, list2)

        # asserts
        assert isinstance(results, list) == True

# test class for habits class


class Testanalytics:

    # test longStreak of the analytics class
    def test_LongStreak(self):
        # initializes object
        User = store()

        # gets the list of habits for the user-id
        listhabits = User.loadSpecific(
            'habits', ['idhabits', 'name', 'periocidity'], 'iduser', 1)

        # gets the list of periocidity
        listperiocity = User.load('periocidity')

        # gets the list of checked habits
        listchecked = User.load('checked')

        # initializes second object
        Streak = analytics()

        # gets the longest streak and puts it in the veraible result
        result = Streak.longStreak(listhabits, listperiocity, listchecked)

        # asserts
        assert result == [23, 'day(s)', 'wash']

    # test listid of the analytics class
    def test_Listid(self):

        # initializes object
        User = store()

        # gets the list of habits for the user-id
        listhabits = User.loadSpecific(
            'habits', ['idhabits', 'name', 'periocidity'], 'iduser', 1)

        # initializes second object
        Streak = analytics()

        # execute module to be tested
        Streak.listid(listhabits, 'idhabits')

        # asserts
        assert isinstance(Streak.idhabits, list) == True

    # test countTime of the analytics class
    def test_CountTime(self):
        # initializes object
        User = store()

        # gets the list of habits for the user-id
        listchecked = User.loadSpecific(
            'checked', ['idchecked', 'checkeddate', 'checked', 'idhabits'], 'idhabits', 3)

        # initializes second object
        Streak = analytics()

        # execute module to be tested and get results
        results = Streak.countTime(2, listchecked)

        # asserts
        assert results == [4, 'week(s)']
