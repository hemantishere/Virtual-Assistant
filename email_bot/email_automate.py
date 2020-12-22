#Email Automation Bot using Voice assistant

#Simple mail transfer protocol python library and others
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

# A typical email list in the dictionary data type format
# Note you can modifiy these using your own values
email_list = {"hemant" : "hemant.1751@gmail.com",
              "jatin" : "jatinswami1999@gmail.com"}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("listening......")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

# Send email function!!
# Provide login details of your email provider in .txt format in the same directory!!!
def send_mail(receiver,subject,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    with open("login.txt","r") as file:
        id = file.readline().strip()
        password = file.readline().strip()
        print(id)
        print(password)
        file.close()
    server.login(id,password)
    email = EmailMessage()
    email["From"] = "hemant2017cs121@abesit.edu.in"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)

 # This function will ask name,subject,message from the user using voice
def get_email_info():
    talk("TO Whom you want to send email")
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What is the subject of your email")
    subject = get_info()
    talk("whats the message")
    message = get_info()
    send_mail(receiver,subject,message)
    talk("Your Email is Sent")
    talk("Do you want to send more email?")
    send_more = get_info()
    if "yes" in send_more:
        get_email_info()

if __name__ == "__main__":
    get_email_info()
