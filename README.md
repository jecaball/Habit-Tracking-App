# Habit-Tracking-App
Habit tracking app in python for Assignments for the course: Object Oriented and Func-tional Programming with Python (DLBDSOOFPP01)
This guide will help you to navigate the Habit Tracking App (HTA); read the document throughly and follow the recommendations written here.

# Requirements
- Python version 3.10 or superior. If not installed in your computer, you can install it following the recommendations indicated in https://www.python.org/downloads/
- Pandas latest version. More information about pandas module and its installation process can be found here: https://pandas.pydata.org/docs/getting_started/install.html
- psycopg2 latest version. More information about psycopg2 module and its installation process can be found here: [https://pandas.pydata.org/docs/getting_started/install.html](https://pypi.org/project/psycopg2/)
- Anaconda (Optional). Let you easily manage integrated applications, packages, and environments without using the command line. You can download Anaconda in the following web-address: https://www.anaconda.com/download
You must install these modules in your python environment before being able to use the HTA.

# Installing HTA in your computer
Install the required modules pandas and psycopg2. Then, copy the following documents and paste them in a folder of your preference:
main.py
store.py
check.py
user.py
habits.py
analytics.py


# Installing pandas (required)
1. Open the folders where the *.py files are located
2. Press right click in the folder, a menu will appear and press on "Open in Terminal"
3. write "pip install pandas" and press enter
4. Wait until the installation is done

# Installing psycopg2 (required)
1. Open the folders where the *.py files are located
2. Press right click in the folder, a menu will appear and press on "Open in Terminal"
3. write "pip install psycopg2" and press enter
4. Wait until the installation is done

# Opening HTA
1. Open the folders where the *.py files are located
2. Press right click in the folder, a menu will appear and press on "Open in Terminal"
3. In the terminal, write "python main.py"
4. Follow the instructions of the menu.

# Navigating through HTA
Navigate iteractively throught the different menus of the app. Follow the intructions and provide the input when requested.
Using the app requires to create an account, that later can be open again to keep tracking habits. Once you have an account you will encounter a menu as indicated below:
- Add a habit (a) -> adds an habit and its description the database. Description has to be at least 51 characters long.
- Check a habit (c) -> Marks a selected habit as checked.
- Delete a habit (d) -> Deletes a habit and their linked information from the database
- Show a list with all tracked habits (l1) -> It shows a list of all tracked habits. Here tracked habits are those which end date is later as from the day of review.
- Show a list of habits by periocidity (l2) -> It shows a list of habits organized by their periodicity.
- Return the longest run streak (r1) -> It provides you with the habit with the longest streak. Here that means that, for example, 3 counted streak of 3 weeks has a longer streak than 5 days streak. The measure is by number regardless the unit.
- Return the longest run streak for a given habit (r2) -> It provides the longest streak of a selected habit. Apply same parameters as in line 35.
- Exit (e) -> Exits from the application
