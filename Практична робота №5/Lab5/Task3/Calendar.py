import calendar

year = int(input("enter the year: "))
month = int(input("enter the number of month: "))

def formatted_calendar(year, month):
    cal = calendar.TextCalendar(firstweekday=0)
    return cal.formatmonth(year, month)

print(f"\n{formatted_calendar(year, month)}")