import datetime
from datetime import date
import pyttsx3

birthday = datetime.datetime(2022,7,2)
print(birthday)
# time_of_wishing = birthday.strftime("%b %d %Y %H:%M:%S")
# print(time_of_wishing)
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
print(current_time)
if birthday == current_time:
    pyttsx3.speak("happy birthday failure")