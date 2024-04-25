# DayOfWeek.py
import sys
from datetime import datetime


def get_day_of_week(date_input):
    try:
        # Parsing the date_input string into a datetime object using "strptime"
        date_obj = datetime.strptime(date_input, '%m-%d-%Y')
        # getting the day of the week as a string using "strftime" from the parced date_obj
        return date_obj.strftime("%A")
    except ValueError:
        return "Invalid date format, Please use MM-DD-YYYY."


if __name__ == "__main__":
    #Check the script execution passes exactly two parameters, the script name and the date
    if len(sys.argv) != 2:
        print("Script Usage: python <scriptname.py> MM-DD-YYYY")
    else:
        # Accept the input from the terminal along with the script name
        # sys.argv[0] -- Script Name, sys.argv[1] -- argument to run the script, here it is the date in string format
        date_input = sys.argv[1]
        #Pass the string date to "get_day_of_week()" function
        day = get_day_of_week(date_input)
        print(f"The day of the week for {date_input} is {day}")
