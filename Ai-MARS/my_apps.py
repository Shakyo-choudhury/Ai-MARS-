# from imghdr import what
# from re import sub
import subprocess
from my_inputs import talk, take_command
def my_app():
    edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    # excel = "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
    vs_code = "C:\Users\SHAKYO\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    whatsapp = "C:\Users\SHAKYO\AppData\Local\WhatsApp\WhatsApp.exe"
    input1 = str(input("enter the app you wanna open: "))
    if "edge" in input1:
        talk("opening edge")
        subprocess.Popen([edge])
        subprocess.call(edge)
    elif "chrome" in input1:
        talk("opening chrome")
        subprocess.Popen([chrome])
        subprocess.open(chrome)
    elif "vs code" in input:
        talk("opening vs code")
        subprocess.Popen([vs_code])
        subprocess.open(vs_code)
    elif "whatsapp" in input:
        talk("opening whatsapp")
        subprocess.Popen([whatsapp])
        subprocess.open(whatsapp)
    else:
        talk("invalid input")
while True:
    my_app()