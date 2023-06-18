# class definition
class habits():
    '''
    Habits class.
    This class allows for a temporal storage of some parameters of the habits.
    '''
    # definition of the class´properties
    habit = None
    specification = None

    def __init__(self):
        '''
        The class can be initiated with a habit and its specification.
        It allows strings only
        '''
        # stores the habit
        self.habit = None

        # stores the specification of the habit
        self.specification = None

    # adds habits of the habit property list
    def addHabits(self, newHabit: str) -> None:
        '''
        Adds habits to the habits list "habit".
        it allows only string values, empty inputs are not allowed.
        when the input was correctly added it indicates so.
        '''
        if newHabit:
            self.habit = newHabit
            print('The habit {} was just added'.format(newHabit))
        else:
            print('the input was empty or invalid, please try again')

    # adds specifications of the habit
    def addHabitSpecification(self, specification) -> None:
        '''
        Adds specifications to the habits.
        The specifications of habit shall have a least 50 characters.
        Every habit has a specification and viceversa.
        It allows only string.
        When the input satisfy the requirements it will be indicated in the command line
        '''
        # establishes a minimum of character for the description of the habit
        if len(specification) > 50 and specification:
            self.specification = specification
            # informs the user that the specification was added
            print('The specification was added succefully')
        else:
            # informs the user that the information provided was not valid
            print('the input was empty or invalid, please try again')

    # deletes habits
    # to be modified according the new model#ä##############
    def deleteHabits(self, habit: str) -> None:
        '''
        Deletes habits and their specifications
        it accepts strings or lists of strings of the habits
        It does not distinguish between upper case and lower case

        Example1 deleteHabits('Dance')
        >>>>> NOT USED<<<<<<
        '''

        try:
            # gets the index of the habit to be removed and deletes the habit
            index = self.habit.index(habit)
            self.habit.remove(habit)

            # gets the specification to be removed and deletes it
            index = self.specification[index]
            self.specification.remove(index)

            # informs that the process was a sucess
            print(
                'The habit {} and its specification were just deleted'.format(habit))

        except Exception as err:
            # informs about the error
            print(f'Unexcpected {err}, {type(err)=}')
            raise

        finally:
            # advice
            print('try again')

    # joins database of habit and database of periods
    def joindb(self, habits: list, periodicity: list) -> list:
        '''
        Takes the list of habits and the list of periocidities and put them together in one list.\
        It gets habits as a list and periocidity as a list. The number of row of the list must be the same. \
        It returns a list.
        '''

        join = []
        for i, j in zip(habits, periodicity):
            # joins lists
            join.append(i+j)

        # returns results
        return join
