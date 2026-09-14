# Parent Class 1
class Camera:
    def take_photo():
        print("You Take the Photo")

class Phone:
    def make_call():
        print("You make Call to ABC")
    
class SmartPhone(Camera, Phone):
    pass

