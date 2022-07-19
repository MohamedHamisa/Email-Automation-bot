!pip install SpeechRecognition
!pip install pyttsx3
import smtplib  #system mail transfer protocol to send email 
import speech_recognition as sr
import pyttsx3 #python text to speech version 3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587) #to create server gmail is server that will be used to send email and port number
    server.starttls() #transport layer security to tell the server that i'm trust person
    # Make sure to give app access in your Google account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = 'receiver''
    email['Subject'] = 'subject'
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dude': 'COOL_DUDE_EMAIL',
    'bh': 'diamond@bts.com',
    'p': 'jennie@blackpink.com',
    'lisa': 'lisa@blackpink.com',
    'i': 'i@redvelvet.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?') #to tel that email is sent
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()









