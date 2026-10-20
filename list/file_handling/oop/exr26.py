import random
import uuid

class Notification:
    def notify(self):
        raise NotImplementedError
    
    
class SMSNotification(Notification):
    
    def __init__(self, phone_number, code) -> None:
        self.code = code
        self.phone_number = phone_number
        super().__init__()
    
    def notify(self):
        print("Sending SMS notification...")
        
        
class EMAILNotification(Notification):
    
    def __init__(self, email, code) -> None:
        self.email = email
        self.code= code
        super().__init__()
    
    def notify(self):
        print("Sending EMAIL notification...")
        
        
class PUSHNotification(Notification):
    
    def __init__(self, device_id, code) -> None:
        self.device_id = device_id
        self.code = code
        super().__init__()
    
    def notify(self):
        print("Sending PUSh notification...")
        
        

# user udemydan kurs sotib oldi endi quyidagi notifla borishi kerak
        
notifs = [
    SMSNotification(phone_number="+998953190373", code=random.randrange(1000, 9999)),
    EMAILNotification(email="empty4035@gmail.com", code=random.randrange(1000,9999)),
    PUSHNotification(device_id=uuid.uuid4(), code=random.randrange(1000, 9999))
]


for notif in notifs:
    notif.notify()



