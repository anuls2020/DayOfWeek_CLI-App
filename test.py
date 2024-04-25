# DayOfWeek.py
import sys
from datetime import datetime


def get_day_of_week(date_str):
    try:
        # Parsing the date string into a datetime object using American date format
        date_obj = datetime.strptime(date_str, '%m-%d-%Y')
        # Getting the day of the week as a string
        return date_obj.strftime("%A")
    except ValueError:
        return "Invalid date format. Please use MM-DD-YYYY."


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python <scriptname.py> MM-DD-YYYY")
    else:
        date_input = sys.argv[1]
        day = get_day_of_week(date_input)
        print(f"The day of the week for {date_input} is {day}.")
