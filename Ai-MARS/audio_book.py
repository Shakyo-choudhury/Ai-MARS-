# importing the necessary modules 
import pyttsx3
import PyPDF2


pdf = str(input('enter the relative path or the file name of the pdf that you wanna read: ')) #takes the path of the book
book = open(pdf, 'rb')#opens the book in binary format
pdfReader = PyPDF2.PdfFileReader(book) #reading the pdf file
pages = pdfReader.numPages #gets the number of pages of the file
speaker = pyttsx3.init() #initializes pyttsx3 
page = pdfReader.getPage(0) #gets the assigned page of the pdf
text = page.extract_text() #extracts the text in the pdf

# reading the text out
speaker.say(text) 
speaker.runAndWait() 