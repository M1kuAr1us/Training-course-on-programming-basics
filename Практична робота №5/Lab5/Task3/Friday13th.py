import datetime

def friday_calculate(year, month):
    date = datetime.date(year, month, 13)

    if date.weekday() == 4:
        return True
    else:
        return False

month = int(input("enter the number of month: "))
year = int(input("enter the year: "))
print(friday_calculate(year, month))