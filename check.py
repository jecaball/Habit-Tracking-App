# imports datetime as dt
import datetime as dt
import math
import random


class time:
    '''Time Class.
    It handles time related calculations that envolve the habits. 
    It requires dateitme, math, and random modules'''
    periocity = None
    chkTime = None
    check = None
    startTime = None
    finishTime = None
    periods = None
    idChecked = None

    def __init__(self):
        self.periocity = None
        self.chkTime = None
        self.check = None
        self.startTime = None
        self.finishTime = None
        self.periods = None
        self.idChecked = None

    # this function keeps track of the periodicity of every habit
    def periocityHabit(self, periocity: str) -> bool:
        '''It is used to store the periocity of the habit, it allows only strings.
        Strings cannot be empty, empty value are not allowed.
        Three words are allowed Monthly, Weekly or Daily, and it is independent from lower or capitalcase'''

        # checks which periocity was selected and adds it to the property list
        if periocity.lower() == 'weekly' or periocity.lower() == 'daily' or periocity.lower() == 'monthly':
            # appends the selected periocity
            self.periocity = periocity
            # informs the selected periocity
            print('The periocity "{}" was selected succefully'. format(periocity))
            return True

        else:
            # informs that the input needs to be corrected
            print('the input was empty or invalid, please try again')
            return False

    def checkedHabit(self, chkTime: bool) -> None:
        '''It adds true or false depending on if the habit was checked that day, week, or month,
        it dependes on the periocity of the habit.
        It allows only boolean data type'''

        if True == chkTime:
            self.chkTime = dt.date.today()
            self.check = chkTime
            # informs that the habit was checked correctly
            print('The habit is been processed')
        elif False == chkTime:
            self.chkTime = dt.date.today()
            self.check = chkTime
            # informs that the habit is not yet checked
            print('The habit cannot be processed!')

    # defines when the habit starts
    def startHabit(self) -> None:
        '''
        It adds the date of start of a habit. \n
        It requires only self. \n
        Returns nothing.
        '''
        self.startTime = dt.datetime.today()

    # defines the date when the habit is not longer traced
    def finishHabit(self, finishDate: str) -> bool:
        '''It adds the date of finilization of the habit´s tracking \n
        It requires the date in format YYYY-MM-dd'''

        # converst from string to datetime format
        format = '%Y-%m-%d'
        try:
            self.finishTime = dt.datetime.strptime(finishDate, format)
        except ValueError:
            # informs something went wrong
            print('Wrong format, try again!')

            # returns False as per handeling the use of the function
            return False

        # adds number of periods to be checked according the initial and end date, and the periocity
        self.periods = self.calPeriods(
            self.startTime, self.finishTime, self.periocity)

        # informs about the number of periods when the habit will be tracked
        print('The number of periods where this activity is going to be checked is equal to {}'.format(
            self.periods))

        # returns True as per handeling the use of the function
        return True

    # calculates the number of periods according the periocity
    def calPeriods(self, startTime, finishTime, pericity: str) -> int:
        '''
        It calculates the total periods to be checked.\n
        It takes the start time and the end time of a habit and calculates the time delta between them. \n
        It requires the start and finish time, and the periocity. All of them as string.\n
        Returns an integer rounded up with the number of periods to be checked
        '''

        # calculates the time difference between two dates
        deltatime = finishTime-startTime

        if 'daily' in pericity:
            return deltatime.days
        elif 'weekly' in pericity:
            return math.ceil(deltatime.days/7)
        elif 'monthly' in pericity:
            return math.ceil(deltatime.days/30)

    # converts periocidity form its form in string to its form in integer to be stored in the long term storage
    def conPeriocityInt(self, periocity: str) -> int:
        '''
        It takes the periocity from string and converst it to integer. \n
        Requieres only periocidity as string.\n
        Returns an integer between 1 and 3.
        '''

        # makes the convertion to integer
        if 'daily' in periocity:
            return 1
        elif 'weekly' in periocity:
            return 2
        elif 'monthly' in periocity:
            return 3

    # converts periocidity from its integer from to its text form back to be presented to the user
    def conPeriocityTex(self, periocity: int) -> str:
        '''
        It takes the periocity from integer and converst it to string. \n
        Requieres only periocidity as integer.\n
        Returns a string: daily, weekly, monthly.
        '''

        # makes the convertion to string
        if 1 == periocity:
            return 'daily'
        elif 2 == periocity:
            return 'weekly'
        elif 3 == periocity:
            return 'monthly'

    # filters habits according to their end traking time
    def filtdate(self, listhabits: list) -> list:
        '''
        Filters the listhabits and returns only the records that are being actively tracked.\
        It requires "listhabits" as a list.
        It returns a list type object.
        '''
        # creates variable to temporaríly store the filtered list
        filtlist = []

        # for-loop to check every record stored in the list "listhabits"
        for i in listhabits:
            # checks the date. It is tracked if the end date is still in the future
            if i[5] >= dt.date.today():
                # appends to "filtlist" if the end date is in the future
                filtlist.append(i)

        # returns list of filtered values
        return filtlist

    # changes datatype from string to datetime
    def strtpdatetime(self, listofdates: list) -> list:
        '''
        Changes the elements of the list-type "listofdates" from string to object-type datetime. 
        Requires a list with strings with the format "YYYY-MM-DD" and returns a list with the converted values.
        '''

        # stablishes the input format
        format = '%Y-%m-%d'

        # changes datetype from string to datetime
        for i in range(len(listofdates)):
            listofdates[i] = dt.datetime.strptime(
                listofdates[i], format)

        return listofdates

    # random date generator
    def randomDates(self, periods: int, periodicity: int, start: dt.datetime) -> list:
        '''Generates random dates between from the indicated start date and up until periods.
        Returns a list with the dates to be checked
        '''
        # getting numbers from 0 to total periods
        inputs = range(periods)

        # gets random numbers in a random quantity between 10 and 70% of the periods to be filled up
        inputs = random.sample(
            inputs, math.ceil(periods*random.randint(10, 70)/100))

        # initializes variable
        list = []

        # different algorithms depending on periodicity
        #1== daily
        if periodicity == 1:

            # iterates through every element in inputs
            for i in inputs:
                list.append(start+dt.timedelta(days=i))

        # 2==weekly
        elif periodicity == 2:
            for i in inputs:
                list.append(start+dt.timedelta(days=7*i))

        # 3==monthly
        elif periodicity == 3:
            for i in inputs:
                list.append(start+dt.timedelta(days=30*i))

        # sort list
        list.sort()

        # returns list with periods to be checked
        return list
