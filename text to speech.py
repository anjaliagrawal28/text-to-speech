import PyPDF2
import pyttsx3

path =open("file.pdf","rb")

pdfReader = PyPDF2.PdfFileReader(path)

from_page = pdfReader.getPage(1)

text = from_page.extractText()
#text = pdfReader.extractText()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
