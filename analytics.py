# imports required modules
import pandas as pd


class analytics:
    '''
    Analytics class.
    This class is in charge to produce the analytics of the tracking habits app. 
    It requires pandas.
    '''
    longeststreak: list = None
    idhabits: list = []
    idperiocidity: list = []

    def __init__(self) -> None:
        pass

    # returns the longest run streak
    def longStreak(self, listhabits: list, listperiocidity: list, listchecked: list) -> list:
        '''
        It gets the longest run streak from the variable "listhabits".\
        "listhabits" is a type list object which contains the dates where the habit was checked.\n\
        Returns a string type object indicating which habit has the longest run streak and their value.
        '''
        # creates a list of idhabits that will be useful for extracting other information
        self.listid(listhabits, 'idhabits')

        # creates a list of idperiocidity that will useful to check the periocidity and do the calculations
        self.listid(listperiocidity, 'idperiocidity')

        # goes through the process to count the streaks per habit
        for idhabits, idperiocidity in zip(self.idhabits, self.idperiocidity):

            # filters the list to get only the checked habits for a defined idhabits
            listcheckedfiltered = self.filtList(listchecked, idhabits)

            # gets periocidity from the periocidity-list as a function of the id-number
            index = -1
            for i in listperiocidity:
                index += 1
                if i[0] == idperiocidity:
                    break

            # auxiliary variable to keep track of the before and actual result of self.countTime
            aux = self.countTime(
                listperiocidity[index][4], listcheckedfiltered)
            if self.longeststreak == None:

                # gets the value of the longest streak of the first habit of the list
                self.longeststreak = aux

            elif aux[0] > self.longeststreak[0]:
                # replaces smaller long streak for the bigger one
                self.longeststreak = aux

            elif aux[0] <= self.longeststreak[0]:
                continue

        # returns the longerst run streak
        return [self.longeststreak[0], self.longeststreak[1], listhabits[index][1]]

    # creates a list of id that will be useful for extracting other information
    def listid(self, listhabits: list, name: str) -> None:
        '''
        Creates a list of ids that will be useful for extracting other information.\
        Requires a list which contains the information required, the name of the list, and self. \
        "name corresponds to: idhabits, idperiocidity, #####". It has no return value.
        '''

        for id in listhabits:
            # it assumes that the Id of the list is at the [0]
            exec('self.{}.append({})'.format(name, id[0]))

    # filters list according the value of a column
    def filtList(self, listo: list, idnumber: int) -> list:
        '''
        Filter a list according to the filtered value provided and returns a type-object list. 
        Parameter "listo" is a list-type object, "idnumber" is an integer-type object.
        '''
        # filters list according column with id-number
        filteredlist = filter(lambda c: c[3] == idnumber, listo)

        # returs filtered list
        return list(filteredlist)

    # return the longest run streak for a given habit
    def countTime(self, periocidity: int, listchecked: list) -> list:
        '''
        Counts days, weeks, or months continously checked. 
        It requires periocidity to control the period (days, weeks, or months) and is required as a value between 1 and 3
        with 1 for days, 2 for weeks, and 3 for months; and listchecked is a list-object with the information 
        coming from the table checked. Returns a list with the longest streak of the habit processed and its time frame.
        '''
        # gets the data into a dataframe form pandas for easy handleing of the information
        data = pd.DataFrame(data=listchecked, columns=[
                            'idchecked', 'checkeddate', 'checked', 'idhabits'])

        # enforces checkeddate as datetime type
        data['checkeddate'] = pd.to_datetime(data['checkeddate'])

        # gets the results according the periocidity
        if periocidity == 1:
            # gets continuos days
            s = data.groupby(
                'idhabits').checkeddate.diff().dt.days.ne(1).cumsum()
            s = data.groupby(['idhabits', s]).size(
            ).reset_index(level=1, drop=True)
            return [s.max(), 'day(s)']
        elif periocidity == 2:
            # gets continuos weeks
            data['weeks'] = data.checkeddate.dt.isocalendar().week
            data['years'] = data.checkeddate.dt.isocalendar().year.diff().fillna(
                0).cumsum().convert_dtypes(convert_integer=True)
            data['weeksc'] = data['weeks'] + \
                data['years']*52  # c is for corrected
            s = data.groupby(
                'idhabits').weeksc.diff().fillna(3).ne(1).cumsum()
            s = data.groupby(['idhabits', s]).size(
            ).reset_index(level=1, drop=True)
            return [s.max(), 'week(s)']

        elif periocidity == 3:
            # gets continuos months
            data['months'] = data.checkeddate.dt.month
            data['years'] = data.checkeddate.dt.isocalendar().year.diff().fillna(
                0).cumsum().convert_dtypes(convert_integer=True)
            data['monthsc'] = data['months']+data['years']*12

            s = data.groupby(
                'idhabits').monthsc.diff().fillna(3).ne(1).cumsum()  # c is for corrected
            s = data.groupby(['idhabits', s]).size(
            ).reset_index(level=1, drop=True)
            return [s.max(), 'month(s)']
