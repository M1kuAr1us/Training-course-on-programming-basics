from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def get_local_time(latitude, longitude):
    timezone_parse = TimezoneFinder().timezone_at(lng=longitude, lat=latitude)
    timezone = pytz.timezone(timezone_parse)
    local_time = datetime.now(timezone)

    return local_time.strftime('%Y-%m-%d %H:%M:%S')

lat = float(input("Enter latitude: "))
lon = float(input("Enter longitude): "))
print(f"Local time: {get_local_time(lat, lon)}")
