from my_inputs import talk
import datetime
from datetime import date
def wishme():
    hour= int(datetime.datetime.now().hour)
    today= date.today()
    if hour>=0 and hour<12:
        talk("good morning i am mars sir please tell me how can i help you")
        talk(today)
    elif hour>=12 and hour<18:
         talk("good afternoon i am mars sir please tell me how can i help you")
         talk(today)
    else:
         talk("good evening i am mars sir please tell me how can i help you")
         talk(today)
if __name__==("__main__"):
    wishme()