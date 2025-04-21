import datetime

def thursday_calculate(year, month):
    date = datetime.date(year, month, 1)

    while date.weekday() != 3:
        date += datetime.timedelta(days=1)

    return date.strftime("%Y-%m-%d")

year = int(input("enter the year: "))
month = int(input("enter the number of month: "))
print(f"{year}, {month} -> \"{thursday_calculate(year, month)}\"")