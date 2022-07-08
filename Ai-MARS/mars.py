import datetime
from datetime import date
from email import message
import json
import random
import math
import cv2
from my_apps import my_app
from my_inputs import take_command, talk
from pywhatkit.ascii_art import image_to_ascii_art
from bit_coin_updates import bitcoin
from my_camera import cam
from wish_me import wishme
from cv2 import *
from my_news import pynewsindia
from my_entertainment_news import entertainment
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
from email.message import EmailMessage
import requests
import time
import math
import os
import json
import sys
from my_email import get_email_info
def mars():
    command= take_command()
    print(command)
    if 'play' in command:
        video= command.replace('play', '')
        talk("okay i will play"+video+"on youtube")
        pywhatkit.playonyt(video)
    elif 'say me about' in command:
        info=command.replace('say me about', '')
        data=wikipedia.summary(info)
        talk(data)
   
    elif 'what is my favorite language' in command:
        talk("your favorite language is Bengali")
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("bro the time is"+time)
    elif 'google' in command:
        google=command.replace('google', '')
        talk("ok i will search it for you on google"+google)
        information= pywhatkit.info(google, lines=4)
        print(information)
    elif 'convert the follwing image to ascii art' in command:
        talk("okay i will convert the image for you but you need to enter the realtive path of the image")
        img_path=str(input("enter the realtive path of the image you want to convert"))
        output_file=str(input("enter the file name in which you want to save"))
        pywhatkit.image_to_ascii_art(img_path, output_file)
    elif 'take a screenshot' in command:
        talk('okay i will take a screenshot for you')
        file_name=str(input("enter the file name in which you wish to save the screenshot"))
        pywhatkit.take_screenshot(file_name)
    elif 'shutdown the computer' in command:
        talk('okay i will shutdown the computer')
        pywhatkit.shutdown(time=20) 
    elif 'answer the folwwing' in command:
        my_query=command.replace('answer the following', '')
        my_info= pywhatkit.search(my_query)
        print(my_info)
        talk(my_info)
    elif 'open google meet' in command:
        talk('okay i will open google meet for you')
        webbrowser.open("https://meet.google.com/")
    elif 'bitcoin updates' in command:
        talk('okay i will say you the updates about bitcoin')
        var_bit=1
        while var_bit<2:
            bitcoin()
            var_bit=var_bit+1
    elif 'send a whatsapp message to a group' in command:
        talk("okay i will send the message in the group but you need to enter some details") 
        group_name=str(input("enter the group name"))
        text_message=str(input("enter the text message you wanna send"))
        hour_12hr=int(input('enter the hour you want to send the message (12 hr)')) 
        minute_min=int(input("enter the minute you wanna send the message"))
        pywhatkit.sendwhatmsg_to_group(group_name, text_message, hour_12hr, minute_min)
    elif 'send an image to whatsapp group' in command:
        talk("okay i will send but you have to enter some details")
        grp_name=str(input("enter the group name"))
        image_path=str(input('enter the relative path of the image you wanna send'))
        caption= str(input("enter the caption"))
        pywhatkit.sendwhats_image(grp_name, image_path, caption) 
    elif 'create meeting' in command:
        talk('ok i will create a meeting for you')
        webbrowser.open_new_tab('http://meet.google.com/new') 
    elif 'open youtube' in command:
        talk('okay i will open youtube for you')
        webbrowser.open('https://www.youtube.com/')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google classroom' in command:
        talk("okay i will open google classroom for you")
        webbrowser.open('https://classroom.google.com')
    elif 'repeat after me' in command:
        talk('ok bro i will repeat after you')
        repeat=take_command()
        talk(repeat)
    elif 'send a whatsapp message' in command:
        talk('okay i will send the whatsapp message but you need to enter some details')
        phno=int(input('enter the receiver phone number'))
        hour= int(input('hour at which it needs to be sent(12hr)'))
        min=int(input('enter the minute at which you want to send the message'))
        pywhatkit.sendwhatmsg(phno, hour, min)
    elif 'convert the following text to handwriting' in command:
        talk('okay but you need to enter some details')
        string=str(input('enter the sting that you want to convert'))
        save_to=str(input('enter the file name you want to save it( add.png after it)'))
        pywhatkit.text_to_handwriting(string, save_to, rgb=(0,0,0))
    elif 'send a mail' in command:
        talk('okay i will send the mail')
        h=1
        while h<2:
            get_email_info()
            h=h+1
    elif 'camera' in command:
        talk('okay i will open camera for you')
        c=1
        while c<2:
            cam()
            c=c+1
    elif 'news' in command:
        talk('okay i will tell you the news')
        n =1
        while n<2:
            pynewsindia()
            n=n+1
    elif 'what is the entertainment news' in command:
        e=1
        while e<2:
            entertainment()
            e=e+1
    elif 'open some apps for me' in command:
        o=1
        while o<2:
            my_app()
            o=o+1
    else:
        talk('thank you for using mars ai')
    
i = 1
while i<2:
    wishme()
    i=i+1



while True:
    mars()