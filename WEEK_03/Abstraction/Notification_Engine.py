"""The Challenge: "The Notification Engine"
Imagine you are building a notification system for a social media app. Users can choose to receive alerts via Email or SMS.

Requirements:

Abstract Base Class: Create a class called Notification with an abstract method called send(self, message).

Concrete Class 1: Create an EmailNotification class. Its send method should print: "Email sent with message: [message]".

Concrete Class 2: Create an SMSNotification class. Its send method should print: "SMS sent with message: [message]".

The Data: You are given a list of dictionaries representing incoming alerts:
"""

from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass
class EmailNotification(Notification):
    def send(self,message):
       self.msg=message
       print(f'email sent with {message}')
class SMSNotification(Notification):
    def send(self,message):
        self.msg=message
        
        print(f'sms is sent with {message}')

email=EmailNotification()
sms=SMSNotification()

alerts = [
    {"type": "email", "msg": "Welcome to our app!"},
    {"type": "sms", "msg": "Your OTP is 1234"},
    {"type": "email", "msg": "Someone liked your photo"},
    {"type": "sms", "msg": "Your delivery has arrived"}
]
for note in alerts:
    if note['type']=='email':
        email.send(note['msg'])
    elif note['type']=='sms':
        sms.send(note['msg'])

