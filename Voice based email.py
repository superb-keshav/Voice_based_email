#importing libraries

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


#function for converting text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()

#function for taking voice input from user.
def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print("Voice Not recognized")


#function for creating server and sending email.
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('//enter your email here','//enter password here')
    email = EmailMessage()
    email['From'] = 'project4semester@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)



def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the Subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    talk('Your text has been recognized')
    send_email(receiver, subject, message)
    talk('Your email has been sent')


#listener for recognizing text.
listener = sr.Recognizer()

#creating and initializing engine
engine = pyttsx3.init()


#a dictionary of all emails.
email_list = {
  
    # We can add emails here to whom we want to send email
}


get_email_info()