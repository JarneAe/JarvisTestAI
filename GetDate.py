from num2words import num2words
from Narrator import Narrator
import calendar as cld
import datetime as dt


def getDate():

    # Instantiate the datatime.datetime.now() method
    now = dt.datetime.now()

    # Declare certain time related variables
    month_names = []
    dayNumCurrent = now.day
    monthNumCurrent = now.month
    currentDate = dt.datetime.today()
    weekDayCurrent = cld.day_name[currentDate.weekday()]

    # Get a list of months
    for i in range(1, 12):
        month_names.append(cld.month_name[i])

    # Pass the arguments in a string and let the narrator say it
    narrator = Narrator("Today is " + weekDayCurrent + " " + month_names[int(monthNumCurrent) - int(1)] + " the " + num2words(dayNumCurrent, to="ordinal_num") + ".")
    narrator.narrator()

    return True
