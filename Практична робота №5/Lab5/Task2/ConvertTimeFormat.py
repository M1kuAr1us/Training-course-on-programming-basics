from datetime import datetime

def time_convert(time):
    if "am" in time or "pm" in time:
        time_parse = datetime.strptime(time, "%I:%M %p")
        return time_parse.strftime("%H:%M")
    else:
        time_parse = datetime.strptime(time, "%H:%M")
        return time_parse.strftime("%I:%M %p").lower()

time = input("enter time (\"hh:mm\" or \"hh:mm am/pm\"): ")
print(f"\"{time}\" -> \"{time_convert(time)}\"")