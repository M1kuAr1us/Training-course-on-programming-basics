import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def parse_time_input(time_str):
    try:
        time_obj = datetime.strptime(time_str, "%I:%M %p")
        return time_obj, "civilian"
    except ValueError:
        try:
            time_obj = datetime.strptime(time_str, "%H:%M")
            return time_obj, "military"
        except ValueError:
            raise ValueError("Invalid time format. Use 'HH:MM' or 'HH:MM AM/PM'.")

def get_time_text(time_obj, mode):
    if mode == "civilian":
        hour = time_obj.strftime("%I").lstrip("0")
        minute = time_obj.strftime("%M")
        am_pm = time_obj.strftime("%p").lower()
        if minute == "00":
            return f"It's {hour} o'clock {am_pm}."
        else:
            return f"It's {hour}:{minute} {am_pm}."
    else:
        hour = time_obj.strftime("%H")
        minute = time_obj.strftime("%M")
        return f"{hour}{minute} hours."

def main():
    time_input = input("Enter the time (e.g. '13:45' or '01:45 PM'):")
    try:
        time_obj, mode = parse_time_input(time_input)
        time_text = get_time_text(time_obj, mode)
        print("Voiceover:", time_text)
        speak(time_text)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()