from num2words import num2words
import calendar as cld
import datetime as dt

class GetDate():

    def getDate(self):
        # Instantiate the datatime.datetime.now() method
        now = dt.datetime.now()

        # Declare certain time related variables
        currentDate = dt.datetime.today()
        weekDayCurrent = cld.day_name[currentDate.weekday()]
        monthNumCurrent = now.month
        dayNumCurrent = now.day
        month_names = []

        # Get a list of months
        for i in range(1, 12):
            month_names.append(cld.month_name[i])

        print("Today is " + weekDayCurrent + " " + month_names[int(monthNumCurrent) - int(1)] + " the " + num2words(dayNumCurrent, to="ordinal_num") + ".")
    
        return True